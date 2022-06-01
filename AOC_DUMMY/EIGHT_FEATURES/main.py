import os
import pandas as pd
from datetime import date
import time
import numpy as np
from B_SCR.Continious_Bayesian_Optimisation import BayesianOptimization
from B_SCR.Acquisition_utilies import AcquisitionUtilities
from B_SCR.clean_fea_dir import delete_unwanted
from B_SCR.csv_functions import rate_of_change
from B_SCR.general_functions import new_dir_add_dic, load_json_file, read_text_file, bounds_select_features, merge_dicts, write_json_file
from B_SCR.termination_function import termination_check
from B_SCR.results_plots import plot_mape_v_sim_time, best_and_worst, plot_mape_v_sim_num
from B_SCR.abaqus_functions import FEA_Function
from B_SCR.feature_selection import feature_selection, reg_features_bo


""" 
THIS SCRIPT IS PART OF A DUMMY PROJECT FOR FILIP SWIGON
TO BUILD A GUI FOR USERS.
"""
""" LIST OF USER REQUIRED INFORMATION:
CWD: CURRENT WORKING DIRECTORY - WHERE DOES THE USER WANT TO SAVE FILES/FOLDERS.
MAT_DIC: DICTIONARY OF SPECIMEN RELATED INFORMATION - E.G. GEOMETRY, MATERIAL PROPERTIES ETC. (DOE)
NUM_FEATURES: HOW MANY VARIABLES DOES THE USER WANT TO ASSESS
PBOUNDS: WHAT ARE THE BOUNDARIES FOR EACH VARIABLE?
MAX_SIMULATIONS: DOES THE USER WANT TO LIMIT THE NUMBER OF VIRTUAL EXPERIMENTS CONDUCTED, WHAT IS THE MAXIMUM? 
"""


# ##GET TODAYS DATE
today = date.today().strftime("%Y%m%d")
# ##CREATE DICTIONARY OF PATHS TO RELEVANT DIRECTORIES AND FILES
path_dic = {'cwd': os.getcwd(),
            'project_dir': os.path.join(os.getcwd(), '../'),
            'raw_data': os.path.join(os.getcwd(), '../A_RAW_DATA'),
            'doe': os.path.join(os.getcwd(), '../C_DESIGN_OF_EXPERIMENTS'),
            'build': os.path.join(os.getcwd(), '../B_SCR/aba_build.py'),
            'postp': os.path.join(os.getcwd(), '../B_SCR/aba_pp.py')}
# ##CREATE RESULTS SUBDIRECTORY
path_dic = new_dir_add_dic(dic=path_dic,
                           key='results',
                           path=path_dic['cwd'],
                           dir_name='results',
                           exist_ok=True)
# ##MAX SIMULATION NUMBERS
max_simulations = 250
# ##LIST ALL FILES IN OUR RAW DATA FOLDER (PROVIDE MATERIAL NAMES)
# material_list = os.listdir(path_dic['raw_data'])
material_list = [ 'P91_500.csv', 'P91_20_1.csv', 'P91_20_2.csv']
for i, material in enumerate(material_list):
    material = material[:-4]
    print('MATERIAL: %s' %(material))
    # ##CREATE MATERIALS SUBDIRECTORY
    path_dic = new_dir_add_dic(dic=path_dic,
                               key='curr_results',
                               path=path_dic['results'],
                               dir_name=material,
                               exist_ok=True)
    #################################
    ## DOE Data
    ################################
    doe_paths = load_json_file(os.path.join(path_dic['doe'],
                                            'RESULTS/%s/PATH_DIC.txt' %(material)))
    # ##GET MAT_DIC VALUES
    doe_mat_dic = load_json_file(doe_paths['MAT_DIC'])
    # ##PATHS IN DOE THAT NEED TO BE IN PATHS DIC
    for k in doe_paths.keys():
        if ('plastic_properties' in k) or ('fvd' in k):
            path_dic[k] = doe_paths[k]
    #################################
    ## FEATURE SELECTION
    ################################
    init_exp_df, feature_list = feature_selection(pathInitExp=doe_paths['output_results'],
                                                  savepath=path_dic['curr_results'],
                                                  num_features=8)
    # ##GET BOUNDS OF RELEVANT FEATURES ONLY
    pbounds, fixed = bounds_select_features(bounds_path=doe_paths['L12_BOUNDS'],
                                            feature_list=feature_list)
    #################################
    ## BAYESIAN OPTIMISATION
    ################################
    optimizer = BayesianOptimization(f=None, pbounds=pbounds, random_state=1)
    utility = AcquisitionUtilities(aq_type="UCB", kappa=2.5, xi=0)
    # ##CHECK FOR EXISTING DATA
    odb_list = [f for f in os.listdir(path_dic['curr_results']) if '.odb' in f]
    if odb_list:
        # ##GET EXISTING OUTPUT FILE
        path_to_output = [os.path.join(path_dic['curr_results'], f) for f in os.listdir(path_dic['curr_results'])
                          if 'OUTPUTS_' in f][0]
        # ##CREATE DF FROM OUTPUT FILE
        init_exp_df = pd.read_csv(path_to_output)
        i_fea = int(init_exp_df['JOB_NUM'].iloc[-1])
        n_additional_exp = (max_simulations - i_fea)
        # ##PATH TO NEW OUTPUT FILE
        path_dic['output_results'] = os.path.join(path_dic['curr_results'], 'OUTPUTS_' + today + '.csv')
    else:
        # ##CREATE NEW OUTPUT FILE AND ADD FILE PATH TO PATH DICTIONARY
        path_dic['output_results'] = os.path.join(path_dic['curr_results'], 'OUTPUTS_' + today + '.csv')
        init_exp_df = pd.read_csv(doe_paths['output_results'])
        # # ##MAX NUM OF EXPERIMENTS
        i_fea = int(init_exp_df['JOB_NUM'].iloc[-1])
        n_additional_exp = (max_simulations - i_fea)
    # ##REGISTER EXISTING DATA FOR OPTIMIZER WITH BAYES DIC
    optimizer, bayes_dic = reg_features_bo(df=init_exp_df,
                                           feature_list=feature_list,
                                           optimizer=optimizer)
    # ##RUN A TERMINATION CHECK (ALREADY REACHED TARGET)
    terminate, bayes_dic, utility = termination_check(i_fea, bayes_dic, utility)
    if (terminate == True) or (i == (n_additional_exp - 1)):
        print('%s has already been optimised with a minimum MAPE of %s %%'
              %(material, round(init_exp_df['MAPE'].sort_values(ascending=True).iloc[0], 2)))
        continue
    headers = ['JOB_NUM', 'Q1', 'Q2', 'Q3', 'EN', 'SN', 'FN', 'F',
               'SLOPE', 'MAPE', 'ROC_BEGIN', 'ROC_THREE', 'KAPPA', 'SIM_TIME']
    # ##RUN ADDITIONAL EXPERIMENTS AS NEEDED
    for i in range(n_additional_exp):
        i_fea = i_fea + 1
        stime = time.time()
        # ##NEXT POINT RETURNS A DICTIONARY OF VALUES
        next_point = optimizer.suggest(utility)
        # print('Optimising the next points took %s seconds' %(time.time() - stime))
        # ##MERGE NEXT POINT WITH THE MAT_GEOM_DIC
        gtn_dic = merge_dicts(next_point, fixed)
        aba_dic = merge_dicts(doe_mat_dic, gtn_dic)
        # ##EXPORT DICTIONARY TO FILE FOR ABAQUS
        json_filename = write_json_file(aba_dic,
                                        path_dic['curr_results'],
                                        'JOB' + str(i_fea) + '_JSON.txt')
        mape, etime, path_dic = FEA_Function(i_fea, json_filename, **path_dic)
        # ##CLEANUP RESULTS DIRECTORY
        delete_unwanted(path_dic['curr_results'])
        # ##RUN OPTIMISER
        optimizer.register(params=next_point, target=mape)
        # ##MERGE CURRENT ITERATION DATA FOR STORAGE INTO DICTIONARY
        store_dic = merge_dicts({'JOB_NUM': i_fea, 'MAPE': mape, 'KAPPA':utility.kappa, 'SIM_TIME': etime}, gtn_dic)
        # ##SAVE CURR ITERATION DATA IN BAYES DIC
        for ind, h in enumerate(headers):
            try:
                bayes_dic[h].append(store_dic[h])
            except KeyError:
                bayes_dic[h].append(np.nan)
        # ##CALCULATE RATE OF CHANGE
        bayes_dic, path_dic = rate_of_change(i, headers, today, bayes_dic, **path_dic)
        # ##run termination check
        terminate, bayes_dic, utility = termination_check(i_fea, bayes_dic, utility)
        # ##EXIT EARLY
        if (terminate == True) or (i == (n_additional_exp - 1)):
            # ##PLOT DATA
            plot_mape_v_sim_num(bayes_dic, **path_dic)
            plot_mape_v_sim_time(bayes_dic, **path_dic)
            best_and_worst(bayes_dic, **path_dic)
            print(f"The final fit value : {optimizer.max['target']}, "
                  f"for GTN parameters of: {optimizer.max['params']}  ")
            print(f"The final bounds are : {optimizer.bounds}")
            print(f"The explored parameters are: {optimizer.space.params}, "
                  f"and the corresponding targets are: {optimizer.space.target} ")
            break
        plot_mape_v_sim_num(bayes_dic, **path_dic)
        plot_mape_v_sim_time(bayes_dic, **path_dic)
        best_and_worst(bayes_dic, **path_dic)


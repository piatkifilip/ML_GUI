import os
import pandas as pd
import collections
from datetime import date
from initial_experiments import initialise
from B_SCR.general_functions import new_dir_add_dic, write_json_file, load_json_file, write_text_file, merge_dicts
from B_SCR.material_properties import convert_stress_strain, aoc_calc_slope, second_derivative_strain, aoc_plastic_prop
from B_SCR.csv_functions import init_data_storage
from B_SCR.Continious_Bayesian_Optimisation import BayesianOptimization
from B_SCR.Acquisition_utilies import AcquisitionUtilities

""" USE TAGUCHI ORTHOGONAL ARRAYS TO DEFINE INITIAL EXPERIMENT FIELD"""

# ##GET TODAYS DATE
today = date.today().strftime("%Y%m%d")
# ##CREATE DICTIONARY OF PATHS TO RELEVANT DIRECTORIES AND FILES
path_dic = {'cwd': os.getcwd(),
            'A_RAW_DATA': os.path.join(os.getcwd(), '../A_RAW_DATA'),
            'project_dir': os.path.join(os.getcwd(), '../'),
            'build': os.path.join(os.getcwd(), '../B_SCR/aba_build.py'),
            'postp': os.path.join(os.getcwd(), '../B_SCR/aba_pp.py')}
# ##CREATE RESULTS SUBDIRECTORY
path_dic = new_dir_add_dic(dic=path_dic,
                           key='results',
                           path=path_dic['cwd'],
                           dir_name='results',
                           exist_ok=True)
# ##LIST ALL FILES IN OUR RAW DATA FOLDER (PROVIDE MATERIAL NAMES)
material_list = os.listdir(path_dic['A_RAW_DATA'])
# ##DICTIONARY HOLDING GEOMETRICAL DATA
geom_dic = {'GAUGE_LENGTH': 25.,
            'GAUGE_DIAMETER': 4.,
            'CONN_DIAMETER': 5.,
            'SPECIMEN_LENGTH': 72.,
            'ROUND_RADIUS': 3.,
            'THREADED_LENGTH': 15}

for i, material in enumerate(material_list):
    material = material[:-4]
    print('MATERIAL: %s' %(material))
    # ##CREATE MATERIALS SUBDIRECTORY
    path_dic = new_dir_add_dic(dic=path_dic,
                               key='curr_results',
                               path=path_dic['results'],
                               dir_name=material,
                               exist_ok=True)
    # ##CHECK IF FEA EXISTS
    odb_list = [f for f in os.listdir(path_dic['curr_results']) if '.odb' in f]
    if len(odb_list) == 12:
        path_dic = load_json_file(os.path.join(path_dic['curr_results'], 'PATH_DIC.txt'))
    else:
        ###############################
        # ##CONDUCT MATERIAL ASSESSMENT
        ###############################
        path_dic['exp_fvd'] = os.path.join(path_dic['A_RAW_DATA'], material_list[i])
        # ##READ IN THE MATERIAL
        fvd = pd.read_csv(path_dic['exp_fvd'], header=[0, 1])
        # ##MATERIAL PROPERTIES CALCULATIONS
        # ##CALCULATE TRUE STRESS AND TRUE STRAIN FROM LOAD DISPLACEMENT
        true_strain, true_stress, max_disp, force, disp = convert_stress_strain(path_dic['exp_fvd'],
                                                                                geom_dic['GAUGE_LENGTH'],
                                                                                geom_dic['GAUGE_DIAMETER'])
        # ##CALCULATE THE SLOPE OF THE CURVES
        min_slope, max_slope = aoc_calc_slope(true_strain,
                                              true_stress)
        # ## CALCULATE SECOND DERIVATIVE OF STRAIN (RETURN INTERPOLATED STRESS/STRAIN VALUES)
        yield_stress, modulus, true_strain, true_stress = second_derivative_strain(true_strain,
                                                                                   true_stress,
                                                                                   **path_dic)
        # ##CALCULATE PLASTIC STRAIN VERSUS TRUE STRESS AND UTS POINT
        plastic_data, uts_point = aoc_plastic_prop(true_strain,
                                                   true_stress,
                                                   yield_stress,
                                                   modulus)
        ###############################
        # ##SAVE RESULTS MATERIAL ASSESSMENT
        ###############################
        # ##WRITE PLASTIC DATA (TO UTS) TO FILE FOR ABAQUS
        df = pd.DataFrame(data=plastic_data,
                          columns=['TRUE_STRESS', 'PLASTIC_STRAIN'])
        # ## UPDATE PATH DIC TO HOLD FILE LOCATION
        path_dic['plastic_properties'] = os.path.join(path_dic['curr_results'],
                                                      'ABAQUS_PLASTIC_PROPERTIES.csv')
        df.to_csv(path_dic['plastic_properties'], header=True, index=False)
        # ##CREATE DICTIONARY OF MATERIAL PROPERTIES INFORMATION
        mat_dic = {'MAX_DISPLACEMENT': max_disp,
                   'YIELD_STRESS': yield_stress,
                   'MODULUS': modulus,
                   'UTS_STRAIN': uts_point[1],
                   'UTS_STRESS': uts_point[0]}
        # ##BOTH GEOM DIC AND MATERIAL PROPS NEED TO BE PASSED TO ABAQUS
        # ##MERGE THESE DICTIONARYS INTO ONE ENTITY
        mat_geom_dic = merge_dicts(geom_dic, mat_dic)
        # ##WRITE DIC TO FILE
        write_json_file(mat_geom_dic, path_dic['curr_results'], 'MAT_DIC.txt')
        # ##SAVE PATH TO FILE
        path_dic['MAT_DIC'] = os.path.join(path_dic['curr_results'], 'MAT_DIC.txt')
        ###############################
        # ##CONDUCT TAGUCHI ARRAY
        ###############################
        # ##HERE WE HAVE 8 VARIABLES AND 2 LEVELS SO OUR TEST MATRIX IS: 2**8=256
        var_dic = {'Q1': (0.9, 1.6),
                   'Q2': (0.9, 1.1),
                   'Q3': (0.9 ** 2, 1.6 ** 2),
                   'EN': (0.25, 0.4),
                   'SN': (0.1, 0.2),
                   'FN': (0.03, 0.09),
                   'F': (0.0013, 0.0015),
                   'SLOPE': (0, max_slope)}
        # ##CALCULATE THE TAGUCHI ARRAY FOR L12
        tag_arr = pd.read_csv(os.path.join(path_dic['cwd'], 'L12.csv'))
        # ##BLANK DF FOR FILLING VALUES
        tag_df = pd.DataFrame(columns=var_dic.keys())
        # ##ITERATE DICTIONARY AND FILL
        for k in var_dic.keys():
            tag_df[k] = tag_arr[k].map({1: var_dic[k][0],
                                        2: var_dic[k][1]})
        # ##SAVE TAGUCHI DF
        tag_df.to_csv(os.path.join(path_dic['curr_results'], 'L12.csv'))
        # ##WRITE THE BOUNDS TO JSON FILE
        write_json_file(var_dic, path_dic['curr_results'], 'L12_BOUNDS.txt')
        # ##ADD PATH TO BOUNDS FILE TO PATH DICTIONARY
        path_dic['L12_BOUNDS'] = os.path.join(path_dic['curr_results'], 'L12_BOUNDS.txt')
        # ##UPDATE PATH DIC TO HOLD FILENAMES
        path_dic['L12'] = os.path.join(path_dic['curr_results'], 'L12.csv')
        # ##WRITE PATHS TO FILE
        write_json_file(path_dic, path_dic['curr_results'], 'PATH_DIC.txt')
        path_dic['output_results'] = os.path.join(path_dic['curr_results'], 'OUTPUTS_' + today + '.csv')
        # ##HEADERS FOR CSV OUTPUT FILE
        headers = ['JOB_NUM', 'Q1', 'Q2', 'Q3', 'EN', 'SN', 'FN', 'F',
                   'SLOPE', 'MAPE', 'ROC_BEGIN', 'ROC_THREE', 'KAPPA', 'SIM_TIME']
        # ## DICTIONARY TO HOLD VALUES + INIT DATA STORAGE
        bayes_dic = collections.defaultdict(list)
        init_data_storage(path_dic['output_results'], headers)

        # ##CREATE COUNTER FOR JOB NUMBERING SYSTEM
        i_fea = 0
        # optimizer = BayesianOptimization(f=None, pbounds=pbounds, random_state=1,
        # 								 bounds_transformer=SequentialDomainReductionTransformer())
        optimizer = BayesianOptimization(f=None, pbounds=var_dic, random_state=1)
        utility = AcquisitionUtilities(aq_type="UCB", kappa=2.5, xi=0)
        # ##CHECK IF FEA ALREADY DONE
        odb_list = [f for f in os.listdir(path_dic['curr_results']) if '.odb' in f]
        # ##CALL INITIAL EXPERIMENTS RETURN UPDATED VALUE FOR IFEA
        i_fea, bayes_dic = initialise(tag_df,
                                      i_fea,
                                      mat_geom_dic,
                                      optimizer,
                                      utility,
                                      headers,
                                      bayes_dic,
                                      **path_dic)
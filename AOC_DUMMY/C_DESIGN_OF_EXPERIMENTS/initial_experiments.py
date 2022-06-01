import numpy as np
import itertools as it
from collections import OrderedDict
import json
from B_SCR.abaqus_functions import *
from B_SCR.csv_functions import store_data
from B_SCR.clean_fea_dir import delete_unwanted
from B_SCR.general_functions import product_dic, merge_dicts, write_json_file


def initialise(points, i_fea, mat_geom_dic, optimizer, utility, headers, bayes_dic, **path_dic):
    """ FUNCTION TO RUN INITIAL EXPERIMENTS FOR BAYESIAN OPTIMISER TO EXPLORE SPACE.
	 NOTE: WE DO NOT CALCULATE RATE OF CHANGE OR ASSESS TERMINATION AT THIS STAGE
	 store_dic: current iterations parameters (geometrical, material, gtn etc)
	 bayes_dic: cumulative iteration parameters for each job
	 """
    # ##ITERATE ROWS OF THE INIT EXP DF
    for i, rw in points.iterrows():
        i_fea += 1
        rw_dic = rw.to_dict()
        aba_dic = merge_dicts(mat_geom_dic, rw_dic)
        json_filename = write_json_file(dic=aba_dic,
                                        pth=path_dic['curr_results'],
                                        filename='JOB' + str(i_fea) + '_JSON.txt')
        mape, etime, path_dic = FEA_Function(i_fea, json_filename, **path_dic)
        # ##CLEANUP RESULTS DIRECTORY
        delete_unwanted(path_dic['curr_results'])
        # ##THE OPTIMIZER REQUIRES SORTED VALUES (KEYS IN ALPHABETICAL ORDER)
        optimizer.register(params=[rw_dic[k] for k in sorted(rw_dic.keys())], target=mape)
        # ##MERGE DATA FOR OUTPUTS STORAGE INTO DICTIONARY
        store_dic = merge_dicts({'JOB_NUM': i_fea, 'MAPE': mape, 'KAPPA':utility.kappa, 'SIM_TIME': etime}, rw_dic)
        # ##STORE DATA IN OUTPUT CSV
        store_data(path_dic['output_results'], headers, store_dic)
        # ##SAVE DATA IN BAYES DIC
        for ind, h in enumerate(headers):
            try:
                bayes_dic[h].append(store_dic[h])
            except KeyError:
                bayes_dic[h].append(np.nan)
    return i_fea, bayes_dic

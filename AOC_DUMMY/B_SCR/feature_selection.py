import os
import pandas as pd
import collections
from B_SCR.plots import heatmap
from sklearn.feature_selection import f_regression, SelectKBest
from B_SCR.general_functions import write_text_file


def feature_selection(pathInitExp=None, savepath=None, num_features=None):
    """ HERE WE USE STATISTICS TO IDENTIFY FEATURES OF INTEREST.
    INPUT IS PATH TO FILE AND NUMBER OF FEATURES TO INVESTIGATE.
    RETURN DF REPRESENTING INTIITAL EXPERIMENT OUTPUT AND LIST OF FEATURE NAMES"""
    results = pd.read_csv(pathInitExp)
    # ##GET TARGET AND PARAMS
    target = results['MAPE']
    params = results.loc[:, ['Q1', 'Q2', 'Q3', 'EN', 'SN', 'FN', 'F', 'SLOPE']]
    heat_res = pd.concat([params, target], axis=1)
    # ##HEATMAP PEARSON CORRELATION BETWEEN TARGET AND PARAMETERS.
    heatmap(heat_res,
            savepath=savepath,
            savename='HEATMAP')
    # ##FIND THE MOST IMPORTANT PARAMETERS
    model = SelectKBest(score_func=f_regression, k=num_features)
    data = model.fit_transform(params, target)
    feature_names = model.get_feature_names_out()
    write_text_file(data=feature_names.tolist(),
                    root=savepath,
                    filename='SELECT_KBEST.txt')
    return results, feature_names

def reg_features_bo(df=None, feature_list=None, optimizer=None):
    """ HERE WE REGISTER THE INITIAL EXPERIMENTS - SPECIFICALLY THE FEATURES OF INTEREST -
    TO THE BO OPTIMISER."""
    # ##CREATE DICTIONARY FROM DF
    bayes_dic = df.to_dict('list')
    params = df.copy()[feature_list]
    mape = df['MAPE']
    for i, rw in params.iterrows():
        sort_keys = sorted(params.columns)
        optimizer.register(params=[rw[k] for k in sort_keys], target=mape[i])
    return optimizer, bayes_dic
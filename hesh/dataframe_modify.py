# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:18:41 2021

@author: Ovindu Wijethunge
"""
import pandas as pd
import numpy as np
import scipy.stats as stat
from scipy.special import boxcox1p

def data_modification(df):
    dfs = df
    dfs = dfs.drop('cid',axis=1)
    dfs['sim_content'] = np.where(dfs['sim_content']>0.5,0.5,dfs['sim_content'])
    dfs['sim_comment'] = np.where(dfs['sim_comment']>0.54,0.54,dfs['sim_comment'])
    dfs['word_count'] = np.where(dfs['word_count']>42,42,dfs['word_count'])
    dfs['length_of_comment'] = np.where(dfs['length_of_comment']>165,165,dfs['length_of_comment'])
    dfs['no_of_sentences'] = np.where(dfs['no_of_sentences']>3,3,dfs['no_of_sentences'])
    dfs['num_of_punctuations'] = np.where(dfs['num_of_punctuations']>6,6,dfs['num_of_punctuations'])
    dfs['post_coment_gap'] = np.where(dfs['post_coment_gap']>584487.0,584487.0,dfs['post_coment_gap'])
    
    dfs['sim_content']=boxcox1p(dfs['sim_content'],0.25)
    dfs['sim_comment']=boxcox1p(dfs['sim_comment'],0.25)
    dfs['word_count'],_=stat.boxcox(dfs['word_count'])
    dfs['length_of_comment']=np.log(dfs['length_of_comment'])
    dfs['post_coment_gap'],_=stat.boxcox(dfs['post_coment_gap'])
    
    
    
    
    
    #from scipy.special import boxcox1p
    #scipy.special.boxcox1p(x, lmbda)
    
    #new_df = pd.get_dummies(dfs,drop_first=True)
    #print(new_df.columns)
    return dfs
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:55:12 2020

@author: Acer
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
# from num2words import num2words

import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math

import csv
import re
from datetime import datetime

import openpyxl





def vectorize(processed_text):
    N = len(processed_text) # get the length of list in list 
    
    

    DF = {} # dictionary

    for i in range(N):
        tokens = processed_text[i]
        for w in tokens:
            try:
                
                DF[w].add(i)
            except:
                
                DF[w] = {i}

 
# =============================================================================
#         for w in tokens:
#             try:
#                 
#                 DF[w].add(i)
#             except:
#                 
#                 DF[w] = {i}
# =============================================================================
            
    for i in DF:
        
        DF[i] = len(DF[i])


    total_vocab_size = len(DF) # just for show
    total_vocab = [x for x in DF]


    def doc_freq(word):
        
        c = 0
        try:
            
            c = DF[word]
        except:
            
            pass
        return c


    tf_idf = {}
    vectors_list = []
    tf_list =[] # just for show

    for i in range(N):

        tokens = processed_text[i]
   
        counter = Counter(tokens)
        words_count = len(tokens)
        Q = np.zeros((len(total_vocab))) # create an array with total bigrams vocabulary length
        j = 0
        rep_word = 0
        for token in np.unique(tokens):

            for z in range(0, len(total_vocab)):
                if token == total_vocab[z]:# find the word position in vocabulary for place the value at right place in vector
                    tf = counter[token] / words_count
                    df = doc_freq(token)
                    idf = 1 + (np.log((N) / (df)))
                    Q[z] = tf * idf
                    if tf > rep_word: # find the maximum term frequency in a comment
                       
                        rep_word = tf
                    break

        vectors_list.append(Q)
        tf_list.append(rep_word) # currently not use previously use for find the frequency in a comment
    return vectors_list

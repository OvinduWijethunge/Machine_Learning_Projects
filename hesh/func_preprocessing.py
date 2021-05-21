# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 22:54:25 2020

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

def remove_punctuation(data):
        
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
                
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data


def stop_word(x):
    
        
    val = " "
    word_list = ["මම","මා","මාත්","මට","මගේ","මං","මන්",
                                     "ඔබ","ඔයා","ඔබට","ඔයාට","ඔබගේ","ඔයාගේ","ඔබත්","ඔයත්",
                                    "ඔහු","එයා","ඔහුගේ","එයාගේ","ඔහුට","එයාට","ඔහුත්","එයත්",
                                    "ඇය","ඇයගේ","ඇයට","ඇයත්",
                                    "ඔවුන්","ඔවුන්ගේ","ඔවුන්ට","ඔවුනුත්",
                                    "අපි","අපගේ","අපිට","අපිත්","අප",
                                    " උඹ","උඹේ","උඹෙ","උඹගෙ","උඹගේ","උඹත්","උඹලා","නුඹ","නුඹෙ","නුඹේ","නුඹගෙ","නුඹගේ","නුඹට","නුඹත්","නුඹලා","නුඹල",
                                     "තෝ","තො","තොගෙ","තොගේ","තොපි","තොපිට","තොප","තොපේ","තොපෙ","තොපට","තොපිලා","තොපලා",
                                     "  උ","උට","උගෙ","උගේ","උත්",
                                     " එක","සදහා","වෙනුවෙන්","හට","සිට","දක්වා",
                                     "මොකක්ද","මොකද","ඇයි","කොහෙද","කොහේද","කවුද","කාගෙද","කීයටද","කොච්චර","කාටද","මුු"
                     ]
    
    
    
    for i in range(0,len(word_list)):
        
        if x == word_list[i]:
            val = x
           
            break
            
    return val


def remove_stopwords(text):
    
    tokenized_text = word_tokenize(str(text))
    new_text = " "    
    for word in tokenized_text:

        if word == stop_word(word):
            
            continue
        else:
            
            new_text += word+" "
    
    return new_text

def preprocess(data):
  
    data1 = remove_punctuation(data)
    data2 = remove_stopwords(data1)
    return data2

# =============================================================================
# def remove_functuations(data):
#     data1 = remove_punctuation(data)
#     return data1
# =============================================================================

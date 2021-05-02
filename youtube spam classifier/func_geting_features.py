# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:53:10 2020

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



def no_sentences(set): 
    splitter = re.split(r'[!.?]+', set)
    if len(splitter) ==1:
        
        return len(splitter)
    else:
            
        return len(splitter)-1
    
def com_length(num):
    return len(num)    
    
def no_punctuations(num):
    
    count = 0
    Sentence = num
    for i in Sentence:
        #print(num)
        if i in string.punctuation and i !=".":
            
            count = count +1
            #print(count)
        
# =============================================================================
#     split_sentences = re.split(r'[!.?]+', num)
#     if len(split_sentences)== 1:
#            
#         return count/(len(split_sentences))
#     else:
#         return count/(len(split_sentences)-1)
# =============================================================================
            
    return count    

#st ="hello!! bro how ar...e you ?"
#x = no_punctuations(st)
#print(x)


    

def stop_word(x):
        
    val = " "
    word_list = ["මම","මා","මාත්","මට","මගේ","මං","මන්","මගෙන්",
                                     "ඔබ","ඔයා","ඔබට","ඔයාට","ඔබගේ","ඔයාගේ","ඔබත්","ඔයත්",
                                    "ඔහු","එයා","ඔහුගේ","එයාගේ","ඔහුට","එයාට","ඔහුත්","එයත්",
                                    "ඇය","ඇයගේ","ඇයට","ඇයත්",
                                    "ඔවුන්","ඔවුන්ගේ","ඔවුන්ට","ඔවුනුත්",
                                    "අපි","අපගේ","අපිට","අපිත්","අප",
                                    " උඹ","උඹේ","උඹෙ","උඹගෙ","උඹගේ","උඹත්","උඹලා","නුඹ","නුඹෙ","නුඹේ","නුඹගෙ","නුඹගේ","නුඹට","නුඹත්","නුඹලා","නුඹල",
                                     "තෝ","තො","තොගෙ","තොගේ","තොපි","තොපිට","තොප","තොපේ","තොපෙ","තොපට","තොපිලා","තොපලා",
                                     "  උ","උට","උගෙ","උගේ","උත්",
                                     " එක","සදහා","වෙනුවෙන්","හට","සිට","දක්වා",
                                     "මොකක්ද","මොකද","ඇයි","කොහෙද","කොහේද","කවුද","කාගෙද","කීයටද","කොච්චර","කාටද","අයියා", "අයියේ", "අයියෙ"
                     ]
        
    for i in range(0,len(word_list)):
        if x == word_list[i]:
            val = x
          
            break
            
    return val

def count_stop_word(text):
    count = 0
    words_count = len(text) # here text is already tokenized
        
    for word in text:
        
        if word == stop_word(word):
            
            count = count +1
           
                
    if words_count == 0:
        words_count = 1
    ratio = count/words_count 
    
    return ratio  




def check_word(word):
        
    
    word_list = ["සස්ක්‍රයිබ්","සබ්","ලින්ක්","චැනල්","බලන්න","වෙබ්","ගොඩ","සප්","සපෝට්","උදව්වක්","උදවු","සහයෝගය","සහයෝගයක්",
                                    "නාලිකාවෙන්","SUBSCRIBE","Subscribe","subscribe","සබ්ස්ක්‍රරයිබ්ලා","මේ පැත්තට","සපෝට්",
                                     " බලන්නකෝ","නිෂ්පාදනය","සබ්ස්ක්‍රයිබ්",
                                    "කොල්ලනේ","ෆිල්ම්","ෆිල්ම්ස්","වට්ටමක්","ටිකට්","කූපන්","බටනය","මෙන්න","විදිහ","දැනගන්න","එන්න","ආදායම්","ඩෙබිට්","ක්රෙඩිට්",
                                   "බටන්","රෙජිස්ටර්","කරන්නකො","කැමතිද","සෙට්","එකතුව","බොත්තම","පැත්තටත්","පැත්තට","පැත්තෙ","ආරාධනා","ප්‍රමෝට්","බැලුවොත්",
                                   "උපයන්න","විකිණීමට","ඔබන්න","ක්ලික්","නොමිලේ","විස්තරය"
                                  ,'කරන්න','ගන්න','සල්ලි','ඔයාට','එකට','අය','කරලා','වෙන්න','පුලුවන්','පුලුවන්','නම්','link','website','site',
                                  'එකතු','register','සයිට්','වෙබ්','මුදල්','රෙජිස්ටර්','චැනල්','නොමිලේ','පහල','ලියාපදිංචි','click','join','කරගන්න','Register',
                                  'ආදායමක්','ලාභයක්','free','යාලුවනේ','මුදලක්','ලාභය','කට්ටිය','පහත','Profit','ලැබෙනව','පහලින්','share','ඉක්මනින්','ජය','සප්',
                                  'යටින්','පුංචි','අලෙවි','ගෙවනවා','ඔයාගෙම','ආදායම්','වෙබ්සයිට්','ලාභයම','ආදායම','උපයන්න','invite','කලොත්','යට','අමතර','සේවා',
                                  'පැත්තෙ','sale','Credit','ආයෝජනය','බට්න්','හම්බෙනවා','download','විකුණන','නොමිලේම','ගිනුමට','Click','ඔබන්න','එකතුවෙන්න',
                                  'සහයෝගය','විනාඩියක්','කියවන්න','හම්බෙනවා','ශෙයා','ජයවේවා','credit','උදවු','වාසිය','වාසියක්','ලාභයෙන්'  ]             
        
    if word in word_list:
        
        return word


def check_black_words_list(text):
        
    val = 0
        
    words_count = len(text)   
    for word in text:
        if word == check_word(word):
            val += 1
   
    ratio = val/words_count
    
    return ratio             
        
   


def duplicate_words(sentence):
    token = sentence
    num_words = len(token)
   # print("number of words ??????????????????????????????????????????????????? ",num_words)
    uniq_words = len(np.unique(token))
    ratio = 1 - (uniq_words/num_words)
    return ratio


def find_mail_site_pnumber(text):
    condition = 0 # by default false 
    x = re.findall("\d+[10]|\d+[10]|@|https|http", text)
    #print(x)
    
    if len(x)!= 0:
            
        condition = 1
    return condition 

def calculate_content_comment_similerity(vector1,vector2):
    product1 = sum(a * a for a in vector1) ** 0.5
    product2 = sum(b * b for b in vector2) ** 0.5
    dot_product = sum(a * b for a, b in zip(vector1, vector2)) 
    distance = (product1 * product2)
    if (distance  == 0).all():
            distance  = 1
            
    cos_simillerity = dot_product / distance
    return cos_simillerity
    

    
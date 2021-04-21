# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:48:37 2020

@author: Acer
"""
from nltk.tokenize import word_tokenize
from func_vector_create import vectorize
from func_preprocessing import preprocess

def find_duplicate_comments(main_list, val):
    
    sub_list = main_list[val]
    channel_id = sub_list[4]
    comment = sub_list[3]
    maxv = 0
    #count = 0
    ct = 0
    for rowd in main_list:
        #print("row is ",rowd)sub_list[6] == rowd[6]
               
               #print(sub_list[6])
               if val == ct: 
                    
                   #print("count ",count)
                   #print("hell")
                   ct +=1
                   continue
               else:
                   
                   ct +=1 
                   if channel_id == rowd[4]:
                       
                       #print("my name cdncnj")
                       row_comment = rowd[3]
                        
                       dataset = [comment , row_comment]
                       print("dta set is",dataset)
                       Ne = len(dataset) 
                        
                       processed_text = []
    
                       for text in dataset[:Ne]:
                        
                           processed_text.append(word_tokenize(str(preprocess(text))))#this is a list in list which have tokenize strings duplicate words also here
                    
                       vectors_list = vectorize(processed_text)
                       

      
                       vec1 = vectors_list[0]
                       vec2 = vectors_list[1]
                       dot = sum(a*b for a, b in zip(vec1,vec2))
                       norm_a = sum(a*a for a in vec1) ** 0.5
                       norm_b = sum(b*b for b in vec2) ** 0.5
                            
                            
                       cos_sims = dot / (norm_a*norm_b)
                       #print("cos val ",cos_sims)
                       if maxv <= cos_sims:
                            
                           maxv = cos_sims
    
                        #print(cos_sims)

               #count = count + 1                        
    return maxv    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:04:15 2021

@author: Acer
"""

import re
from func_geting_features import check_black_words_list

#list_val = []
def link_mob_mail_length_blckword(text):
   # print('test is ',text)
    st = ' '.join(text)
  
    list_val = []
    com_length = len(st)
    list_val.append(com_length)
   # print(com_length)
    word_count = len(text)
   # print(word_count)
    list_val.append(word_count)

    isLink = 0
    isYoutubeLink = 0
    x = re.findall("\ https|http", st)
    if len(x)> 0:
        isLink = 1
        
        for i in text:
            
            y = re.search("youtu",i)
            if y is not None:
                
                isYoutubeLink = 1
                break
    #print("link is ",isLink,isYoutubeLink),
    list_val.append(isLink)
    list_val.append(isYoutubeLink)


    isTnumber = 0
    x = re.findall("\d{10}|\d{9}", st)
    if len(x) > 0:
        number = x[0]
        isTnumber = 1
        #print(x[0])
    list_val.append(isTnumber) 
    
    #print("phone number is ",isTnumber)  
    
    
# =============================================================================
#     isMail = 0
#     x = re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', st)
#     #print(x)
# 
#     if len(x)!= 0:
#         
#         isMail = 1
#     list_val.append(isMail)    
# =============================================================================
        
   # print("mail is ",isMail) 


    black_words_count = check_black_words_list(text)
    list_val.append(black_words_count)
    #print("b countt ",black_words_count)    
    #print(list_val) 
    return list_val 
    
    
#ss = ['0778405011','මේ වගේ ලස්සනම ලස්සන සින්දු අහන්න අපිත් එක්ක එකතු වෙන්න https://youtu.be/zuXy30wsY2E','0778405011','ැනල්','අපි','බටන්','කට']
#st = "https://m.youtube.com/channel/UCOyzo3-s5keZkVVObYUugyg යාළුවනේ චැනල් 0778405011 අපි බටන්  එකට oum@gmail.com එක් වෙමු youtube  ජිවිතයෙ පලමු sUBSCRIBE 1000 ගන්න එක තමා පලමු අබියෝගය මෙකෙන් අපි එකතු වෙලා ජය ගමු අපි sUBSCRIBE  Share කරගමු එතකොට එ අරමුනට යන්න පුලුවන් එතින් ඔයලා මගෙ channel එක sUBSCRIBE  karala මට comment  එකක් දන්න එතකොට මමත් ඔයලගෙ channel sUBSCRIBE  කරන්නම් අපි එක් වෙමු thanks"
#link_mob_mail_length_blckword(ss)    





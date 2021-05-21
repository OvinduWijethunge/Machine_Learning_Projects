import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

from youtubeData_v3 import download_comments_and_content
from comments_downlod_to_hate_module import get_ham_comments

from sklearn.preprocessing import StandardScaler
import scipy.stats as stat

from dataframe_modify import data_modification


app = Flask(__name__)
model = pickle.load(open('gboostv4.pkl', 'rb'))
#scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    id = [x for x in request.form.values()]
    val = id[0] 
    str_val = str(val)
    #str_val = 'eXllTof3hKI'
    download_comments_and_content(str_val) # gmsUIoMSgsY

    df = pd.read_csv('data.csv')
    data_frame = data_modification(df)
    ldd= data_frame.columns
    
    
    
    
    
    prediction = model.predict(data_frame.values.tolist())
    print(prediction)
    
    prediction_series = pd.Series(prediction)
    
    df1= pd.concat([df,prediction_series], axis=1)
    df1 = df1.rename(columns={0: 'is_spam'})
    id_group = df1.groupby(['is_spam'])
    spam_group = id_group.get_group(1)
    ham_group = id_group.get_group(0)
    spam_list = spam_group['cid'].tolist()
    ham_list = ham_group['cid'].tolist()
    
    total_comments = len(prediction_series)
    spam_commnets = len(spam_list)
    spam_presentage = (spam_commnets/total_comments)*100
    
    
    
    # make a dataframe without spam commnets
    df_comments = pd.read_excel('comments.xlsx')
    index_names = (df_comments[ df_comments['comment_id'].isin(spam_list) ].index).tolist()
    df_ham_comments = df_comments.drop(index_names) # legitimate comments dataframe for next step.....
    
    
    
    get_ham_comments(str_val,spam_list)
    
    return render_template('index.html', prediction_text="spam comments presentage of this video is {:.2f}".format(spam_presentage)+chr(37))
   



if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
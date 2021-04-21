
# first neural network with keras tutorial
import numpy as np
from numpy import loadtxt

from imblearn.combine import SMOTETomek
from imblearn.under_sampling import NearMiss
import pandas as pd 
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
# load the dataset
data = pd.read_csv('newData.csv') 
# split into input (X) and output (y) variables
corr_matrix = data.corr()
price_corr = corr_matrix['classifier_val']
print(price_corr)
price_corr.iloc[price_corr.abs().argsort()]




X = data[data.columns[1:-1]] 
y = data[data.columns[-1]]
smk = SMOTETomek(random_state=42)
X_res,y_res=smk.fit_sample(X,y) 


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.30)
# define the keras model


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


input_dim = X_train.shape[1]



model = Sequential()
model.add(Dense(12, input_dim=input_dim, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X_train, y_train, epochs=100, batch_size=50)
# evaluate the keras model


y_pred = model.predict(X_test)
li = []
for i in y_pred:
    if i <0.5:
        li.append(0)
    else:
        li.append(1)
#print(li)        
print(type(y_pred))
#_, accuracy = model.evaluate(X, y)
#print('neural network Accuracy: %.2f' % (accuracy*100))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, li))
print(classification_report(y_test,li))






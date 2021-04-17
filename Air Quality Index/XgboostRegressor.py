# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:15:10 2021

@author: Acer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
#conda install -c ananconda py-xgboost

df=pd.read_csv('Data/Real-Data/Real_Combine.csv')
df=df.dropna()
X=df.iloc[:,:-1] ## independent features
y=df.iloc[:,-1] ## dependent features

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

regressor=xgb.XGBRegressor()
regressor.fit(X_train,y_train)

print("Coefficient of determination R^2 <-- on train set: {}".format(regressor.score(X_train, y_train)))

print("Coefficient of determination R^2 <-- on train set: {}".format(regressor.score(X_test, y_test)))

from sklearn.model_selection import cross_val_score
score=cross_val_score(regressor,X,y,cv=5)
print(score.mean())

# Model Evaluation
#^^^^^^^^^^^^^^^^^^^

prediction=regressor.predict(X_test)
sns.distplot(y_test-prediction)

plt.scatter(y_test,prediction)


#Hyperparameter Tuning
#^^^^^^^^^^^^^^^^^^^^^^^

from sklearn.model_selection import RandomizedSearchCV
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
print(n_estimators)

#Randomized Search CV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
# Various learning rate parameters
learning_rate = ['0.05','0.1', '0.2','0.3','0.5','0.6']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
# max_depth.append(None)
#Subssample parameter values
subsample=[0.7,0.6,0.8]
# Minimum child weight parameters
min_child_weight=[3,4,5,6,7]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'learning_rate': learning_rate,
               'max_depth': max_depth,
               'subsample': subsample,
               'min_child_weight': min_child_weight}

print(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
regressor=xgb.XGBRegressor()


# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations
xg_random = RandomizedSearchCV(estimator = regressor, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 100, cv = 5, verbose=2, random_state=42, n_jobs = 1)

xg_random.fit(X_train,y_train)
print(xg_random.best_params_)

print(xg_random.best_score_)

predictions=xg_random.predict(X_test)


sns.distplot(y_test-predictions)

plt.scatter(y_test,predictions)

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

import pickle
# open a file, where you ant to store the data
file = open('xg_boost_regression_model.pkl', 'wb')

# dump information to that file
pickle.dump(xg_random, file)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:17:49 2022

@author: akhbh
"""

import pandas as pd

import matplotlib.pyplot as mtp
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
import numpy as nm



df=pd.read_csv('Wine.csv')
k=df.describe()
x=df.iloc[:,:13].values
y=df.iloc[:,[13]].values
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=0)

model=KNeighborsClassifier(n_neighbors=5,p=2,metric='manhattan')

model.fit(x_train,y_train)
ypred=model.predict(x_test)
model.score(x_test,y_test)


cm=confusion_matrix(y_test, ypred)
ac=accuracy_score(y_test, ypred)
cr=classification_report(y_test, ypred)





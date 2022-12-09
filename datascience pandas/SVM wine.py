# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:03:29 2022

@author: akhbh
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



df=pd.read_csv('Wine.csv')
x=df.iloc[:,:13].values
y=df.iloc[:,13].values

sc=StandardScaler()
X=sc.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=0,train_size=0.8)

model=SVC(kernel='linear')

model.fit(x_train,y_train)
ypred=model.predict(x_test)

cm=confusion_matrix(y_test, ypred)
ac=accuracy_score(y_test, ypred)
cr=classification_report(y_test, ypred)


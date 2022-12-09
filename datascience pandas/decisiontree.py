# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:25:34 2022

@author: akhbh
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

df=pd.read_csv('salaries (4).csv')

label=LabelEncoder()
model=DecisionTreeClassifier()
df['company']=label.fit_transform(df.company)
df['job']=label.fit_transform(df.job)
df['degree']=label.fit_transform(df.degree)

x=df.iloc[:,[0,1,2]]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=1)

model.fit(x_train,y_train)
y_pred=model.predict(x_test)


cm=confusion_matrix(y_test, y_pred)

ac=accuracy_score(y_test, y_pred)
cr=classification_report(y_test, y_pred)






# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:28:17 2022

@author: akhbh
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

df=pd.read_csv('Social_Network_Ads.csv')

x=df.iloc[:,2:4].values
y=df.iloc[:,4].values

sc=StandardScaler()

X=sc.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=0)
model=GaussianNB()

model.fit(x_train,y_train)

ypred=model.predict(x_test)

cm=confusion_matrix(y_test, ypred)
cr=classification_report(y_test, ypred)
ac=accuracy_score(y_test, ypred)


#model saving

import pickle
f1=open(file="naivebayesmodel.pkl",mode="bw")
pickle.dump(model,f1)
f1.close()

f2=open(file="standard_scaler.pkl",mode="bw")
pickle.dump(sc,f2)
f2.close()


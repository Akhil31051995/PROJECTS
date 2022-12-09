# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:44:03 2022

@author: akhbh
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
wine=load_wine()


dir(wine)

df=pd.DataFrame(wine['data'],columns=wine['feature_names'])

x=wine.data
y=wine.target


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=20)

model=GaussianNB()
model1=BernoulliNB()
model2=MultinomialNB()

model.fit(x_train,y_train)
y_pred=model.predict(x_test)

cm=confusion_matrix(y_test, y_pred)
ac=accuracy_score(y_test, y_pred)
cr=classification_report(y_test, y_pred)

model1.fit(x_train,y_train)
y1pred=model1.predict(x_test)
model2.fit(x_train,y_train)
y2pred=model2.predict(x_test)



cm1=confusion_matrix(y_test, y1pred)
cm2=confusion_matrix(y_test, y2pred)

ac1=accuracy_score(y_test, y1pred)
cr1=classification_report(y_test, y1pred)

ac2=accuracy_score(y_test, y2pred)
cr2=classification_report(y_test, y2pred)



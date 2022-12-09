# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 12:27:51 2022

@author: akhbh
"""

from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.model_selection import train_test_split

df=load_breast_cancer()

x=df.data
y=df.target

print(df.feature_names)
print(df.target_names)

model=KNeighborsClassifier(n_neighbors=5,p=2,metric='euclidean')
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.85,random_state=19)

model.fit(x_train,y_train)
y_pred=model.predict(x_test)


cm=confusion_matrix(y_test, y_pred)
cr=classification_report(y_test, y_pred)
ac=accuracy_score(y_test,y_pred)

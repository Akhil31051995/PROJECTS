# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:17:49 2022

@author: akhbh
"""

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

iris=datasets.load_iris()


iris.feature_names
iris.target_names
iris.target
iris.data
x=iris.data
y=iris.target
model=KNeighborsClassifier(n_neighbors=4,p=2,metric='minkowski')
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,train_size=0.8)


model.fit(x_train,y_train)


ypred=model.predict(x_test)


cm=confusion_matrix(y_test, ypred)
ac=accuracy_score(y_test, ypred)
cr=classification_report(y_test, ypred)

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:38:57 2022

@author: akhbh
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.tree import export_text
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('Social_Network_Ads.csv')

x=df.iloc[:,2:4].values
y=df.iloc[:,-1].values

sc=StandardScaler()
X=sc.fit_transform(x)

model=DecisionTreeClassifier(criterion="gini",random_state=0)
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=0)

model.fit(x_train,y_train)
y_pred=model.predict(x_test)

cm=confusion_matrix(y_test, y_pred)
ac=accuracy_score(y_test, y_pred)
cr=classification_report(y_test, y_pred)

tree=export_text(model,feature_names=['age','salary'])



#ROC---AOC curve

from sklearn.metrics import roc_curve,auc,roc_auc_score
fpr,tpr,thresh=roc_curve(y_test,y_pred)


a=auc(fpr,tpr)
plt.plot(fpr,tpr,color="green",label=("AUC value: %0.2f"%(a)))
plt.plot([0,1],[0,1],"--",color="red")
plt.xlabel("False positive rate")
plt.ylabel("True positive rate")
plt.title("ROC-AUC CURVE")
plt.legend(loc="best")
plt.show()

lrmodel=LogisticRegression()

lrmodel.fit(x_train,y_train)
pred=lrmodel.predict(x_test)

cm1=confusion_matrix(y_test, pred)
ac1=accuracy_score(y_test, pred)

cr1=classification_report(y_test, pred)


from sklearn.metrics import roc_auc_score,roc_curve,auc
fpr,tpr,thresh=roc_curve(y_test,y_pred)
a = auc(fpr,tpr)


fpr1,tpr1,thresh = roc_curve(y_test,pred)
b = auc(fpr1,tpr1)

plt.plot(fpr,tpr,color="green",label=("AUC value of Decision tree: %0.2f"%(a)))
plt.plot(fpr1,tpr1,color="blue",label=("AUC value of logistic Regression: %0.2f"%(b)))
plt.plot([0,1],[0,1],"--",color="red")
plt.xlabel("False positive rate")
plt.ylabel("True Positive rate")
plt.title("ROC-AUC Curve")
plt.legend(loc="best")
plt.show()


























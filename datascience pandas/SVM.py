# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:20:38 2022

@author: akhbh
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as mtp
import numpy as nm

df=pd.read_csv('Social_Network_Ads.csv')
x=df.iloc[:,2:4].values
y=df.iloc[:,4].values

sc=StandardScaler()
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.75,random_state=0)
xtrain=sc.fit_transform(x_train)
xtest=sc.transform(x_test)


from sklearn.svm import SVC
model=SVC(kernel='linear',random_state=0)

model.fit(xtrain,y_train)

ypred=model.predict(xtest)

cm=confusion_matrix(y_test, ypred)
ac=accuracy_score(y_test, ypred)
cr=classification_report(y_test, ypred)



#Visualizing the training set result  
from matplotlib.colors import ListedColormap  
x_set, y_set = xtest, y_test  
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(x1, x2, model.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
alpha = 0.75, cmap = ListedColormap(('purple','green' )))  
mtp.xlim(x1.min(), x1.max())  
mtp.ylim(x2.min(), x2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],c = ListedColormap(('purple', 'green'))(i), label = j)  
mtp.title('KNN')  
mtp.xlbel('y-values')  
mtp.legendabel('x-values')  
mtp.ylad()  
mtp.show()




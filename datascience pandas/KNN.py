# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:42:39 2022

@author: akhbh
"""

import pandas as pd
import numpy as nm
import matplotlib.pyplot as mtp
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

df=pd.read_csv('Social_Network_Ads.csv')
x=df.iloc[:,2:4].values
y=df.iloc[:,[4]].values

sc=StandardScaler()
X = sc.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=0)


#model selection
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=4,metric='minkowski',p=2) 
#acc=[]
#for i in range(1,11):
   
#    model=KNeighborsClassifier(n_neighbors=i,metric='minkowski',p=2) 
    
#    model.fit(x_train,y_train)
#    pred=model.predict(x_test)
#    a=accuracy_score(y_test,pred)
#    acc.append(a)

#plt.plot(range(1,11),acc)
#plt.show()
                                              

model.fit(x_train,y_train)

#predicting the test result

ypred=model.predict(x_test)

#create confusion matrix


cm=confusion_matrix(y_test, ypred)
cr=classification_report(y_test, ypred)
ac=accuracy_score(y_test,ypred)



#Visualizing the training set result  
from matplotlib.colors import ListedColormap  
xset, y_set = x_train, y_train  
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
nm_.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(x1, x2, model.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
alpha = 0.75, cmap = ListedColormap(('purple','green' )))  
mtp.xlim(x1.min(), x1.max())  
mtp.ylim(x2.min(), x2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],c = ListedColormap(('purple', 'green'))(i), label = j)  
mtp.title('KNN')  
mtp.xlbel('y-values')  
mtp.legenabel('x-values')  
mtp.ylad()  
mtp.show()




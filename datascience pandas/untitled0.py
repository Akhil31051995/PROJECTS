# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:49:57 20

@author: akhbh
"""

import pandas as pd
import pickle
f1=open(file="naivebayesmodel.pkl",mode="br")
model=pickle.load(f1)  # assign variable while loading to use again
f1.close()
f2=open(file="standard_scaler.pkl",mode="br")
sc=pickle.load(f2)
f2.close()

#a=age,b=salary

def prediction(a,b):
    data={'age':a,'estimated_salary':b}
    df=pd.DataFrame(data,index=[0])
    df=sc.transform(df)
    pred=model.predict(df)
    
    
    if int(pred)==1:
        return'purchased'
    else:
        return 'not purchased'
    
    
age=int(input('enter your age'))
salary=int(input('enter your salary'))

prediction(age,salary)

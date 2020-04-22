#coding=utf-8
'''
Created on 2016.12.25
TopQuant-极宽量化系统·培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''

import pandas as pd
import sklearn 
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import ztop_ai as zai
import zpd_talib as zta

#
#-----------------------

#1 
fs0='dat/iris_'
print('\n1# init，fs0,',fs0)
x_train=pd.read_csv(fs0+'xtrain.csv',index_col=False);
y_train=pd.read_csv(fs0+'ytrain.csv',index_col=False);
x_test=pd.read_csv(fs0+'xtest.csv',index_col=False)
y_test=pd.read_csv(fs0+'ytest.csv',index_col=False)
df9=x_test.copy()

#2
print('\n2# 建模')
mx =zai.mx_GBDT(x_train.values,y_train.values)

#3
print('\n3# 预测')
y_pred = mx.predict(x_test.values)
df9['y_predsr']=y_pred
df9['y_test'],df9['y_pred']=y_test,y_pred
df9['y_pred']=round(df9['y_predsr']).astype(int)   

#4
df9.to_csv('tmp/iris_9.csv',index=False)
print('\n4# df9')
print(df9.tail())
  
#5   
dacc=zai.ai_acc_xed(df9,1,False)
print('\n5# mx:mx_sum,kok:{0:.2f}%'.format(dacc))   

#-----------------------    
print('\nok!')

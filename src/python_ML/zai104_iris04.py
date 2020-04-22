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

import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import ztop_ai as zai
import zpd_talib as zta

#--------------------------------------------------------------------------------

#1 
fs0='dat/iris_'
print('\n1# fs0,',fs0)
x_train=pd.read_csv(fs0+'xtrain.csv',index_col=False)
y_train=pd.read_csv(fs0+'ytrain.csv',index_col=False)


#2
print('\n2# train')
print(x_train.tail())
print(y_train.tail())


#3
#通过ztop_ai模块中的mx_line函数接口间接调用LinearRegression
#Sklearn模块中的机器学习函数，都是使用fit命令自动学习，建立模型。
print('\n3# 建模')
mx =zai.mx_line(x_train.values,y_train.values)

#4 
x_test=pd.read_csv(fs0+'xtest.csv',index_col=False)
df9=x_test.copy()
print('\n4# x_test')
print(x_test.tail())

#5
#运行预测函数，生成结果数据
print('\n5# 预测')
y_pred = mx.predict(x_test.values)
df9['y_predsr']=y_pred

#6
#读入训练数据的正确答案，并保存到变量y_test
y_test=pd.read_csv(fs0+'ytest.csv',index_col=False)
print('\n6# y_test')
print(y_test.tail())


#7
#整理结果变量数据df9
df9['y_test'],df9['y_pred']=y_test,y_pred
df9['y_pred']=round(df9['y_predsr']).astype(int)    #Round a DataFrame to a variable number of decimal places
df9.to_csv('tmp/iris_9.csv',index=False)
print('\n7# df9')
print(df9.tail())

   
#
#8
#检验测试结果
dacc=zai.ai_acc_xed(df9,1,False)
print('\n8# mx:mx_sum,kok:{0:.2f}%'.format(dacc))   

#-----------------------    
print('\nok!')

#coding=utf-8
'''
Created on 2016.12.25
TopQuant-极宽量化系统·培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''


import arrow
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
import zpd_talib as zta
import ztop_ai as zai

#
#-----------------------
    

#-----------------------

#1
#测试相关参数，读取测试所需的数据集
fsr0='dat/ccpp_'
print('#1',fsr0)
mlst1=['line','log','bayes','knn','forest','dtree','svm','mlp','mlpreg']
mlst2=['forest','dtree','svm']
mlst3=['line','log','bayes']
mlst4=['line','forest','dtree']

x_test=zai.ai_f_datRd010(fsr0+'xtest.csv')
y_test=zai.ai_f_datRd010(fsr0+'ytest.csv',1)
    
#2
#批量读取机器学习算法模型，保存到变量xmodel（全局字典变量）
zai.xmodel={}
print('\n#2,ai_f_mxRdlst')
zai.ai_f_mxRdlst(fsr0,mlst1)    

#3
#调用机器学习组合算法函数
print('\n#3,mlst1',mlst1)
zai.mx_mul(mlst1, x_test,  y_test,yk0=1,fgInt=False,fgDebug=False)

#4
print('\n#4,mlst2',mlst2)
zai.mx_mul(mlst2, x_test,  y_test,yk0=1,fgInt=False,fgDebug=False)

#5
print('\n#5,mlst3',mlst3)
zai.mx_mul(mlst3, x_test,  y_test,yk0=1,fgInt=False,fgDebug=False)

#6
print('\n#6,mlst3',mlst4)
zai.mx_mul(mlst4, x_test,  y_test,yk0=1,fgInt=False,fgDebug=False)
  
#-----------------------    
print('\nok!')

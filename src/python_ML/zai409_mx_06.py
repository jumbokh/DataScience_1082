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

import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import zpd_talib as zta
import ztop_ai as zai



#---------------------------------------------------------------------------

#1
#读取测试数据，调用单组数据调用函数
#读取主数据，k0=0，读取以y开头的结果数据，需要进行缩放，并且转换成整数格式，所以参数不同。
fsr0='dat/ccpp_'
print('#1',fsr0)
mxlst=['line','log','bayes','knn','forest','dtree','svm','mlp','mlpreg']
x_test=zai.ai_f_datRd010(fsr0+'xtest.csv')
y_test=zai.ai_f_datRd010(fsr0+'ytest.csv',1)
    
#2
#批量读取算法模型
zai.xmodel={}
print('\n#2,ai_f_mxRdlst')
zai.ai_f_mxRdlst(fsr0,mxlst)    

#3
#批量调用算法模型，并进行分析预测
print('\n#3,mx_funlst8mx')
zai.mx_funlst8mx(mxlst, x_test,  y_test,yk0=5,fgInt=False)
  
#-----------------------    
print('\nok!')

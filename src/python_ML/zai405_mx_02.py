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
import ztop_ai as zai
import zpd_talib as zta


#
#-----------------------


#1
#批量调用的机器学习字符串代码列表
mxlst1=['line','knn','bayes']
mxlst2=['line','log','bayes','knn','forest','dtree','svm','mlp','mlpreg']   
#'gbdt','svmcr'

fsr0='dat/ccpp_'
print('#1',fsr0)
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0)

#2
print('\n#2,mxlst1')
zai.mx_funlst(mxlst1,x_train, x_test, y_train, y_test)    

#3
print('\n#3,mxlst2')
zai.mx_funlst(mxlst2,x_train, x_test, y_train, y_test)    

  
#-----------------------    
print('\nok!')
 
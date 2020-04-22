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


#1 
fsr0='dat/ccpp_'
print('#1',fsr0)
mxlst=['line','log','bayes','knn']
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0)
ftg0='tmp/ccpp_'

#2
#批量存储相关模型代码
print('\n#2,mx_svm.wr')
zai.ai_f_mxWrlst(ftg0,mxlst,x_train, y_train)
  
#-----------------------    
print('\nok!')

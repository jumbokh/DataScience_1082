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
from sklearn.externals import joblib 
from sklearn.model_selection import cross_val_predict

#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
import zpd_talib as zta
import ztop_ai as zai


#-----------------------

#1
#设置参数，读取训练和测试数据
fsr0='dat/ccpp_'
print('#1',fsr0)
xlst,ysgn=['AT','V','AP','RH'],'PE'
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0)
funSgn,ftg='svm','tmp/ccpp_svm.pkl'

#2
#对输入的数据运行机器学习算法，并保存到文件
print('\n#2,mx_svm.wr')
tim0=arrow.now()
zai.ai_f_mxWr(ftg,funSgn,x_train, y_train)
tn=zt.timNSec('',tim0,True)
    
#3
#读取mx模型
tim0=arrow.now()
print('\n#3,mx_svm.rd')
mx = joblib.load(ftg)
tn=zt.timNSec('',tim0,True)

#4
#使用读取的mx模型进行预测分析
print('\n#4,mx_svm')
tim0=arrow.now()
zai.mx_fun8mx(mx,x_test,y_test)
tn=zt.timNSec('',tim0,True)
  
#-----------------------    
print('\nok!')
 
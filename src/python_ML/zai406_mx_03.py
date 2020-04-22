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
xlst,ysgn=['AT','V','AP','RH'],'PE'
df=pd.read_csv('dat/ccpp.csv',index_col=False)

#2
print('\n#2,mx_line')
funsgn='line'
tim0=arrow.now()
zai.mx_fun_call(df,xlst,ysgn,funsgn)
tn=zt.timNSec('',tim0,True)
    

  
#-----------------------    
print('\nok!')
 
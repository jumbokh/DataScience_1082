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


def mx_fun010(funSgn,x_train, x_test, y_train, y_test,yk0=5,fgInt=False,fgDebug=False):
    #1
    df9=x_test.copy()
    mx_fun=zai.mxfunSgn[funSgn]
    mx =mx_fun(x_train.values,y_train.values)
    #2
    y_pred = mx.predict(x_test.values)
    df9['y_test'],df9['y_pred']=y_test,y_pred
    #3   
    if fgInt:
        df9['y_predsr']=df9['y_pred']
        df9['y_pred']=round(df9['y_predsr']).astype(int)
        
    #4
    dacc=zai.ai_acc_xed(df9,yk0,fgDebug)

    #5
    if fgDebug:
        #print(df9.head())
        print('@fun name:',mx_fun.__name__)
        df9.to_csv('tmp/df9_pred.csv')

    #6
    print('@mx:mx_sum,kok:{0:.2f}%'.format(dacc))   
    return dacc,df9   

#-------------------------------------------------------------------------------------------------------

#1 
fsr0='dat/ccpp_'
print('#1',fsr0)
x_train, x_test, y_train, y_test=zai.ai_dat_rd(fsr0)

#2
#设置机器学习函数名称，并调用统一的接口函数
print('\n#2,mx_line')
funSgn='line'
tim0=arrow.now()
dacc,df9=mx_fun010(funSgn,x_train, x_test, y_train, y_test,5,False)
tn=zt.timNSec('',tim0,True)
    
#3
print('\n#3,mx_log')
funSgn='log'
tim0=arrow.now()
dacc,df9=mx_fun010(funSgn,x_train, x_test, y_train, y_test,5,False,True) #True表示采用调试模式输出更多信息
tn=zt.timNSec('',tim0,True)

  
#-----------------------    
print('\nok!')
 
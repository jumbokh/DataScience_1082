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
import zpd_talib as zta

#-------------------------------------------------------------------------------------
def ai_data_cut(df,xlst,ysgn,ftg0,fgPr=False):
    x,y= df[xlst],df[ysgn]      
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    #
    fss=ftg0+'xtrain.csv';x_train.to_csv(fss,index=False);print(fss)
    fss=ftg0+'xtest.csv';x_test.to_csv(fss,index=False);print(fss)
    fss=ftg0+'ytrain.csv';y_train.to_csv(fss,index=False,header=True);print(fss)
    fss=ftg0+'ytest.csv';y_test.to_csv(fss,index=False,header=True);print(fss)
    #
    if fgPr:
        print('\nx_train');print(x_train.tail())
        print('\nx_test');print(x_test.tail())
        print('\ny_train');print(y_train.tail())
        print('\ny_test');print(y_test.tail())        
                                      
    

#-----------------------

#1 
fss='dat/ccpp.csv'
df=pd.read_csv(fss,index_col=False)

#2
print('\n2# df')       
print(df.tail())

#3
#设置相关参数，调用切割函数
xlst,ysgn=['AT','V','AP','RH'],'PE'
ftg0='tmp/ccpp_'
ai_data_cut(df,xlst,ysgn,ftg0,True)
    


#-----------------------    
print('\nok!')
 
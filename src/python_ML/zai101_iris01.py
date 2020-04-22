#coding=utf-8
'''
Created on 2016.12.25
TopQuant-极宽量化系统·培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''

import pandas as pd

#-----------------------------------------------------

#1 
fss='dat/iris.csv'
df=pd.read_csv(fss,index_col=False)
print('\n#1 df')
print(df.tail())        #tail(n)returns last n rows from the object based on position,n default 5
print(df.describe())    #Generates descriptive statistics that summarize the central tendency

#2
d10=df['xname'].value_counts()   #Returns object containing counts of unique values
print('\n#2 xname')       
print(d10)       

#-----------------------------------------------------
print('\nok!')

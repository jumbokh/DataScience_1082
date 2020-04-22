#coding=utf-8
'''
Created on 2016.12.25
TopQuant-极宽量化系统·培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com

'''

import pandas as pd

#--------------------------------------------------------------

#1 
#读取数据文件，保存到df变量
fss='dat/iris.csv'
df=pd.read_csv(fss,index_col=False)

#2
#loc() Access group of values using labels
df.loc[df['xname']=='virginica', 'xid'] = 1
df.loc[df['xname']=='setosa', 'xid'] = 2
df.loc[df['xname']=='versicolor', 'xid'] = 3
df['xid']=df['xid'].astype(int)
df.to_csv('tmp/iris2.csv',index=False)       #将iris2文件复制到tmp目录下

#3
print('\n3#df')       
print(df.tail())
print(df.describe())

#4
d10=df['xname'].value_counts()
print('\n4#xname')       
print(d10)       

#5
d10=df['xid'].value_counts()
print('\n5#xid')       
print(d10)       

        
#-----------------------    
print('\nok!')

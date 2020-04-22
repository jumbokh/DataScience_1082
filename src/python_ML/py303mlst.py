#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''
import numpy as np
import scipy as sp
import pandas as pd
import pip

# =======================
x10=pip.get_installed_distributions();
df=pd.DataFrame();
df['name']=x10
print(df.head())

df.to_csv('tmp/m10.csv',index=False)

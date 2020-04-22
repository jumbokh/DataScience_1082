#coding=utf-8
# -*- coding: utf-8 -*- 
'''
Top极宽量化(原zw量化)，Python量化第一品牌 
网站:www.TopQuant.vip   www.ziwang.com
QQ总群:124134140   千人大群 zwPython量化&大数据 
    
TopQuant.vip ToolBox 2016
Top极宽·量化开源工具箱 系列软件 
by Top极宽·量化开源团队 2016.12.25 首发
  
文件名:ztools_data.py
默认缩写：import ztools_data as zdat
简介：Top极宽常用工具函数集
'''

import os,sys,io,re
import random,arrow,bs4
import numpy as np
import numexpr as ne
import pandas as pd
import tushare as ts

import requests
#
import cpuinfo as cpu
import psutil as psu
import inspect
#
import matplotlib as mpl
import matplotlib.colors
from matplotlib import cm

#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb

#

#-----------------------
'''

misc
#
df.xxx,pandas.xxx
    df.cov.
    df.get.
    df.cut.
#

'''

#-----------------------
#----------misc
def fb_df_type2float(df,xlst):
    for xsgn in xlst:
        df[xsgn]=df[xsgn].astype(float)

def fb_df_type4mlst(df,nlst,flst):
    for xsgn in nlst:
        df[xsgn]=df[xsgn].astype(int)
        
    for xsgn in flst:
        df[xsgn]=df[xsgn].astype(float)
        
def df_type2float(df,xlst):
    for xsgn in xlst:
        df[xsgn]=df[xsgn].astype(float)

def df_type4mlst(df,nlst,flst):
    for xsgn in nlst:
        df[xsgn]=df[xsgn].astype(int)
        
    for xsgn in flst:
        df[xsgn]=df[xsgn].astype(float)
            
    
#----------df.xxx,pandas.xxx

#----------df.cov.xxx,pandas.xxx       
def df_2ds8xlst(df,ds,xlst):
    for xss in xlst:
        ds[xss]=df[xss]
    #
    
    #df9.to_csv(ftg,index=False,encoding='gbk')
    return ds
    
#----------df.get.xxx,pandas.xxx       
def df_get8tim(df,ksgn,kpre,kn9,kpos):
    #@ zdr.dr_df_get8tim
    #
    xdf=pd.DataFrame(columns=['nam','dnum'])
    ds=pd.Series(['',0],index=['nam','dnum'])
    for xc in range(1,kn9+1):
        xss,kss='{0:02d}'.format(xc),'{0}{1:02d}'.format(kpre,xc)
        df2=df[df[ksgn].str.find(kss)==kpos]
        ds['nam'],ds['dnum']=xss,len(df2['gid'])
        xdf=xdf.append(ds.T,ignore_index=True)
        #print(xc,'#',xss,kss)
    #
    xdf.index=xdf['nam']
    return xdf

#----------df.cut.xxx,pandas.xxx            
def df_kcut8tim(df,ksgn,tim0str,tim9str):
    df2=df[tim0str<=df[ksgn]]
    df3=df2[df2[ksgn]<=tim9str]
    return df3
        
def df_kcut8yearlst(df,ksgn,ftg0,yearlst):
    for ystr in yearlst:
        tim0str,tim9str=ystr+'-01-01',ystr+'-12-31'
        df2=df_kcut8tim(df,ksgn,tim0str,tim9str)
        ftg=ftg0+ystr+'.dat';print(ftg)
        df2.to_csv(ftg,index=False,encoding='gb18030')
    
def df_kcut8myearlst(df,ksgn,tim0str,ftg0,yearlst):
    for ystr in yearlst:
        tim9str=ystr+'-12-31'
        df2=df_kcut8tim(df,ksgn,tim0str,tim9str)
        ftg=ftg0+ystr+'.dat';print(ftg)
        df2.to_csv(ftg,index=False,encoding='gb18030')
    

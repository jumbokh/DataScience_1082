# -*- coding: utf-8 -*- 
'''
Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2016.12.25 首发
   
Top Football，又称Top Quant for football-简称TFB
TFB极宽足彩量化分析系统，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
QQ总群:124134140   千人大群 zwPython量化&大数据 

  
文件名:tfb_draw.py
默认缩写：import tfb_draw as tfbdr
简介：Top极宽量化·常用足彩绘图函数模块
 

'''
#

import sys,os,re
import os,sys,re
import arrow,bs4,random

import numpy as np
import pandas as pd
import tushare as ts
#import talib as ta

import matplotlib as mpl
from matplotlib import pyplot as plt

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
#import multiprocessing
#
#import arrow
import datetime as dt
import time
from dateutil.rrule import *
from dateutil.parser import *
import calendar as cal
#
import csv
import pickle
import numexpr as ne  

#
import requests
import bs4
from bs4 import BeautifulSoup 
from robobrowser import RoboBrowser 
#from selenium import webdriver

#
import zsys
import ztools as zt
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft




        
#----------fb.get.misc.xxx
def dr_gid_top10(df,ksgn,ftg0=''):
    
    xn9=len(df['gid'])
    d10=df[ksgn].value_counts()[:10];print(d10)
    
    #
    #---set chinese font
    mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  
    #             
    d10.plot(kind = 'bar',rot=0,color=zsys.cors_brg)
    if ftg0!='':plt.savefig(ftg0+'_bar.png')
    plt.show()
    #            
    dsum=d10.sum()
    d10['other']=xn9-dsum
    k10=np.round(d10/xn9*100,decimals=2)
       
    k10.plot(kind = 'pie',rot=0,table=True)
    if ftg0!='':plt.savefig(ftg0+'_pie.png')
    plt.show()
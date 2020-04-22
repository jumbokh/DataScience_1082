#coding=utf-8
'''
Created on 2016.12.25
Top Quant-极宽量化分析系统
培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''

import pandas as pd
import numpy as np

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm

import zsys
import ztools as zt

def dr_cormap(fcor='dat/cormap.dat'):
    #font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  
    clst=zt.f_lstRdTxt(fcor)
    ds=pd.Series(range(5,25))
    for xc,cor in enumerate(clst):
        css=cor[0]
        xss='cm.'+str(css)+'(np.linspace(0,1,10))'
        print(xc,'#',css,xss)
        cor2=eval(xss)
        #print(css,xss,cor2)
        ds.plot(kind='bar',rot=0,color=cor2) 
        plt.savefig('tmp/cm_'+css+'.png')

def dr_cors_sys():
    ds=pd.Series(range(5,25));print(ds)
    ds.plot(kind='bar',rot=0,color=zsys.cors_prism) 
    plt.savefig('tmp/prism.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_brg) 
    plt.savefig('tmp/brg.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_Dark2) 
    plt.savefig('tmp/dark2.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_hsv) 
    plt.savefig('tmp/hsv.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_jet) 
    plt.savefig('tmp/jet.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_hsv) 
    plt.savefig('tmp/hsv.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_hot) 
    plt.savefig('tmp/hot.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_Vega10) 
    plt.savefig('tmp/Vega10.png')    

    ds.plot(kind='bar',rot=0,color=zsys.cors_Vega20) 
    plt.savefig('tmp/Vega20.png')    


dr_cormap()
dr_cors_sys()

print('\nok,!')

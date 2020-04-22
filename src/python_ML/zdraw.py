# -*- coding: utf-8 -*- 
'''
Top极宽量化(原zw量化)，Python量化第一品牌 
网站:www.TopQuant.vip   www.ziwang.com
QQ总群:124134140   千人大群 zwPython量化&大数据 
    
TopQuant.vip ToolBox 2016
Top极宽·量化开源工具箱 系列软件 
by Top极宽·量化开源团队 2016.12.25 首发
  
文件名:zdraw.py
默认缩写：zdr,示例：import zdraw as zdr
简介：Top极宽量化软件，绘图模块
'''


import sys,os
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
#from PIL import Image,ImageDraw,ImageFont
#
import plotly as py
import plotly.graph_objs as pygo
from plotly import tools
from plotly.graph_objs import *
from plotly.graph_objs import Scatter, Layout, Figure
from plotly.tools import FigureFactory as pyff

#
import zsys
import ztools as zt
import ztools_data as zdat

'''
var&const
#

misc
#
dr.mul.xxx
dr.fintech
#

'''
#----var&const.pre_def
pyplt=py.offline.plot

#----------dr.misc
def dr_df_get8tim(xdf):
    #@zdat.df_get8tim
    #
    print(xdf)
    xdf.plot(kind = 'bar',rot=0)    
    plt.show()
    #
    dsum=xdf['dnum'].sum()
    xdf['k10']=np.round(xdf['dnum']/dsum*100,decimals=2)
    xdf['k10'].plot(kind = 'pie',rot=0,table=True)
    plt.show()
    
#----------dr.mul.xxx

def dr_mul_line(df,ftg='tmp/tmp_plotly.html',m_tkAng=-20,m_dtick=5,
                m_title='多周期分时数据',
                xlst=['t1','t5','t15','t30','t60']):
    xdat = pygo.Data([])
    for xsgn in xlst:
        r_xnam='r_'+xsgn
        r_xnam = pygo.Scatter(
            x=df.index,
            y=df[xsgn],
            name=xsgn,
            connectgaps=True,
            )
        #
        xdat.extend([r_xnam])
    #
    lay = pygo.Layout( 
        title=m_title,
        xaxis=pygo.XAxis(
            gridcolor='rgb(180, 180, 180)',
            mirror='all',
            showgrid=True,
            showline=True,
            ticks='outside',#'inside',
            #
            dtick=m_dtick,
            tickangle=m_tkAng,
            #
            type='category',
            categoryarray=df.index,
        ),
                       
    ) #lay = pygo.Layout( 
    r_vol = pygo.Bar(
            x=df.index,#df['xtim'],
            y=df['volume'],
            name='volume',
            yaxis= 'y2',
            opacity=0.6,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(color='rgb(8,48,107)',width=1.5,),
            ),
    )   #r_vol
    #
    fig['data'].extend([r_vol])
    #
    #xdat = pygo.Data([r_t1,r_t5,r_t15,r_t30,r_t60])
    fig = pygo.Figure(data=xdat, layout=lay)
    pyplt(fig,filename=ftg,show_link=False)
 

def dr_mul_xline(df,ftg='tmp/tmp_plotly.html',m_tkAng=-20,m_dtick=5,
                m_title='多周期分时数据',
                xlst=['t1','t5','t15','t30','t60']):
    r_vol = pygo.Bar(
            x=df.index,#df['xtim'],
            y=df['volume'],
            name='volume',
            yaxis= 'y2',
            opacity=0.6,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(color='rgb(8,48,107)',width=1.5,),
            ),
    )   #r_vol
    #        
    xdat = pygo.Data([r_vol])
    for xsgn in xlst:
        r_xnam='r_'+xsgn
        r_xnam = pygo.Scatter(
            x=df.index,
            y=df[xsgn],
            name=xsgn,
            connectgaps=True,
            )
        #
        xdat.extend([r_xnam])
    #
    lay = pygo.Layout( 
        title=m_title,
        xaxis=pygo.XAxis(
            gridcolor='rgb(180, 180, 180)',
            mirror='all',
            showgrid=True,
            showline=True,
            ticks='outside',#'inside',
            #
            dtick=m_dtick,
            tickangle=m_tkAng,
            #
            type='category',
            categoryarray=df.index,
        ),
        yaxis2=pygo.YAxis(
                side='right', 
                overlaying='y',
                range=[0,max(df['volume'])*3],
        ),                
    ) #lay = pygo.Layout( 
    
    #xdat = pygo.Data([r_t1,r_t5,r_t15,r_t30,r_t60])
    fig = pygo.Figure(data=xdat, layout=lay)
    pyplt(fig,filename=ftg,show_link=False)
    

def dr_mul_xsub(df,ftg='tmp/tmp_plotly.html',m_tkAng=-20,m_dtick=5,
                m_title='多周期分时数据',
                xlst=['t1','t5','t15','t30','t60']):
    r_vol = pygo.Bar(
            x=df.index,#df['xtim'],
            y=df['volume'],
            name='volume',
            yaxis= 'y2',
            opacity=0.6,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(color='rgb(8,48,107)',width=1.5,),
            ),
    )   #r_vol
    # vertical_spacing
    fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True,horizontal_spacing=0.01)
    #        
    for xsgn in xlst:
        r_xnam='r_'+xsgn
        r_xnam = pygo.Scatter(
            x=df.index,
            y=df[xsgn],
            name=xsgn,
            connectgaps=True,
            )
        #
        #xdat.extend([r_xnam])
        fig.append_trace(r_xnam, 1, 1)
    #
    fig['layout'].update(
    #lay = pygo.Layout( 
        title=m_title,
        xaxis=pygo.XAxis(
            gridcolor='rgb(180, 180, 180)',
            mirror='all',
            showgrid=True,
            showline=True,
            ticks='outside',#'inside',
            #
            dtick=m_dtick,
            tickangle=m_tkAng,
            #
            type='category',
            categoryarray=df.index,
        ),
    ) #lay = pygo.Layout( 
    
    #xdat = pygo.Data([r_t1,r_t5,r_t15,r_t30,r_t60])
    #fig = pygo.Figure(data=xdat, layout=lay)
    fig.append_trace(r_vol, 2, 1)
    pyplt(fig,filename=ftg,show_link=False)    


    
#--------------dr.fintech
def dr_tick(df,ftg='tmp/tmp_plotly.html',m_title='tick数据'):
    r_price = pygo.Scatter(
        x=df['xtim'],
        y=df['price'],
        name='price'
    )
    r_vol = pygo.Bar(
        x=df['xtim'],
        y=df['volume'],
        name='volume',
        #yaxis= 'y2'
    )

    lay = pygo.Layout( 
        title=m_title,
        xaxis=pygo.XAxis(
            #autorange=True,
            gridcolor='rgb(180, 180, 180)',
            #gridwidth=1,
            dtick=5,
            mirror='all',
            showgrid=True,
            showline=True,
            ticks='outside',#'inside',
            tickangle=-20,
            #
            type='category',
            categoryarray=df.index,
        ),
        yaxis2=pygo.YAxis(
            side='right', 
            overlaying='y',
            range=[0,max(df['volume'])*3],
        ),
    ) #lay = pygo.Layout( 

    xdat = pygo.Data([r_price,r_vol])
    fig = pygo.Figure(data=xdat, layout=lay)
    pyplt(fig,filename=ftg,show_link=False)
#---
def dr_cdl(df,m_title='分时数据K线图',ftg='tmp/tmp_plotly.html',m_tkAng=-20,m_dtick=5,m_y2k=3):
    fig=pyff.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index)
    fig['layout'].update(title=m_title,
        xaxis=pygo.XAxis(
            autorange=True,
            gridcolor='rgb(180, 180, 180)',
            mirror='all',
            showgrid=True,
            showline=True,
            ticks='outside',
            tickangle=m_tkAng,
            dtick=m_dtick,
            type='category',
            categoryarray=df.index,
            ),
        yaxis=pygo.YAxis(
            autorange=True,
            gridcolor='rgb(180, 180, 180)',
            ),
        yaxis2=pygo.YAxis(
                side='right', 
                overlaying='y',
                range=[0,max(df['volume'])*m_y2k],
            ),
    )  # fig.update
    r_vol = pygo.Bar(
            x=df.index,#df['xtim'],
            y=df['volume'],
            name='volume',
            yaxis= 'y2',
            opacity=0.6,
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(color='rgb(8,48,107)',width=1.5,),
            ),
    )   #r_vol
    #
    fig['data'].extend([r_vol])
    #
    pyplt(fig,filename=ftg,show_link=False)

#coding=utf-8
import math
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from dateutil.parser import parse

def open_csv(file,lack_values):
    f = pd.read_csv(file,header=0,encoding='utf-8')
    f1 = DataFrame(f)
    f10 = f1.replace(lack_values,np.nan)
    f11 = f10.dropna()
    index_list = f.keys()
    time_index = str(index_list[0])
    f11[time_index] = f1[time_index].map(lambda x:parse(str(x)))
    f11.index = f11[time_index]
    return(f11)

def draw_ax(df,index_list,fig,num1,num2,i,keywords):
    scheme = keywords['scheme']
    range_adjustment = keywords['range_adjustment']
    color_list = keywords['color_list']
    ax = fig.add_subplot(num1,num2,i)
    if(scheme == 'bar'): 
        ax.bar(df[index_list[0]],height=df[index_list[i]],color = color_list[i-1])       
    elif(scheme == 'linesc'):
        ax.plot(df[index_list[0]],df[index_list[i]],color = color_list[i-1])
        ax.scatter(df[index_list[0]],df[index_list[i]],color = color_list[i-1])
    else:
        ax.plot(df[index_list[0]],df[index_list[i]],color = color_list[i-1])
    ax.set_xlabel('time')
    ax.set_ylabel(index_list[i])
    if(i in range_adjustment):
        k_y0 = (max(df[index_list[i]])-min(df[index_list[i]]))/max(df[index_list[i]])
        y0 = min(df[index_list[i]])*(1-abs(k_y0))
        y1 = max(df[index_list[i]])*(1+abs(k_y0))
        plt.ylim(ymin=y0,ymax=y1)
    else:
        print()
    #plt.xticks(rotation=30) #坐标轴倾斜，解决坐标轴标签重叠问题
    plt.subplots_adjust(hspace=0.3,wspace=0.3)
    #plt.ticklabel_format(axis='y',style='sci', scilimits=(1,0)) #科学计数法,解决某些版本不能自动显示科学计数法的问题
    return(ax)

def time_series(df,**keywords):
    index_list = df.keys()
    num = len(index_list)-1
    num1 = int(num**0.5)
    num2 = math.ceil(num/num1)
    try:
        scheme = keywords['scheme']
    except:
        keywords['scheme']=0;
    try:
        range_adjustment = keywords['range_adjustment']
    except:
        keywords['range_adjustment']=[];
    try:
        color_list = keywords['color_list']
    except:
        keywords['color_list'] = ['c']*num   
    fig=plt.figure(figsize=(num1*5,num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df,index_list,fig,num1,num2,i,keywords)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

def year_mean(df,start_year,end_year,**keywords):  
    index_list = df.keys()
    time_index = str(index_list[0])
    num = len(index_list)-1
    num1 = int(num**0.5)
    num2 = math.ceil(num/num1)
    try:
        scheme = keywords['scheme']
    except:
        keywords['scheme']=0;
    try:
        range_adjustment = keywords['range_adjustment']
    except:
        keywords['range_adjustment']=[];
    try:
        color_list = keywords['color_list']
    except:
        keywords['color_list'] = ['c']*num   
    year_list = [str(year) for year in range(start_year,end_year+1)]
    dict1 = {time_index:year_list}
    df1 = DataFrame(dict1)
    for i in range(1,num+1):
        year_average = []
        data = df[str(index_list[i])]
        for year in year_list:
            year_average.append(data[year].mean());
        df1[str(index_list[i])] = year_average    
    fig=plt.figure(figsize=(num1*5,num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,num1,num2,i,keywords)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    
def month_mean(df,**keywords):
    index_list = df.keys()
    time_index = str(index_list[0])
    num = len(index_list)-1
    num1 = int(num**0.5)
    num2 = math.ceil(num/num1)
    try:
        scheme = keywords['scheme']
    except:
        keywords['scheme']=0;
    try:
        range_adjustment = keywords['range_adjustment']
    except:
        keywords['range_adjustment']=[];
    try:
        color_list = keywords['color_list']
    except:
        keywords['color_list'] = ['c']*num
    month_list = [str(month) for month in range(1,13)]
    dict1 = {time_index:month_list}
    df1 = DataFrame(dict1)
    for i in range(1,num+1):
        data = df[str(index_list[i])].resample('m').mean()
        data.index = data.index.strftime('%m')
        average_list = data.groupby(data.index).mean()
        average_list = average_list.values
        df1[str(index_list[i])] = average_list
    fig=plt.figure(figsize=(num1*5,num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,num1,num2,i,keywords)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

def hour_mean(df,**keywords):
    index_list = df.keys()
    time_index = str(index_list[0])
    num = len(index_list)-1
    num1 = int(num**0.5)
    num2 = math.ceil(num/num1)
    try:
        scheme = keywords['scheme']
    except:
        keywords['scheme']=0;
    try:
        range_adjustment = keywords['range_adjustment']
    except:
        keywords['range_adjustment']=[];
    try:
        color_list = keywords['color_list']
    except:
        keywords['color_list'] = ['c']*num
    hour_num = [i for i in range(24)]
    df['hour'] = df[str(index_list[0])].map(lambda x:x.hour)
    x = []
    time_str = ':00'
    for i in hour_num:
        i_str = str(i)
        x.append(i_str+time_str);
    dict1 = {time_index:x}
    df1 = DataFrame(dict1)
    for i in range(1,num+1):
        out_mean = []
        for hour in hour_num:
            hour_df = df[df['hour'] == hour]
            out_mean.append(hour_df[str(index_list[i])].mean())
        df1[str(index_list[i])] = out_mean
    fig=plt.figure(figsize=(num1*5,num2*5),dpi=200)        
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,num1,num2,i,keywords)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
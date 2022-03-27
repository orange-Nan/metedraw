#coding=utf-8
import math
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from dateutil.parser import parse

def preprocessing(data,**keywords):
    data = DataFrame(data)
    index_list = data.keys()
    time_index = str(index_list[0])
    data[time_index] = data[time_index].map(lambda x:parse(str(x)))
    data.index = data[time_index]   
    try:
        print_timeindex = keywords['print_timeindex']
        print('start time:',data[time_index][0],'end time:',data[time_index][len(data[time_index])-1])
    except:
        print_timeindex = False
    try:
        lack_values = keywords['lack_values']
        data = data.replace(lack_values,np.nan)
        data = data.dropna()
    except:
        lack_values = False
    try:
        start_time = keywords['start_time']
        end_time = keywords['end_time']
        data = data[start_time:end_time]
    except:
        keywords['start_time'] = False   
    return data

def get_num(index_list):
    num = len(index_list)-1
    sub_num1 = int(num**0.5)
    sub_num2 = math.ceil(num/sub_num1) 
    return num,sub_num1,sub_num2

def draw_ax(df,index_list,fig,i,num,sub_num1,sub_num2,keywords):
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
        keywords['color_list'] = ['k']*num       
    ax = fig.add_subplot(sub_num1,sub_num2,i)
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
    #plt.xticks(rotation=30) #坐标轴倾斜，解决坐标轴标签重叠问题
    #plt.ticklabel_format(axis='y',style='sci', scilimits=(1,0)) #科学计数法,解决某些版本不能自动显示科学计数法的问题
    return ax

def plt_adjust():
    plt.subplots_adjust(hspace=0.3,wspace=0.3)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

def time_series(df,**keywords):
    index_list = df.keys()
    num,sub_num1,sub_num2 = get_num(index_list)
    fig=plt.figure(figsize=(sub_num1*5,sub_num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df,index_list,fig,i,num,sub_num1,sub_num2,keywords)
    plt_adjust()

def year_mean(df,**keywords):  
    index_list = df.keys()
    num,sub_num1,sub_num2 = get_num(index_list)
    time_index = str(index_list[0])
    start_year = df[time_index][0].year
    end_year = df[time_index][len(df)-1].year
    year_list = [str(year) for year in range(start_year,end_year+1)]
    dict1 = {time_index:year_list}
    df1 = DataFrame(dict1)
    for i in range(1,num+1):
        year_average = []
        data = df[str(index_list[i])]
        for year in year_list:
            year_average.append(data[year].mean());
        df1[str(index_list[i])] = year_average    
    fig=plt.figure(figsize=(sub_num1*5,sub_num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,i,num,sub_num1,sub_num2,keywords)
    plt_adjust()
       
def month_mean(df,**keywords):
    index_list = df.keys()
    num,sub_num1,sub_num2 = get_num(index_list)
    time_index = str(index_list[0])
    month_list = [str(month) for month in range(1,13)]
    dict1 = {time_index:month_list}
    df1 = DataFrame(dict1)
    for i in range(1,num+1):
        data = df[str(index_list[i])].resample('m').mean()
        data.index = data.index.strftime('%m')
        average_list = data.groupby(data.index).mean()
        average_list = average_list.values
        df1[str(index_list[i])] = average_list
    fig=plt.figure(figsize=(sub_num1*5,sub_num2*5),dpi=200)
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,i,num,sub_num1,sub_num2,keywords)
    plt_adjust()

def hour_mean(df,**keywords):
    index_list = df.keys()
    num,sub_num1,sub_num2 = get_num(index_list)
    time_index = str(index_list[0])
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
    fig=plt.figure(figsize=(sub_num1*5,sub_num2*5),dpi=200)        
    for i in range(1,num+1):
        draw_ax(df1,index_list,fig,i,num,sub_num1,sub_num2,keywords)
    plt_adjust()
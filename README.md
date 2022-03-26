# metedraw
metedraw is a project mainly for data visualization projects of Atmospheric Science, Marine Science, Environmental Science or other majors, you can use metedraw for simple meteorological, environmental or other data visualization.
Our intention is to make it easier for students, researchers and practitioners in these fields -- they often have a lot of data to deal with, but most of these items are simple analysis. So we thought we could develop a program that would simplify those repetitive mechanical tasks.
To start with this project, please read _使用说明.docx. The manual in English will be released later.

metedraw是一个主要面向于大气科学、海洋科学、环境科学等专业的数据可视化项目，您可以使用metedraw来完成一些简单的气象、环境等数据可视化的工作。
我们的初衷是方便这些专业的学生、科研工作者、从业人员——因为他们通常有大量的数据需要处理，但是大部分只是较为简单的分析。因此我们认为可以开发这样的一个项目，简化那些重复的机械的劳动。
开始使用这个项目，请阅读_使用说明.docx（中文使用手册）。


—— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——

# metedraw 1.1    ——2022/3/26
【新增】
预处理函数preprocessing

    默认功能：解析第一列为时间（方便后续绘图）
    可选功能：print_timeindex输出文件的起始时间和终止时间、lack_values处理异常值、start_time,end_time截取时间段
  （其他的常见预处理方法，诸如标准化等，用户可直接使用pandas/sklearn等库包中的相关函数）

—— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— —— ——

# metedraw 1.0    ——2022/2/11

【介绍】
4种常用时间分析方法：时间序列time_series、年变化year_mean、月变化month_mean和日变化hour_mean；
3个可选参数：scheme画图类型、range_adjustment坐标范围调整、color_list配色方案。

【功能特点】

    1.自动解析时间（气象数据为时间序列，文件第一列为时间），支持多种时间格式；
    2.自动筛选缺测值（文件中的Nan，或者用-999这样的数值标记的缺测值、异常值）；
    3.自动根据文件中变量数目，生成相应数目的子图；
    4.自动调整子图排列方式、子图间距；
    5.range_adjustment自动坐标范围调整，解决matplotlibs只能手动调整坐标刻度的问题，适合绘制气压等数据；
    6.可配合matplotlib.pyplot使用，绘制更符合您需求的图片。

【作品展示】
示例1：2015-2020年沈阳市气象数据年变化（温度、露点、气压、风速）
![Shenyang_meteorological_annual_variation](https://user-images.githubusercontent.com/71633656/153591108-ef5b93dd-02d0-4b08-b1a4-0aa3b9ba4eea.jpg)

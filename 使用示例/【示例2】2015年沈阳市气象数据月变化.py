import pandas as pd
import matplotlib.pyplot as plt
import metedraw as md

file = r'C:\Users\LULU\Desktop\metedraw\Shenyang_meteorological_month.xls'
lack_values = -999
color_list1 = ['#9ACD32','#6B8E23','#8FBC8F','#006400']
data = pd.read_excel(file)
df = md.preprocessing(data,print_timeindex = True,lack_values = -999,start_time='2015-1-1',end_time='2015-12-1')
md.month_mean(df,scheme = 'linesc',range_adjustment = [3],color_list = color_list1)

plt.suptitle('2015 monthly variation of meteorological data in Shenyang',fontsize=15,y=0.92)
plt.savefig('C:/Users/LULU/Desktop/Shenyang_meteorological_monthly_variation.jpg')
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
import metedraw as md

file = r'C:\Users\LULU\Desktop\metedraw\Shenyang_meteorological_month.csv'
lack_values = -999
color_list1 = ['#9ACD32','#6B8E23','#8FBC8F','#006400']
data = pd.read_csv(file)
data = md.preprocessing(data,print_timeindex = True,lack_values = -999)
md.year_mean(data,scheme = 'bar',range_adjustment = [1,3,4],color_list = color_list1)

plt.suptitle('2015-2020 annual variation of meteorological data in Shenyang',fontsize=15,y=0.92)
plt.savefig('C:/Users/LULU/Desktop/Shenyang_meteorological_annual_variation.jpg')
plt.show()




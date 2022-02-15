import netCDF4 as nc
import matplotlib.pyplot as plt

#导入文件
filename = r'C:\Users\LULU\Desktop\air.nc'
f = nc.Dataset(filename)

#提取变量
level = f.variables['level'][:]
#print(level)

air_mean = []
for i in range(16):
    air = f.variables['air'][0,i,:,:].compressed().mean() #取17个层次上的有效气温数据，每个层次的气温的平均值
    air_mean.append(air)
    
#print(air_mean)  #可以查看一下数据

x=[i for i in range(16)]

fig=plt.figure(figsize=(10,10),dpi=200)  #创建画布
plt.bar(x,height=air_mean, color="grey", edgecolor="black")

plt.xticks([0,2,4,6,8,10,12,14],['1000','850','600','400','250','150','70','30']) #标上每层的气压
plt.ylabel('Temperature(°C)')
plt.xlabel('Level(hPa)')

plt.title('Monthly Mean of Air temperature',fontsize=15,y=1.05) #添加标题，调整字号和位置
plt.savefig('C:/Users/LULU/Desktop/Average_temperature_of_each_level.jpg')
plt.show()



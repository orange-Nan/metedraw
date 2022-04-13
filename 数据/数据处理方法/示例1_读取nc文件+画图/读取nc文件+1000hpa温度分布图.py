#导入需要用到的包，此处读取nc文件使用的是netCDF4
import netCDF4 as nc
import matplotlib.pyplot as plt

#导入文件
filename = r'C:\Users\LULU\Desktop\air.nc'
f = nc.Dataset(filename)

#查看文件信息
#print(f)  

#获取所有变量信息
all_vars = f.variables.keys()  #查看变量名称
#print(all_vars)  #dict_keys(['level', 'lat', 'lon', 'time', 'air'])
all_vars_info = f.variables.items()  #查看变量详细信息
#print(all_vars_info)  

#查看单个变量信息
var_info = f.variables['level']  #获取变量信息
var_data = f['level'][:]  #获取变量数据
#print(var_info)
#print(var_data)

#提取变量
level = f.variables['level'][:]
lat = f.variables['lat'][:]
lon = f.variables['lon'][:]
time = f.variables['time']
air = f.variables['air'][:]  #注意，这里的air是分层次的多维数组(Monthly Mean of Air temperature，时间只有一维，说明是只有某个月的)
air1 = f.variables['air'][0,0,:,:] #取时间为0，层次为0(1000hPa)的所有格点的air（气温）
#print(air1)  #可以查看一下数据

fig=plt.figure(figsize=(10,10),dpi=200)  #创建画布
im = plt.imshow(air1,cmap='jet')  #绘图，air1必须是二维的数据
plt.yticks([0,36.5,72],['90°N','0°','90°S'])  #标上纬度，lat的数目是73
plt.xticks([0,36,72,108,143],['0°','90°E','180°','90°W','0°']) #标上经度，lon的数目是144
plt.colorbar(im,label='Temperature(°C)', orientation='horizontal') #添加图例
plt.title('Monthly Mean of Air temperature(1000hPa)',fontsize=15,y=1.1) #添加标题，调整字号和位置
plt.savefig('C:/Users/LULU/Desktop/Temperature_distribution(1000hPa).jpg')
plt.show()



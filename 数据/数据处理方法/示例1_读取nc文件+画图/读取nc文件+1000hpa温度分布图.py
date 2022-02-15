import netCDF4 as nc
import matplotlib.pyplot as plt

#�����ļ�
filename = r'C:\Users\LULU\Desktop\air.nc'
f = nc.Dataset(filename)

#�鿴�ļ���Ϣ
#print(f)  

#��ȡ���б�����Ϣ
all_vars = f.variables.keys()  #�鿴��������
#print(all_vars)  #dict_keys(['level', 'lat', 'lon', 'time', 'air'])
all_vars_info = f.variables.items()  #�鿴������ϸ��Ϣ
#print(all_vars_info)  

#�鿴����������Ϣ
var = 'level'
var_info = f.variables[var]  #��ȡ������Ϣ
var_data = f[var][:]  #��ȡ��������
#print(var_info)   #air(time, level, lat, lon)
#print(var_data)

#��ȡ����
level = f.variables['level'][:]
lat = f.variables['lat'][:]
lon = f.variables['lon'][:]
time = f.variables['time']
air = f.variables['air'][:]  #ע�⣬�����air�Ƿֲ�εĶ�ά����(Monthly Mean of Air temperature��ʱ��ֻ��һά��˵����ֻ��ĳ���µ�)
air1 = f.variables['air'][0,0,:,:] #ȡʱ��Ϊ0�����Ϊ0(1000hPa)�����и���air�����£�
#print(air1)  #���Բ鿴һ������

fig=plt.figure(figsize=(10,10),dpi=200)  #��������
im = plt.imshow(air1,cmap='jet')  #��ͼ��air1�����Ƕ�ά������
plt.yticks([0,36.5,72],['90��N','0��','90��S'])  #����γ�ȣ�lat����Ŀ��73
plt.xticks([0,36,72,108,143],['0��','90��E','180��','90��W','0��']) #���Ͼ��ȣ�lon����Ŀ��144
plt.colorbar(im,label='Temperature(��C)', orientation='horizontal') #���ͼ��
plt.title('Monthly Mean of Air temperature(1000hPa)',fontsize=15,y=1.1) #��ӱ��⣬�����ֺź�λ��
plt.savefig('C:/Users/LULU/Desktop/Temperature_distribution(1000hPa).jpg')
plt.show()



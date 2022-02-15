import netCDF4 as nc
import matplotlib.pyplot as plt

#�����ļ�
filename = r'C:\Users\LULU\Desktop\air.nc'
f = nc.Dataset(filename)

#��ȡ����
level = f.variables['level'][:]
#print(level)

air_mean = []
for i in range(16):
    air = f.variables['air'][0,i,:,:].compressed().mean() #ȡ17������ϵ���Ч�������ݣ�ÿ����ε����µ�ƽ��ֵ
    air_mean.append(air)
    
#print(air_mean)  #���Բ鿴һ������

x=[i for i in range(16)]

fig=plt.figure(figsize=(10,10),dpi=200)  #��������
plt.bar(x,height=air_mean, color="grey", edgecolor="black")

plt.xticks([0,2,4,6,8,10,12,14],['1000','850','600','400','250','150','70','30']) #����ÿ�����ѹ
plt.ylabel('Temperature(��C)')
plt.xlabel('Level(hPa)')

plt.title('Monthly Mean of Air temperature',fontsize=15,y=1.05) #��ӱ��⣬�����ֺź�λ��
plt.savefig('C:/Users/LULU/Desktop/Average_temperature_of_each_level.jpg')
plt.show()



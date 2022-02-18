import pandas as pd

#xls文件读写
file1 = r'C:\Users\LULU\Desktop\2.xls'
data1 = pd.read_excel(file1)  #从file1(2.xls)读取data1
print(data1.keys())

print(data1)  #输出data1
print(len(data1))  #输出data1的行数(5行)
print(data1.keys())   #输出data1的每一列的名称（变量名）：Index(['date', 'var1', 'var2'], dtype='object'
print(data1['date'])   #输出data1的某一列

file2 = r'C:\Users\LULU\Desktop\3.xls'
data1.to_excel(file2) #将data1写入file2(3.xls)

#csv文件读写
file3 = r'C:\Users\LULU\Desktop\4.csv'
data2 = pd.read_csv(file3)

file4 = r'C:\Users\LULU\Desktop\5.csv'
data1.to_csv(file4) #将data1写入file4(5.csv)

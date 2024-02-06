import pandas as pd
import openpyxl
import xlrd
import statistics as s
import numpy as np
import math
import random
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


#1
df=pd.read_excel("Lab1\stat.xls",skiprows=6,skipfooter=3)
# print(df.head)
saldo=df["Unnamed: 7"]
names_saldo=df.iloc[:,[0,7]]
# print(saldo.head)
print(names_saldo)
#2
m=saldo.mean()
print("mat", m)
mode=saldo.mode()
print("mode", mode if mode.size<saldo.size else "no mode")
median=s.median(sorted(saldo))
print("median",median)
dysp=s.pvariance(saldo)
print("pvariance",dysp)
pstdev=s.pstdev(saldo)
print("pstdev",pstdev)

#3
gs = GridSpec(1, 3)
fig = plt.figure(figsize=(10, 6))



def hui(plot_column_num:int,column_dict_name:str,column_dict_num:int,x_label:str,label:str,multiplier=1.0):
    ax=fig.add_subplot(gs[0,plot_column_num])
    cities_data=df.iloc[:,[0,column_dict_num]]
    cities_data_hist=cities_data.to_dict('list')
    ys=cities_data_hist[column_dict_name]
    if(multiplier!=1.0):
        temp=[]
        for i in cities_data_hist[column_dict_name]:
            temp.append(i*multiplier)
        ys=temp
    ax.bar(cities_data_hist['у тому числі'],ys)
    ax.set_xticklabels(cities_data_hist['у тому числі'], rotation=90)
    yticks=np.linspace(round(min(ys),2),round(max(ys),3),num=5)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticks)
    ax.set_xlabel(x_label)
    ax.set_title(label)
    ax.grid(axis='y')
    return ax


# Сальдо - гістрограма
hui(0,'Unnamed: 7',7,'Міста','Сальдо, млрд. долл',10e-7)

# експорт - гістрограма
hui(1,'Unnamed: 1',1,'Міста','Експорт, млрд. долл',10e-7)

# Імпорт - гістрограма
hui(2,'Unnamed: 4',4,'Міста','Імпорт, млрд. долл',10e-7) 

# cities_hist=names_saldo.to_dict('list')

# ax1 = fig.add_subplot(gs[0, 0])
# ax1.bar(cities_hist['у тому числі'],cities_hist['Unnamed: 7'])


# ax1.set_xticklabels(cities_hist['у тому числі'], rotation=90)
# ax1.set_xlabel('Міста')
# ax1.set_ylabel('Сальдо, 10 млрд. долл')

# Експорт

cities_export=df.iloc[:,[0,1]]
print(cities_export)

plt.show()
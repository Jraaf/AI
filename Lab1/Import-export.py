import pandas as pd
import openpyxl
import xlrd
import statistics as s
import numpy as np
import math
import random
import seaborn as sns
import matplotlib.pyplot as plt
import num3 as n3
from matplotlib.gridspec import GridSpec


#1
df=pd.read_excel("stat.xls",skiprows=6,skipfooter=3)
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
gs = GridSpec(1, 5)
fig = plt.figure(figsize=(10, 6))



def hui(plot_column_num:int, column_dict_name:str, column_dict_num:int, x_label:str, label:str, multiplier=1.0):
    ax = fig.add_subplot(gs[0, plot_column_num])
    cities_data = df.iloc[:, [0, column_dict_num]]
    cities_data_hist = cities_data.to_dict('list')
    ys = cities_data_hist[column_dict_name]
    if multiplier != 1.0:
        temp = []
        for i in cities_data_hist[column_dict_name]:
            temp.append(i * multiplier)
        ys = temp
    # Change to horizontal bar plot
    ax.barh(cities_data_hist['у тому числі'], ys)
    # Adjusting the x and y labels since we're flipping the orientation
    ax.set_yticklabels(cities_data_hist['у тому числі'], rotation=0)  # Assuming you want the 'у тому числі' as y labels now
    xticks = np.linspace(round(min(ys), 2), round(max(ys), 3), num=5)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks,rotation=90)
    ax.set_ylabel(x_label)  # Now it's the y label since we flipped the axes
    ax.set_title(label)
    ax.grid(axis='x')  # Grid lines now should be along the x-axis
    return ax



# Сальдо - гістрограма
hui(0,'Unnamed: 7',7,'Міста','Сальдо, млрд. долл',10e-7)

# експорт - гістрограма
hui(2,'Unnamed: 1',1,'Міста','Експорт, млрд. долл',10e-7)

# Імпорт - гістрограма
hui(4,'Unnamed: 4',4,'Міста','Імпорт, млрд. долл',10e-7) 

# 3
df.index = [df["у тому числі"]]
df = df.iloc[:, 1:7]

print(df)

n3.do_dataframe(df=df,num_of_cloumn=1,num_of_row_start=1,num_of_row_end=15)
# df.at
plt.show()
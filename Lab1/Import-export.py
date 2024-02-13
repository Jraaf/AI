import pandas as pd
import statistics as s
import numpy as np
import matplotlib.pyplot as plt
import num4 as n4
from matplotlib.gridspec import GridSpec
import os

#1
df=pd.read_excel("stat.xls",skiprows=6,skipfooter=3)
saldo=df["Unnamed: 7"]
names_saldo=df.iloc[:,[0,7]]

print('-----------------Сальдо по областям України за 2023 рік--------------------')
print(names_saldo)

#2
print('-----------------Статистика по сальдо--------------------')
mean = saldo.mean()
print("mean", mean)
mode = saldo.mode()
print("mode", mode if mode.size < saldo.size else "no mode")
median = s.median(sorted(saldo))
print("median",median)
dysp = s.pvariance(saldo)
print("pvariance",dysp)
std = s.pstdev(saldo)
print("std",std)

#3
gs = GridSpec(1, 5)
fig = plt.figure(figsize=(10, 6))
def print_this_sheet(plot_column_num:int, column_dict_name:str, column_dict_num:int, x_label:str, label:str, multiplier=1.0):
    ax = fig.add_subplot(gs[0, plot_column_num])
    cities_data = df.iloc[:, [0, column_dict_num]]
    cities_data_hist = cities_data.to_dict('list')
    ys = cities_data_hist[column_dict_name]
    if multiplier != 1.0:
        temp = []
        for i in cities_data_hist[column_dict_name]:
            temp.append(i * multiplier)
        ys = temp
    ax.barh(cities_data_hist['у тому числі'], ys)
    ax.set_yticklabels(cities_data_hist['у тому числі'], rotation=0)
    xticks = np.linspace(round(min(ys), 2), round(max(ys), 3), num=5)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks,rotation=90)
    ax.set_ylabel(x_label)
    ax.set_title(label)
    ax.grid(axis='x')
    return ax

# Сальдо - гістрограма
print_this_sheet(0,'Unnamed: 7',7,'Міста','Сальдо, млрд. долл',10e-7)

# експорт - гістрограма
print_this_sheet(2,'Unnamed: 1',1,'Міста','Експорт, млрд. долл',10e-7)

# Імпорт - гістрограма
print_this_sheet(4,'Unnamed: 4',4,'Міста','Імпорт, млрд. долл',10e-7)

plt.show()

# 4
print('\n----------------------------------------------------')
print('-----------------Колекція Series--------------------')
print('----------------------------------------------------\n')
n4.do_series(df)

df.index = [df["у тому числі"]]
df = df.iloc[:, 1:7]

print('\n-------------------------------------------------------')
print('-----------------Колекція DataFrame--------------------')
print('-------------------------------------------------------\n')
n4.do_dataframe(df=df,num_of_cloumn=1,num_of_row_start=1,num_of_row_end=15)
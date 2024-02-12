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

# 8
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')

# 9
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']

print(titanic)

# 10
youngest = titanic.loc[titanic['age'].idxmin()]
eldest = titanic.loc[titanic['age'].idxmax()]
average = titanic['age'].mean()

first_class_women = titanic[(titanic['sex'] == 'female') & (titanic['class'] == '1st')].sort_values(by='name')
youngest_fcw = first_class_women.loc[first_class_women['age'].idxmin()]
eldest_fcw = first_class_women.loc[first_class_women['age'].idxmax()]
count_survived = first_class_women[first_class_women['survived'] == 'yes'].shape[0]

print("###################################################################"
      "\nyoungest person:\n", youngest)
print("###################################################################"
      "\neldest person:\n", eldest)
print("###################################################################"
      "\naverage age: ", average)
print("###################################################################"
      "\nwomen: \n", first_class_women)
print("###################################################################"
      "\nyoungest women of 1st class: \n", youngest_fcw)
print("###################################################################"
      "\neldest women of 1st class: \n", eldest_fcw)
print("###################################################################"
      "\nquantity of survived women of 1st class: ", count_survived)

#11
titanic.hist()
plt.xlabel("Вік пасажирів")
plt.ylabel("Частота")
plt.show()
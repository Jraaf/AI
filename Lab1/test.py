import num4 as n4
import pandas as pd


df=pd.read_excel("stat.xls",skiprows=6,skipfooter=3)
n4.do_series(df)
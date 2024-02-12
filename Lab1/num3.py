import pandas as pd

def do_dataframe(df:pd.DataFrame,num_of_cloumn:int,num_of_row_start:int,num_of_row_end:int):
    print('-----------------Зернення до колонки--------------------')
    print(df[f'Unnamed: {num_of_cloumn}'])
    # print(df.loc[''])
    df=df.rename(columns={'Unnamed: 1':'|у тому числі|',
                          'Unnamed: 2':'|експорт, тис USD|',
                          'Unnamed: 3':'|експорт у % до 2022|',
                          'Unnamed: 4':'|експорт у % до загального|', 
                          'Unnamed: 5':'|імпорт, тис USD|',
                          'Unnamed: 6':'|імпорт у % до 2022|',
                          'Unnamed: 7':'|імпорт % до загального|'})
    print('------------------Звернення до стовпців-----------------------')
    print(df.iloc[num_of_row_start])
    print('------------------Вібір підмножини-----------------------')
    print(df.iloc[num_of_row_start:num_of_row_end])
    print('------------------Логічне індексування-----------------------')
    print(df[df>=45])
    print('------------------Звернення до конкретного осередку[4,5]-----------------------')
    print(df.iat[4,5])
    print('------------------Описова статистика-----------------------')
    print(df.describe())
    print('------------------Траноспонування-----------------------')
    print(df.T)
    print('------------------Сортування рядків за індексами (спадання)-----------------------')
    print(df.sort_index(ascending=False))
    print('------------------Сортування стовпців за індексами (спадання)-----------------------')
    print(df.sort_index(ascending=False,axis=1))

import pandas as pd

def do_dataframe(df:pd.DataFrame,num_of_cloumn:int,num_of_row_start:int,num_of_row_end:int):
    print('-----------------------------------------')
    print(df[f'Unnamed: {num_of_cloumn}'])
    # print(df.loc[''])

    print(df.iloc[num_of_row_start])
    print('-----------------------------------------')
    print(df.iloc[num_of_row_start:num_of_row_end])
    print('-----------------------------------------')
    print(df.iloc[[num_of_row_start,num_of_row_end]])
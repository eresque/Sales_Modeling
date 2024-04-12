import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

def getInfo(date: datetime.date = '2023-07-02'):
    df=pd.read_csv("data/df.csv")
    df['Начало нед'] = pd.to_datetime(df['Начало нед'])
    user_inp=pd.to_datetime(date)
    print(type(df['Начало нед']))
    print(type(user_inp))
    filtered_df = df[df['Начало нед'] <= user_inp]
    sorted_df = filtered_df.sort_values(by='Начало нед', ascending=False)
    closest_date = sorted_df.iloc[0]['Начало нед']
    index = df[df['Начало нед'] == closest_date].index[0]
    next_28_rows = df.iloc[index:index+28]
    print(next_28_rows)


getInfo('2023-07-03')
import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

def getInfo(date: datetime.date = '2023-07-02'):
    df=pd.read_csv("backhack/data/df.csv")
    nearest_previous_date=[]
    for data in df['Начало нед']:
        if data<=date:
            nearest_previous_date.append(data)
    row_index = df[df['Начало нед'] == nearest_previous_date[-1]].index[0]
    next_28_rows = df.iloc[row_index:row_index+28]
    print(next_28_rows)


getInfo('2023-07-03')
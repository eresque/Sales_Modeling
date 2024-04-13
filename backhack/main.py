from fastapi import FastAPI, File, UploadFile
import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import joblib
import os

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5173'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "I'm working!"}

@app.post("/main")
def getInfo(date: datetime.date = '2023-07-02', file: UploadFile = None):
    fileinfo="no file"
    output=""
    if file is not None:
        try:
            contents = file.file.read()
            print(contents)
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            fileinfo="there was an error uploading file"
        finally:
            file.file.close()
            fileinfo = f"Successfuly uploaded {file.filename}"
    df=pd.read_csv("./data/df.csv")
    df['Начало нед'] = pd.to_datetime(df['Начало нед'])
    user_inp=pd.to_datetime(date)
    filtered_df = df[df['Начало нед'] <= user_inp]
    sorted_df = filtered_df.sort_values(by='Начало нед', ascending=False)
    closest_date = sorted_df.iloc[0]['Начало нед']
    index = df[df['Начало нед'] == closest_date].index[0]
    next_28_rows = df.iloc[index:index+28]
    rf_model = joblib.load("./model/rf_100.joblib")
    non_numerical_columns = next_28_rows.select_dtypes(exclude=['number']).columns.tolist()

    non_numeric_features = []

    for col in non_numerical_columns:
        non_numeric_features.append(col)

    output = rf_model.predict(next_28_rows.drop(non_numeric_features, axis=1).drop('Продажи, рубли', axis=1))
    curf=[]
    cwd=os.getcwd()
    curf=os.listdir(cwd)
    print(curf)
    os.remove(file.filename)
    curf=os.listdir(cwd)
    print(curf)   
    return {"message":{"outp":str(output), "file": fileinfo}}

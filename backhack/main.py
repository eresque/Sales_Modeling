from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import os
import plotly.express as px
import zipfile

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


def getgraphs():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    df = df.loc[(df["Date"] >= "2016-07-01") & (df["Date"] <= "2016-12-01")]

    fig = px.line(df, x='Date', y='AAPL.High')
    fig.update_xaxes(ticks="outside",
                     ticklabelmode="period",
                     tickcolor="black",
                     ticklen=10,
                     minor=dict(
                         ticklen=4,
                         dtick=7 * 24 * 60 * 60 * 1000,
                         tick0="2016-07-03",
                         griddash='dot',
                         gridcolor='white')
                     )
    fig.write_image('pictures/linear.png')


def zipfiles(directory):
    # Define the path to the directory containing the files

    # Create a ZipFile object to write to a new zip file
    with zipfile.ZipFile('output.zip', 'w') as zipf:
        # Iterate over all the files in the directory
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Add each file to the zip archive
                zipf.write(file_path, arcname=os.path.relpath(file_path, directory))


@app.post("/main")
def getInfo(date: datetime.date = '2023-07-02', file: UploadFile = None):
    fileinfo = "no file"
    output = ""
    if file is not None:
        try:
            contents = file.file.read()
            print(contents)
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            fileinfo = "there was an error uploading file"
        finally:
            file.file.close()
            fileinfo = f"Successfuly uploaded {file.filename}"
    df = pd.read_csv("./data/df.csv")
    df['Начало нед'] = pd.to_datetime(df['Начало нед'])
    user_inp = pd.to_datetime(date)
    filtered_df = df[df['Начало нед'] <= user_inp]
    sorted_df = filtered_df.sort_values(by='Начало нед', ascending=False)
    closest_date = sorted_df.iloc[0]['Начало нед']
    index = df[df['Начало нед'] == closest_date].index[0]
    next_28_rows = df.iloc[index:index + 28]
    rf_model = joblib.load("./model/rf_100.joblib")
    non_numerical_columns = next_28_rows.select_dtypes(exclude=['number']).columns.tolist()

    non_numeric_features = []

    for col in non_numerical_columns:
        non_numeric_features.append(col)

    output = rf_model.predict(next_28_rows.drop(non_numeric_features, axis=1).drop('Продажи, рубли', axis=1))
    getgraphs()
    
    if file is not None:
        os.remove(file.filename)
    zipfiles('pictures')
    return FileResponse(path='output.zip',media_type='application/octet-stream', filename='output.zip')

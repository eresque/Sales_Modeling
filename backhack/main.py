from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import os
import plotly.express as px
import zipfile
import shap
import matplotlib.pyplot as plt

app = FastAPI()

origins = [
    'http://5.35.29.99:5173',
    'http://5.35.29.99:3000',
    'http://5.35.29.99:8000',
    'http://5.35.29.99',
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


def getgraphs(df, model, non_numeric_features):
    
    fig = px.line(df, x='Начало нед', y='Продажи, рубли')
    fig.update_xaxes(ticks="outside",
                     ticklabelmode="period",
                     tickcolor="black",
                     ticklen=10,
                     minor=dict(
                         ticklen=4,
                         dtick=7 * 24 * 60 * 60 * 1000,
                         griddash='dot',
                         gridcolor='white')
                     )
    fig.write_image('files/linear.png')
    
    df=df.drop(non_numeric_features, axis=1)
    
    # explain the model's predictions using SHAP
    # (same syntax works for LightGBM, CatBoost, `scikit-learn, transformers, Spark, etc.)
    explainer = shap.Explainer(model)
    shap_values = explainer(df.drop('Продажи, рубли', axis=1))
    
    # visualize the first prediction's explanation
    
    fig = shap.plots.waterfall(shap_values[0],show=False)
    plt.tight_layout()
    plt.savefig('files/scratch.png')



@app.get("/getFile")
def getFile(path:str="filename"):
    return FileResponse(f"files/{path}")

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
    next_28_rows['Продажи, рубли']=output
    next_28_rows.to_excel("files/prediction.xlsx", index=False)

    getgraphs(next_28_rows, rf_model, non_numeric_features)
    
    if file is not None:
        os.remove(file.filename)
    file_names = []
    
    # Check if the folder path exists
    if os.path.exists('files'):
        # Iterate over all files in the folder
        for file_name in os.listdir('files'):
            # Check if the path is a file (not a directory)
            if os.path.isfile(os.path.join('files', file_name)):
                file_names.append(file_name)
    return {"files": file_names}

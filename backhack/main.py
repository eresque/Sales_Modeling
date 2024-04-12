from fastapi import FastAPI, File, UploadFile
import datetime
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import joblib

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

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        print(contents)
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "there was an error uploading file"}
    finally:
        file.file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}

@app.get("/main")
def getInfo(date: datetime.date = '2023-07-02'):
    df=pd.read_csv("./data/df.csv")
    rf_model = joblib.load("./model/rf_100.joblib")
    non_numerical_columns = df.select_dtypes(exclude=['number']).columns.tolist()

    non_numeric_features = []

    for col in non_numerical_columns:
        non_numeric_features.append(col)

    output = rf_model.predict(df.drop(non_numeric_features, axis=1).drop('Продажи, рубли', axis=1))
    return {"message":str(output)}

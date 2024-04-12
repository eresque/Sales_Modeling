from fastapi import FastAPI, File, UploadFile
import datetime
from fastapi.middleware.cors import CORSMiddleware

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
def getInfo(date: datetime.date = '27.03.2023'):
    return {"message":"test_data_worked"}

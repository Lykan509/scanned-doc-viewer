
from fastapi import FastAPI, Depends
SECRET_KEY = "your-secure-secret-key"
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Advanced API with Auth, OCR, and Search"}

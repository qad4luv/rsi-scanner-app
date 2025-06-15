from fastapi import FastAPI
from scan import scan_handler

app = FastAPI()

@app.get("/")
def root():
    return scan_handler()

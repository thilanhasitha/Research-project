from fastapi import FastAPI
import logging
import sys



app = FastAPI()


@app.get('/')
def root():
    return {"message":"Backend API is running"}

@app.get('/api/test')
def test():
    return {"message":"FastAPI is running successfully"}




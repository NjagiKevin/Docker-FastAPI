from fastapi import FastAPI
from os import environ as env 


app=FastAPI()

@app.get("/")
def greet():
    return {"details": f"Hello World! Secret = {env['MY_VARIABLE']}"}
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return { "message": "FastAPI! Though, as you can see - it has changed!" }
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return { "message": "FastAPI! Further revisions, working with git branches." }
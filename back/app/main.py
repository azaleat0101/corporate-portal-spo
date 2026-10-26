from fastapi import FastAPI

app = FastAPI(title="Corporate Portal API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend works!"}
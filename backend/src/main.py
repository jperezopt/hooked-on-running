from fastapi import FastAPI

app = FastAPI(title="Hooked on Running API")

@app.get("/")
def read_root():
    return {"message": "hello user"}

@app.get("/nums")
def read_num():
    return {"message": 1}

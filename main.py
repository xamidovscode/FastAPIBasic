from fastapi import FastAPI

app = FastAPI()


@app.get("/admin/")
def get_hello():
    return "Hello World"



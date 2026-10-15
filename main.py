from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"Hello Kamran"}

@app.get("/about")
def about():
    return{"This is About Page"}

@app.get("/users")
def about():
    return{"Users" : {
        "Ali",
        "Ahmad",
        "Kamran"
    }}

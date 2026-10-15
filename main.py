from fastapi import FastAPI

app = FastAPI()

# Simple get Routes Examples

# @app.get("/")
# def home():
#     return{"Hello Kamran"}

# @app.get("/about")
# def about():
#     return{"This is About Page"}

# @app.get("/users")
# def about():
#     return{"Users" : {
#         "Ali",
#         "Ahmad",
#         "Kamran"
#     }}


# Path Parameters

# @app.get("/users/{user_id}")
# def get_users(user_id:int):
#     return {"User_Id" : user_id}

# Query Parameters

@app.get("/students")
def get_age(age:int = 20 , name : str = None):
    return {
        "Name" :name,
        "Age" : age,
         }
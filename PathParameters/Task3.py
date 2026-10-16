# Task 3 — Student Age Validator 
# Goal: Create a new endpoint that checks whether a student is old enough to enter a course.
# Requirements
# 1. Create a GET route: /student-age/{age}
# 2. Accept age as an integer path parameter.
# 3. If age is 18 or above, return {"message": "Eligible"}.
# 4. If age is below 18, return {"message": "Not eligible"}.

from fastapi import FastAPI

app = FastAPI()

@app.get("/student_age/{age}")
def get_age(age : int):
    if (age >= 18):
        return{
            "message": "Eligible"
        }
    elif (age < 18):
        return{
            "message": "Not Eligible"
        }
# Goal: Create an API that returns information about a student based on their ID.


# Requirements
# 1. Create a FastAPI route that accepts a student ID from the URL.
# 2. The student ID must be an integer.
# 3. If the ID is 1, return the student's name as "Ali".
# 4. If the ID is 2, return the student's name as "Ahmed".
# 5. For any other ID, return a message saying "Student not found".


from fastapi import FastAPI

app = FastAPI()

@app.get("/student/{student_id}")
def get_student(student_id : int):
        if(student_id == 1):
            return{"name" : "Ali"}
        elif (student_id == 2):
            return{"name" : "Ahmed"}
        else:
            return{"message" : "Student not found"}

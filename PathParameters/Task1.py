# Task 1: Path Parameter

# Problem: Create a GET route /courses/{course_id}.

# Requirements:

# course_id must be an integer.
# The route returns a JSON object with two keys: course_id (the value from the URL) and title (always the text "Python Basics").


from fastapi import FastAPI

app = FastAPI()

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {
        "course_id": course_id,
        "title": "Python Basics",
    }

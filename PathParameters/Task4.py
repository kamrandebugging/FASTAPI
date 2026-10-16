# Task 4 — Positive, Negative, or Zero 
# Let's level up slightly. This time, you'll practice multiple conditions.
# Goal: Create a FastAPI endpoint that identifies whether a number is positive, negative, or zero.
# Requirements
# 1. Create a GET route: /number/{value}
# 2. Accept value as an integer path parameter.
# 3. If the number is greater than zero, return {"result": "Positive"}.
# 4. If the number is less than zero, return {"result": "Negative"}.
# 5. If the number equals zero, return {"result": "Zero"}.

from fastapi import FastAPI

app = FastAPI()

@app.get("/number/{value}")
def get_value(value : int):
    if (value > 0):
        return{
            "result": "Positive"
        }
    elif (value < 0):
        return{
            "result": "Negative"
        }
    elif (value == 0):
        return{
            "result": "Zero"
        }
    else:
        return{
            "result": "Not a Number"
        }
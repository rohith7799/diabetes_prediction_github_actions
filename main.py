import json
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines the structure of the JSON request body.
# BaseModel ensures that the API receives valid input types.
# Each attribute represents a medical feature used for diabetes prediction.

class ModelInput(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# loading the saved model
diabetes_model = pickle.load(open('trained_model/diabetes_model.pkl', 'rb'))

@app.post('/diabetes_prediction')

# input_parameters is a variable that stores the health information provided by a user.
# It is an object of the ModelInput class.
# This means input_parameters has all the attributes (fields) from ModelInput, like pregnancies, Glucose, BloodPressure, etc.

def diabetes_pred(input_parameters: ModelInput):

    preg = input_parameters.pregnancies
    glu = input_parameters.Glucose
    bp = input_parameters.BloodPressure
    skin = input_parameters.SkinThickness
    insulin = input_parameters.Insulin
    bmi = input_parameters.BMI
    dpf = input_parameters.DiabetesPedigreeFunction
    age = input_parameters.Age

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        result = {"label": 0,
                  "result": "The person is not diabetic"}
        return result
    else:
        result = {"label": 1,
                  "result": "The person is diabetic"}
        return result

# to run, type the command in terminal : uvicorn main:app  (main is the file name and app is the instance of fastapi application)

# syntax = uvicorn filename:app_instance --host 0.0.0.0 --port port_number --reload
# eg =     uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# if file is in other location then : uvicorn app_folder.main:app --host 0.0.0.0 --port 8000 --reload
# uvicorn folder_name.filename:app_instance --host 0.0.0.0 --port port_number --reload

# you can run a FastAPI application using the Python command.you have to add 
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#     uvicorn.run("<module_name or file_name>:<app_instance>", host="0.0.0.0", port=<port_number>, reload=True)
# <module_name> → The name of your Python file without .py.
# <app_instance> → The FastAPI object (usually app).
# <port_number> → The port number (default is 8000).
# cmd = python app_folder/main.py

# docker_venv\Scripts\activate
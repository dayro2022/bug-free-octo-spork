from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

#from typing import List




app = FastAPI()



class Student(BaseModel):

    id: str

    name: str

    lastname: str

    #skills: List[str] = []



students = []





@app.get("/estudiantes")

def get_students():

    return students



@app.get("/estudiantes/{id}")

def get_student(id: str):

    for student in students:

        if student["id"] == id:

            return student

    return "No existe el estudiante"



@app.post("/estudiantes")

def save_student(student: Student):

    student.id = str(uuid4())

    students.append(student.dict())

    return "Estudiante registrado"



@app.put("/estudiantes/{id}")

def update_student(updated_updated: Student, id:str):

    for student in students:

        if student["id"] == id:

            student["name"] = updated_updated.name

            student["lastname"] = updated_updated.lastname

            #student["skills"] = updated_updated.skills

            return "Estudiante modificado"

    return "No existe el estudiante"


@app.delete("/estudiantes/{id}")
def delete_student(id: str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "estudiante eliminado"
    return "No existe el estudiante"
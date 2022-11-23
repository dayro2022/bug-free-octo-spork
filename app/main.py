from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

#from typing import List




app = FastAPI()




class Envio(BaseModel):

    id: str

    name: str

    lastname: str

    Ciudad: str


    #skills: List[str] = []



envios = []





@app.get("/enviados")

def get_envios():

    return envios



@app.get("/enviados/{id}")

def get_envios(id: str):

    for send in envios:

        if send["id"] == id:

            return send

    return "No existe el envio"



@app.post("/envio")

def save_envio(send: Envio):

    send.id = str(uuid4())

    envios.append(send.dict())

    return "envio registrado"



@app.put("/modificar envio/{id}")

def update_envio(updated_updated: Envio, id:str):

    for send in envios:

        if send["id"] == id:

            send["name"] = updated_updated.name

            send["lastname"] = updated_updated.lastname

            #student["skills"] = updated_updated.skills

            return "Envio modificado"

    return "No existe el envio"


@app.delete("/envio/{id}")
def delete_envio(id: str):
    for send in envios:
        if send["id"] == id:
            envios.remove(send)
            return "envio eliminado"
    return "No existe el envio"
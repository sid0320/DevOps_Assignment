from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/Home")
def read_root():
    return {"Hello": "World"}

@app.get("/About")
def about():
    return{"Msg":"About us"}

@app.get("Contact-Us")
def contact_us():
    return {"Email":"abc@gmail.com","Mob_no.":"1234567890"}

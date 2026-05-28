from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    tittle: str
    body: str


@app.post("/blog")
def Create(title,body):
    return {'title': title, 'body': body}

from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas, models
from database import engine
import uvicorn

app = FastAPI()


#Models database
models.Base.metadata.create_all(engine )


class Blog(BaseModel):
    tittle: str
    body: str


@app.post("/blog")
def Create(request: Blog):
    return {
        'title': request.tittle, 
        'body': request.body
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

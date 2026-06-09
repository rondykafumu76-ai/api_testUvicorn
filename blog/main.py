from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


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

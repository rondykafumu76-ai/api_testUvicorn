from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()



@app.get("/blog")
def read_item(limit=10,published:bool=True,sort: Optional[str]=None):
    if published:
        return {
            "data": f"{limit} published blogs from the db"
        }
    else:
        return {
            "data": f"{limit} blogs from the db"
        }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blogModel")
def read_item(blog:Blog):
    
    return {
        "Name": f"Blog is created with title as {blog.title}",
        "body": f"Blog is created with body as {blog.body}",
        "published": f"Blog is created with published as {blog.published}"
    }

@app.get("/hello/{id}")
def read_item(id):
    return {
        "data": 
            {
                "id":id
            }
            
    }

@app.get("/hello/{id}/commets/")
def read_item(id:int):
    return {
        "data": 
            {
                "1","2"
            }
            
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

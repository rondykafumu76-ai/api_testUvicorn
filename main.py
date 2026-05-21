from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_item():
    return {"data": 
            {
                "name":"sarthak"
                }
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
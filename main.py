from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_item():
    return {"data": 
            {
                "name":"sarthak"
                }
            }

@app.get("/hello")
def read_item():
    return {"data": 
            {
                "name":"rondy"
                }
            }
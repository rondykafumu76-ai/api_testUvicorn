from fastapi import FastAPI

app = FastAPI()



@app.get("/blog")
def read_item(limit,published):

    if published == False:
        return {"data": 
                {
                    "name":f'{limit} sarthak'
                }
            }
    elif published == True:
        return {'data':"error"}

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
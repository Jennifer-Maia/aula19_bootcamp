from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Se adiciono decoradores do fastapi ele transforma minha função em uma API
@app.get("/") 
def read_root():
    return {"Hello": "World"}

@app.get("/jornada") #Posso criar qualquer api apenas passando o "@app.get("/")"
def read_jornada():
    return {"Nossa primeira": "API"}

@app.get("/items/{item_id}") #Posso fazer com variáveis
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}") # pydantic, mkdocs, uvicorn, api
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# Para rodar usamos o uvicorn: uvicorn + nome do arquivo + : + nome da instancia criada + --reload (pra sempre que fizer uma 
  #alteração ele renderiza automaticamente). Nesse caso ficaria: uvicorn main:app --reload

# Sempre que eu tenho uma API meu objetivo é retornar alguma coisa através de um path
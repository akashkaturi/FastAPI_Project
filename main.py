from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()


class Item(BaseModel):
    id:int
    name:str 
    age:int 
    salary:Optional[int]
    phone:int
    

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def get_unpublished():
    return {'data':'unpublished'}


@app.get('/allblogs')
def display_blogs(limit=10, sort:Optional[str]=None,published:bool=True):
    if published:    
        return {'data':f'Displaying published blogs which are sorted in {sort} order'}
    else:
        return {'data': f'Diplsaying all blogs which are sorted in {sort} order'}

@app.get('/blog/{id}')
def show_blog(id:int):
    return {'data': id}




@app.get('/blog/{id}/comment')
def show_comments(id:int):
    return {'data':f'comments of {id}'}


@app.post('/postblog')
def post_blog(item:Item):
    return {'data':f'name: {item.name}'}


if __name__=='__main__':
    uvicorn.run(app,port=9000)
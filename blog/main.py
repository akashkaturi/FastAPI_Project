"""
main app
"""
from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
import blog.models as models
import blog.schemas as schemas
from .db import engine, getdata_base
from blog.encryption import hash_password
from .routers import blog, user, login

app = FastAPI()

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(bind=engine)


# def getdata_base():
#     data_base = SessionLocal()
#     try:
#         yield data_base
#     finally:
#         data_base.close()


# @app.post('/blogs', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def index(request: schemas.Blog, data_base: Session = Depends(getdata_base)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     data_base.add(new_blog)
#     data_base.commit()
#     data_base.refresh(new_blog)
#     return new_blog

#
# @app.get('/viewblogs', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def get_blogs(data_base: Session = Depends(getdata_base)):
#     blogs = data_base.query(models.Blog).all()
#     return blogs
#
#
# @app.get('/blog/{id}', status_code=status.HTTP_200_OK,
#          response_model=schemas.ShowBlog, tags=['blogs'])
# def get_blog(id: int, response: Response, data_base: Session = Depends(getdata_base)):
#     blog = data_base.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'message': f'Blog with {id} not found'}
#     return blog
#
#
# @app.delete('/delete/{id}', status_code=status.HTTP_200_OK, tags=['blogs'])
# def delete_blog(id: int, data_base: Session = Depends(getdata_base)):
#     blog = data_base.query(models.Blog).filter(models.Blog.id == id)
#
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} is not found")
#     blog.delete(synchronize_session=False)
#     data_base.commit()
#     return {'deleted': blog}
#
#
# @app.put('/editblog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update_blog(id: int, new_blog: schemas.UpdateBlog, data_base: Session = Depends(getdata_base)):
#     blog = data_base.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} is not found")
#     blog.update(new_blog.dict())
#     data_base.commit()
#     return status.HTTP_202_ACCEPTED

#
# @app.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'], response_model=schemas.ShowUser)
# def index(request: schemas.User, data_base: Session = Depends(getdata_base)):
#     new_blog = models.User(
#         name=request.name, email=request.email, password=hash_password(request.password))
#     data_base.add(new_blog)
#     data_base.commit()
#     data_base.refresh(new_blog)
#     return new_blog
#
#
# @app.get('/users', response_model=List[schemas.ShowUser], tags=['users'])
# def get_users(data_base: Session = Depends(getdata_base)):
#     users = data_base.query(models.User).all()
#     return users
#
#
# @app.get('/user/{id}', tags=['users'], status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
# def user(id: int, data_base: Session = Depends(getdata_base)):
#     new_user = data_base.query(models.User).filter(models.User.id == id).first()
#     if not new_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return new_user

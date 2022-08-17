from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from .. import schemas, models, oauth2
from sqlalchemy.orm import Session
from ..db import getdata_base
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def index(request: schemas.Blog, data_base: Session = Depends(getdata_base),
          get_c: schemas.User = Depends(get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    data_base.add(new_blog)
    data_base.commit()
    data_base.refresh(new_blog)
    return new_blog


@router.get('/', response_model=List[schemas.ShowBlog])
def get_blogs(data_base: Session = Depends(getdata_base), get_c: schemas.User = Depends(get_current_user)):
    blogs = data_base.query(models.Blog).all()
    return blogs


@router.get('/{id}', status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def get_blog(id: int, response: Response, data_base: Session = Depends(getdata_base),
             get_c: schemas.User = Depends(get_current_user)):
    blog = data_base.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog with {id} not found'}
    return blog


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int, data_base: Session = Depends(getdata_base), get_c: schemas.User = Depends(get_current_user)):
    blog = data_base.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not found")
    blog.delete(synchronize_session=False)
    data_base.commit()
    return {'deleted': blog}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, new_blog: schemas.UpdateBlog, data_base: Session = Depends(getdata_base),
                get_c: schemas.User = Depends(get_current_user)):
    blog = data_base.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not found")
    blog.update(new_blog.dict())
    data_base.commit()
    return status.HTTP_202_ACCEPTED

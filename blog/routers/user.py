from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..db import getdata_base
from .. import schemas, models
from ..encryption import hash_password

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def index(request: schemas.User, data_base: Session = Depends(getdata_base)):
    new_blog = models.User(
        name=request.name, email=request.email, password=hash_password(request.password))
    data_base.add(new_blog)
    data_base.commit()
    data_base.refresh(new_blog)
    return new_blog


@router.get('', response_model=List[schemas.ShowUser])
def get_users(data_base: Session = Depends(getdata_base)):
    users = data_base.query(models.User).all()
    return users


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def user(id: int, data_base: Session = Depends(getdata_base)):
    new_user = data_base.query(models.User).filter(models.User.id == id).first()
    if not new_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return new_user

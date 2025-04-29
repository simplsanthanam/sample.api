import psycopg
from .. import utils,schemas,models
from ..database import engine,get_db
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session


router= APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = utils.hash_password(user.password)
    user.password=hashed_pwd
    new_user = models.User(**user.dict())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except psycopg.IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    return new_user

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id: int,db: Session=Depends(get_db)):
    user= db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id:{id} not found")
    print(user)
    return user
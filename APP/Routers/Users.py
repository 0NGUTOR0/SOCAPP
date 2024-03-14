from APP.Database import engine, get_db
from .. import Models, Schemas, Utilities, oauth2
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from sqlalchemy.sql import func
Models.Base.metadata.create_all(bind = engine)

router = APIRouter(
    prefix= "/users",
    tags= ["USERS"]
)
    

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= Schemas.UserResponse)
def create_user(newuser: Schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = Utilities.passwordhasher(newuser.password)
    newuser.password = hashed_password
    new_user = Models.Users(**newuser.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=Schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    user = db.query(Models.Users).filter(Models.Users.id == id).first()
    if user == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"user with id:{id} not found")
    return user
    

@router.get("/", response_model= List[Schemas.UserFollow])
#@router.get("/")
def get_all_users(db: Session = Depends(get_db),
                  current_user:int = Depends(oauth2.get_current_user), limit:int = 6000000000, skip:int =0, search :Optional[str]=""):
    users = db.query(Models.Users).filter(Models.Users.Name.contains(search)).limit(limit).offset(skip).all()
    results = db.query(Models.Users, func.count(Models.Follows.leaders).label("Followers")).join(Models.Follows, Models.Follows.leaders == Models.Users.id, isouter= True).group_by(Models.Users.id).all()
    return results
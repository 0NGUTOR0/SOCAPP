from APP.Database import get_db
from APP import Models, Utilities, oauth2, Schemas
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import oauth2PasswordRequestForm

router = APIRouter(tags=['AUTHENTICATION'])

@router.post("/login", response_model=Schemas.Token)
def login(login:oauth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Models.Users).filter(Models.Users.email == login.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Utilities.verify(login.password, user.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = oauth2.create_access_token (data= {"users_ID":user.id})
    return {"access_token": access_token, "token_type": "bearer"}
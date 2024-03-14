from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import Schemas, Database, Models
from fastapi.security import oauth2PasswordBearer
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .Config import Settings

oauth2_Schema = oauth2PasswordBearer(tokenUrl="login")
SECRET_KEY = Settings.secret_key
ALGORITHM = Settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES =  Settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode (to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(JWtoken:str, credentials_excpetion):
    try:
        payload = jwt.decode(JWtoken, SECRET_KEY, algorithms=[ALGORITHM])
        ID:int =payload.get("users_ID")
        if ID == None :
            raise credentials_excpetion
        token_data = Schemas.Tokendata(ID = id) 
    except JWTError:
        raise credentials_excpetion
    return token_data
    
def get_current_user(JWtoken:str = Depends(oauth2_Schema), 
                     db: Session = Depends(Database.get_db)):
    credentials_excpetion = HTTPException (status_code= status.HTTP_401_UNAUTHORIZED, 
                                          detail= "could'nt validate credentials",
                                          headers={"WWW-Authenticate":"bearer"})
    token = verify_access_token(JWtoken, credentials_excpetion)
    
    user = db.query(Models.Users).filter(Models.Users.id == token.id).first()
    
    return user
    
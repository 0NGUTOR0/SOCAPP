from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_password : str 
    database_hostname : str 
    database_username: str 
    database_name: str 
    database_port: str 
    secret_key : str 
    algorithm: str  
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    
    class Config:
        env_file = ".env"

Settings = Settings()
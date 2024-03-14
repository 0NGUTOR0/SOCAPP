from APP.Database import engine
from .import Models
from fastapi import FastAPI
from .Routers import Follow, Posts, Users, Authentication, Like
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind = engine)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Posts.router)
app.include_router(Users.router)
app.include_router(Authentication.router)
app.include_router(Like.router)
app.include_router(Follow.router)

@app.get("/")
def root():
    return {"message":"TO NEW BEGINNINGS"}
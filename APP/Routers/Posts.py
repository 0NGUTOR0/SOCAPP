import sqlalchemy
from APP.Database import engine, get_db
from .. import Models, Schemas, oauth2
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
Models.Base.metadata.create_all(bind = engine)
from sqlalchemy.sql import func

router = APIRouter(
    prefix= "/posts",
    tags= ["POSTS"]
)
 

@router.get("/", response_model=List[Schemas.PostVoteOut])
def get_all_posts(db: Session = Depends(get_db),
                  current_user:int = Depends(oauth2.get_current_user), limit:int = 10, skip:int =0, search :Optional[str]=""):
    results = db.query(Models.Post, func.count(Models.Likes.post_id).label("Likes")).join(Models.Likes, Models.Likes.post_id==Models.Post.id, isouter=True).group_by(Models.Post.id).filter(Models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    print(results)
    return results
   


@router.post("/", status_code=status.HTTP_201_CREATED,  response_model= Schemas.PostResponse)
def create_posts(newpost: Schemas.PostCreate, db: Session = Depends(get_db), 
                 current_user:int = Depends(oauth2.get_current_user)):
    #current_user = db.query(Models.Users).filter(Models.Users.id == token.id).first()
    print(current_user.id)
    new_post = Models.Post(Poster=current_user.id, **newpost.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=Schemas.PostVoteOut)
def get_one_post(id: int, db: Session = Depends(get_db),
                current_user:str = Depends(oauth2.get_current_user)):
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    results = db.query(Models.Post, func.count(Models.Likes.post_id).label("Likes")).join(Models.Likes, Models.Likes.post_id==Models.Post.id, isouter=True).group_by(Models.Post.id).filter(Models.Post.id == id).first()
    if results == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} unavailable")
    return results


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)
                ,current_user:str = Depends(oauth2.get_current_user)):
    post_query = db.query(Models.Post).filter(Models.Post.id == id)
    post = post_query.first()
    #cursor.execute("""DELETE FROM "POSTS" WHERE "ID"= %s RETURNING *""" ,
    #                (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id:{id} not found")
    if post.Poster != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"how you go delete another man post Oga?")
    post_query.delete(synchronize_session=False)
    db.commit()
    return {'post is gone nigga!'}


@router.put("/{id}", status_code=status.HTTP_201_CREATED,  response_model=Schemas.PostResponse)
def update_post(id:int, updatedpost: Schemas.PostCreate, db: Session = Depends(get_db),
                 current_user:str = Depends(oauth2.get_current_user)):
   
   
    

    # This only works this way and i dont know why. Why does the .first method have to be called on a separate line and call that variable post
    
    post_query = db.query(Models.Post).filter(Models.Post.id == id)
    post=post_query.first()
    
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found")
    if post.Poster != current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"how you go update another man post Oga?")
    post_query.update (updatedpost.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
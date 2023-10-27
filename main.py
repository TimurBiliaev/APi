from fastapi import Depends, FastAPI, Body
from database import *
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return "Test API"


@app.get("/api/groups")
def get_all_groups(db: Session = Depends(get_db)):
    return db.query(group).all()


@app.get("/api/groups/{id}")
def get_group(id, db: Session = Depends(get_db)):
    Group = db.query(group).filter(group.group_id == id).first()
    if Group == None:
        return "This group is None"
    return Group
    

@app.post("/api/groups")
def create_person(data  = Body(), db: Session = Depends(get_db)):
    Group = group(group_id=data["group_id"], group_name=data["group_name"], avaliable_lessons=data["avaliable_lessons"])
    db.add(Group)
    db.commit()
    db.refresh(Group)
    return Group    


@app.delete("/api/groups/{id}")
def delete_group(id, db: Session = Depends(get_db)):
    Group = db.query(group).filter(group.group_id == id).first()
    if Group == None:
        return "Thhis group is none"
    db.delete(Group)
    db.commit()
    return "DELETE sucksesful"



@app.put("/api/groups")
def edit_group(data  = Body(), db: Session = Depends(get_db)):
   
    
    Group = db.query(group).filter(group.group_id == data["group_id"]).first()
    
    if Group == None: 
        return JSONResponse(status_code=404, content={ "message": "Group is NONE"})
    
    Group.avaliable_lessons = data["avaliable_lessons"]
    Group.group_name = data["group_name"]
    db.commit() 
    db.refresh(Group)
    return "sucsesful"



@app.get("/api/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(user).all()


@app.get("/api/users/{id}")
def get_user(id, db: Session = Depends(get_db)):
    User = db.query(user).filter(user.user_id == id).first()
    if User == None:
        return "This user us none"
    return User

@app.post("/api/user")
def add_user(data = Body(), db: Session = Depends(get_db)):
    User = user(user_id=data["user_id"], user_name=data["user_name"], user_surname=data["user_surname"],
                 user_email=data["user_email"], user_password=data["user_password"], group_id= data["group_id"], role_id=data["role_id"] )
    db.add(User)
    db.commit()
    db.refresh(User)
    return User

@app.put("/api/users/")
def  edit_user(data = Body(), db: Session = Depends(get_db)):
    User = db.query(user).filter(user.user_id == data["user_id"]).first()

    if User == None:
        return JSONResponse(status_code=404, content={ "message": "User id NONE"})

    User.user_name = data["user_name"]
    User.user_surname = data["user_surname"]
    User.user_email = data["user_email"]

    db.commit()
    db.refresh(User)
    return "sucsesful"


@app.delete("/api/users/{id}")
def delete_user(id,  db: Session = Depends(get_db)):
    User = db.query(user).filter(user.user_id == id).first()
    if User == None:
        return "This user is NONE"    
    db.delete(User)
    db.commit()
    return "sucsesful"    
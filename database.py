from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/course"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

class group(Base):
    __tablename__ = "Groups"

    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String)
    avaliable_lessons = Column(Integer)



class role(Base):
    __tablename__ = "Roles"

    role_id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)


class user(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, index=True)    
    user_name = Column(String)
    user_surname = Column(String)
    user_email = Column(String, unique=True)
    user_password = Column(String)
    group_id =  Column(Integer, ForeignKey(group.group_id))
    role_id = Column(Integer, ForeignKey(role.role_id))
   # group = relationship("group", back_populates="Users")


SessionLocal = sessionmaker(autoflush=False, bind=engine)

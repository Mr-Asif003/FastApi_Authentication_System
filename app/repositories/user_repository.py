from sqlalchemy import Select
from sqlalchemy.orm import Session
from app.models.user import User
class User_repository:
    def __init__(self,db:Session):
        self.db=db

    def get_by_email(self,email:str):
        statement=Select(User).where(
            User.email==email
        )
        return self.db.scalar(statement)

    def get_by_id(self,id:int):
        statement=Select(User).where(
            User.id==id
        )
        return self.db.scalar(statement)

    def get_by_username(self,name:str):
        statement=Select(User).where(
            User.name==name
        )
        return self.db.scalar(statement)

    def create_user(self,user:User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user


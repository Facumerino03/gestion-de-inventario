from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class Category(db.Model):
    '''
    Class representing the categories and their attributes
    '''
    __tablename__ = "categories"
    
    id:int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name:str = db.Column("name", db.String(100), unique=True, nullable=False)
    description:str = db.Column("description", db.String(255), nullable=True)
    
    def __eq__(self, other: object) -> bool:
        return (
            self.id == other.id and 
            self.name == other.name and
            self.description == other.description
        )
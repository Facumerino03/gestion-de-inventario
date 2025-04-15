from sqlalchemy.exc import IntegrityError # type: ignore
import logging
from typing import List
from app.models import Category
from app import db
from app.repositories.base_repository import CreateAbstractRepository, ReadAbstractRepository, UpdateAbstractRepository, DeleteAbstractRepository

class CategoryRepository(CreateAbstractRepository, ReadAbstractRepository, UpdateAbstractRepository, DeleteAbstractRepository):
    '''
    Class representing the categories repository (interacts with the database)
    '''
    def save(self, category: Category) -> Category:
        '''
        Saves a category to the database
        param:
            category: Category
        return:
            Category: The saved category
        '''
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'error saving category: {e}')
            raise ValueError("A category with the same name already exists.")
        return category
      
    def find_all(self) -> List[Category]:
        '''
        Finds all categories
        return:
            List[Category]: The list of categories found
        '''
        return Category.query.all()

    def find_by(self, **kargs) -> List[Category]:
        '''
        Finds categories by a given criteria
        param:
            kargs: dict
        return:
            List[Category]: The list of categories found
        '''
        return Category.query.filter_by(**kargs).all()
        
    def find(self, id: int) -> Category:
        '''
        Finds a category by its id
        param:
            id: int
        return:
            Category: The category found
        '''
        result = None
        if id is not None:
            try:
                result = Category.query.get(id)
            except Exception as e:
                logging.error(f'error getting category by id: {id}, {e}')
        return result
    
    def delete(self, category: Category) -> None:
        '''
        Deletes a category from the database
        param:
            category: Category
        '''
        existing_category = self.find(category.id)
        if existing_category:
            db.session.delete(existing_category)
            db.session.commit()
        else:
            logging.error(f'error deleting category by id: {category.id}')
    
    def update(self, category: Category) -> Category:
        '''
        Updates a category in the database
        param:
            category: Category
        return:
            Category: The updated category
        '''
        existing_category = self.find(category.id)
        
        if existing_category is None:
            return None
        
        existing_category.name = category.name
        existing_category.description = category.description
        
        try:
            db.session.add(existing_category)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'error updating category: {e}')
            raise ValueError("A category with the same name already exists.")
        return existing_category
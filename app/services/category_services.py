from typing import List
from app.models import Category
from app.repositories import CategoryRepository

class CategoryService:
    '''
    Class that handles the CRUD of the categories
    '''
    def __init__(self):
        self.category_repository = CategoryRepository()

    def save(self, category: Category) -> Category:
        '''
        Saves a category
        
        param:
            category: Category
        return:
            Category
        '''
        return self.category_repository.save(category)

    def update(self, category: Category) -> Category:
        '''
        Updates a category
        
        param:
            category: Category
        return:
            Category
        '''
        return self.category_repository.update(category)

    def find_all(self) -> List[Category]:
        '''
        Finds all categories
        
        return:
            List[Category]
        '''
        categories = self.category_repository.find_all()
        return categories

    def find_by(self, **kargs) -> List[Category]:
        '''
        Finds categories by the given arguments
        
        param:
            **kargs: dict
        return:
            List[Category]
        '''
        categories = self.category_repository.find_by(**kargs)
        return categories

    def find(self, id: int) -> Category:
        '''
        Finds a category by its id
        
        param:
            id: int
        return:
            Category
        '''
        category = self.category_repository.find(id)
        return category

    def delete(self, id: int) -> None:
        '''
        Deletes a category by its id
        
        param:
            id: int
        '''
        category = self.category_repository.find(id)
        if category:
            self.category_repository.delete(category)
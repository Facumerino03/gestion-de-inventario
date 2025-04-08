from sqlalchemy.exc import IntegrityError # type: ignore
import logging
from typing import List
from app.models import Brand
from app import db
from app.repositories.base_repository import CreateAbstractRepository, ReadAbstractRepository, UpdateAbstractRepository, DeleteAbstractRepository

class BrandRepository(CreateAbstractRepository, ReadAbstractRepository, UpdateAbstractRepository, DeleteAbstractRepository):
    '''
    Class representing the brands repository (interacts with the database)
    '''
    def save(self, brand: Brand) -> Brand:
        '''
        Saves a brand to the database
        param:
            brand: Brand
        return:
            Brand: The saved brand
        '''
        try:
            db.session.add(brand)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'error saving brand: {e}')
            raise ValueError("A brand with the same name already exists.")
        return brand
      
    def find_all(self) -> List[Brand]:
        '''
        Finds all brands
        return:
            List[Brand]: The list of brands found
        '''
        return Brand.query.all()

    def find_by(self, **kargs) -> List[Brand]:
        '''
        Finds brands by a given criteria
        param:
            kargs: dict
        return:
            List[Brand]: The list of brands found
        '''
        return Brand.query.filter_by(**kargs).all()
        
    def find(self, id: int) -> Brand:
        '''
        Finds a brand by its id
        param:
            id: int
        return:
            Brand: The brand found
        '''
        result = None
        if id is not None:
            try:
                result = Brand.query.get(id)
            except Exception as e:
                logging.error(f'error getting brand by id: {id}, {e}')
        return result
    
    def delete(self, brand: Brand) -> None:
        '''
        Deletes a brand from the database
        param:
            brand: Brand
        '''
        existing_brand = self.find(brand.id)
        if existing_brand:
            db.session.delete(existing_brand)
            db.session.commit()
        else:
            logging.error(f'error deleting brand by id: {brand.id}')
    
    def update(self, brand: Brand) -> Brand:
        '''
        Updates a brand in the database
        param:
            brand: Brand
        return:
            Brand: The updated brand
        '''
        existing_brand = self.find(brand.id)
        
        if existing_brand is None:
            return None
        
        existing_brand.name = brand.name
        existing_brand.description = brand.description
        
        try:
            db.session.add(existing_brand)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'error updating brand: {e}')
            raise ValueError("A brand with the same name already exists.")
        return existing_brand
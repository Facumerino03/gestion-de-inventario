from typing import List
from app.models import Brand
from app.repositories import BrandRepository

class BrandService:
    '''
    Class that handles the CRUD of the brands
    '''
    def __init__(self):
        self.brand_repository = BrandRepository()

    def save(self, brand: Brand) -> Brand:
        '''
        Saves a brand
        
        param:
            brand: Brand
        return:
            Brand
        '''
        return self.brand_repository.save(brand)

    def update(self, brand: Brand) -> Brand:
        '''
        Updates a brand
        
        param:
            brand: Brand
        return:
            Brand
        '''
        return self.brand_repository.update(brand)

    def find_all(self) -> List[Brand]:
        '''
        Finds all brands
        
        return:
            List[Brand]
        '''
        brands = self.brand_repository.find_all()
        return brands

    def find_by(self, **kargs) -> List[Brand]:
        '''
        Finds brands by the given arguments
        
        param:
            **kargs: dict
        return:
            List[Brand]
        '''
        brands = self.brand_repository.find_by(**kargs)
        return brands

    def find(self, id: int) -> Brand:
        '''
        Finds a brand by its id
        
        param:
            id: int
        return:
            Brand
        '''
        brand = self.brand_repository.find(id)
        return brand

    def delete(self, id: int) -> None:
        '''
        Deletes a brand by its id
        
        param:
            id: int
        '''
        brand = self.brand_repository.find(id)
        if brand:
            self.brand_repository.delete(brand)
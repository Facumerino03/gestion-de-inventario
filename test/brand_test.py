import unittest
from flask import current_app
from app import create_app, db
import os
from app.models import Brand
from app.repositories import BrandRepository

repository = BrandRepository()

class BrandTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_brand(self):
        brand = self.__new_brand()
        self.assertIsNotNone(brand)
        self.assertEqual(brand.name, "Test Brand")
        self.assertEqual(brand.description, "This is a test brand")
    
    def test_compare_brand(self):
        brand = self.__new_brand()
        brand2 = self.__new_brand()
        self.assertEqual(brand, brand2)
    
    def test_save(self):
        brand = self.__new_brand()
        brand_save = repository.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
    
    def test_find(self):
        brand = self.__new_brand()
        brand_save = repository.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        brand = repository.find(brand_save.id)
        self.assertIsNotNone(brand)
        self.assertEqual(brand.id, brand_save.id)
    
    def test_find_all(self):
        brand = self.__new_brand()
        brand2 = self.__new_brand()
        brand2.name = "Another Brand"
        brand_save = repository.save(brand)
        brand2_save = repository.save(brand2)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertIsNotNone(brand2_save)
        self.assertIsNotNone(brand2_save.id)
        brands = repository.find_all()
        self.assertIsNotNone(brands)
        self.assertGreater(len(brands), 1)
    
    def test_find_by(self):
        brand = self.__new_brand()
        brand_save = repository.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        brands = repository.find_by(name='Test Brand')
        self.assertIsNotNone(brands)
        self.assertGreater(len(brands), 0)
    
    def test_update(self):
        brand = self.__new_brand()
        brand_save = repository.save(brand)
        brand_save.name = "Updated Brand"
        brand_update = repository.update(brand_save)
        self.assertIsNotNone(brand_update)
        self.assertEqual(brand_update.name, "Updated Brand")
    
    def test_delete(self):
        brand = self.__new_brand()
        brand_save = repository.save(brand)
        self.assertIsNotNone(brand_save)
        self.assertIsNotNone(brand_save.id)
        self.assertGreater(brand_save.id, 0)
        repository.delete(brand_save)
        brand_delete = repository.find(brand_save.id)
        self.assertIsNone(brand_delete)
    
    def __new_brand(self):
        return Brand(
            name="Test Brand",
            description="This is a test brand"
        )

if __name__ == '__main__':
    unittest.main()
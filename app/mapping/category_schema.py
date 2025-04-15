from marshmallow import Schema, fields, post_load, validate #type: ignore
from app.models import Category

class CategorySchema(Schema):
    '''
    Category schema for validation and serialization
    '''
    id:int = fields.Integer(dump_only=True)
    name:str = fields.String(required=True, validate=validate.Length(max=100))
    description:str = fields.String(required=False, validate=validate.Length(max=255))

    @post_load
    def bind_category(self, data: dict, **kwargs) -> Category:
        '''
        Bind data to a Category model
        params:
            data: Dict
        returns:
            Category
        '''
        return Category(**data)
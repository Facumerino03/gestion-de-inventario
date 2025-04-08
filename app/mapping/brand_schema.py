from marshmallow import Schema, fields, post_load, validate #type: ignore
from app.models import Brand

class BrandSchema(Schema):
    '''
    Brand schema for validation and serialization
    '''
    id:int = fields.Integer(dump_only=True)
    name:str = fields.String(required=True, validate=validate.Length(max=100))
    description:str = fields.String(required=False, validate=validate.Length(max=255))

    @post_load
    def bind_brand(self, data: dict, **kwargs) -> Brand:
        '''
        Bind data to a Brand model
        params:
            data: Dict
        returns:
            Brand
        '''
        return Brand(**data)
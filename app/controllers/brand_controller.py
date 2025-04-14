import logging
from flask import Blueprint, request
from flask import Response
from app.mapping import BrandSchema
from app.services import BrandService
from app.utils import build_response
from app.validators import validate_with

brand_bp = Blueprint('brand', __name__)
brand_map = BrandSchema()
brand_service = BrandService()

@brand_bp.route('/brand/<int:id>', methods=['GET'])
def get_brand(id: int) -> Response:
    '''
    Get a brand by its id
    params:
        id: int
    returns:
        Response
    '''
    brand = brand_service.find(id)
    
    if brand is None:
        logging.info(f'Brand not found id: {id}')
        return build_response('Brand not found', code=404)
    
    logging.info(f'Brand found id: {id}')
    return build_response('Brand found', data=brand_map.dump(brand))

@brand_bp.route('/brands', methods=['GET'])
def get_all_brands() -> Response:
    '''
    Get all brands
    returns:
        Response
    '''
    brands = brand_service.find_all()
    
    if not brands:
        logging.info('No brands found')
        return build_response('No brands found', code=404)
    
    logging.info('Brands found')
    return build_response('Brands found', data={'brands': brand_map.dump(brands, many=True)})

@brand_bp.route('/create', methods=['POST'])
@validate_with(BrandSchema)
def post_brand() -> Response:
    '''
    Create a brand
    returns:
        Response
    '''
    brand = brand_map.load(request.json)
    
    try:
        brand_saved = brand_service.save(brand)
        logging.info(f'Brand saved id: {brand_saved.id}')
        return build_response('Brand saved', data=brand_map.dump(brand_saved), code=201)
    
    except ValueError as e:
        logging.error(f'Error saving brand: {e}')
        return build_response(str(e), code=400)

@brand_bp.route('/brand/<int:id>', methods=['PUT'])
@validate_with(BrandSchema)
def update_brand(id: int) -> Response:
    '''
    Update a brand
    params:
        id: int
    returns:
        Response
    '''
    brand = brand_map.load(request.json)
    existing_brand = brand_service.find(id)
    
    if existing_brand is None:
        logging.info(f'Brand not found id: {id}')
        return build_response('Brand not found', code=404)
    
    try:
        brand.id = id
        updated_brand = brand_service.update(brand)
        logging.info(f'Brand updated id: {id}')
        return build_response('Brand updated', data=brand_map.dump(updated_brand))
    
    except ValueError as e:
        logging.error(f'Error updating brand: {e}')
        return build_response(str(e), code=400)

@brand_bp.route('/brand/<int:id>', methods=['DELETE'])
def delete_brand(id: int) -> Response:
    '''
    Delete a brand
    params:
        id: int
    returns:
        Response
    '''
    brand = brand_service.find(id)
    
    if brand is None:
        logging.info(f'Brand not found id: {id}')
        return build_response('Brand not found', code=404)
    
    brand_service.delete(id)
    logging.info(f'Brand deleted id: {id}')
    return build_response('Brand deleted', code=200)
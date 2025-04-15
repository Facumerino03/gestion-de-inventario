import logging
from flask import Blueprint, request
from flask import Response
from app.mapping import CategorySchema
from app.services import CategoryService
from app.utils import build_response
from app.validators import validate_with

category_bp = Blueprint('category', __name__)
category_map = CategorySchema()
category_service = CategoryService()

@category_bp.route('/category/<int:id>', methods=['GET'])
def get_category(id: int) -> Response:
    '''
    Get a category by its id
    params:
        id: int
    returns:
        Response
    '''
    category = category_service.find(id)
    
    if category is None:
        logging.info(f'Category not found id: {id}')
        return build_response('Category not found', code=404)
    
    logging.info(f'Category found id: {id}')
    return build_response('Category found', data=category_map.dump(category))

@category_bp.route('/categories', methods=['GET'])
def get_all_categories() -> Response:
    '''
    Get all categories
    returns:
        Response
    '''
    categories = category_service.find_all()
    
    if not categories:
        logging.info('No categories found')
        return build_response('No categories found', code=404)
    
    logging.info('Categories found')
    return build_response('Categories found', data={'categories': category_map.dump(categories, many=True)})

@category_bp.route('/create', methods=['POST'])
@validate_with(CategorySchema)
def post_category() -> Response:
    '''
    Create a category
    returns:
        Response
    '''
    category = category_map.load(request.json)
    
    try:
        category_saved = category_service.save(category)
        logging.info(f'Category saved id: {category_saved.id}')
        return build_response('Category saved', data=category_map.dump(category_saved), code=201)
    
    except ValueError as e:
        logging.error(f'Error saving category: {e}')
        return build_response(str(e), code=400)

@category_bp.route('/category/<int:id>', methods=['PUT'])
@validate_with(CategorySchema)
def update_category(id: int) -> Response:
    '''
    Update a category
    params:
        id: int
    returns:
        Response
    '''
    category = category_map.load(request.json)
    existing_category = category_service.find(id)
    
    if existing_category is None:
        logging.info(f'Category not found id: {id}')
        return build_response('Category not found', code=404)
    
    try:
        category.id = id
        updated_category = category_service.update(category)
        logging.info(f'Category updated id: {id}')
        return build_response('Category updated', data=category_map.dump(updated_category))
    
    except ValueError as e:
        logging.error(f'Error updating category: {e}')
        return build_response(str(e), code=400)

@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id: int) -> Response:
    '''
    Delete a category
    params:
        id: int
    returns:
        Response
    '''
    category = category_service.find(id)
    
    if category is None:
        logging.info(f'Category not found id: {id}')
        return build_response('Category not found', code=404)
    
    category_service.delete(id)
    logging.info(f'Category deleted id: {id}')
    return build_response('Category deleted', code=200)
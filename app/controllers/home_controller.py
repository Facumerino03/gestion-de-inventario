from flask import Blueprint, jsonify, Response
from app.mapping import MessageSchema
from app.services import MessageBuilder
from app.utils import build_response
import logging

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def get_home() -> Response:
    '''
    API Home - Documentation and available endpoints for inventory management
    returns:
        Response
    '''
    api_docs = {
        'name': 'Stock Management API',
        'version': '1.0.0',
        'description': 'API for inventory management',
        'endpoints': {
            'brands': {
                'GET /brands': 'Get all brands',
                'GET /brands/<id>': 'Get specific brand',
                'POST /brands/create': 'Create new brand',
                'PUT /brands/<id>': 'Update brand',
                'DELETE /brands/<id>': 'Delete brand'
            },
            'categories': {
                'GET /categories': 'Get all categories',
                'GET /categories/<id>': 'Get specific category',
                'POST /categories/create': 'Create new category',
                'PUT /categories/<id>': 'Update category',
                'DELETE /categories/<id>': 'Delete category'
            },
            'articles': {
                'GET /articles': 'Get all articles',
                'GET /articles/<id>': 'Get specific article',
                'POST /articles/create': 'Create new article',
                'PUT /articles/<id>': 'Update article',
                'DELETE /articles/<id>': 'Delete article'
            },
            'stock': {
                'GET /stock': 'Get current stock',
                'GET /stock/<article_id>': 'Get stock for specific article'
            }
        },
        'api_version': '/api/v1',
        'documentation': 'For more details, check the complete documentation at /docs',
        'status': {
            'code': 200,
            'message': 'API is running correctly'
        }
    }
    
    logging.info('Home endpoint accessed')
    return build_response('Welcome to Stock Management API', data=api_docs)
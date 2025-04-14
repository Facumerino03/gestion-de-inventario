#https://flask.palletsprojects.com/es/main/blueprints/

class RouteApp:
    def init_app(self, app):
        '''
        Initializes the routes
        param:
            app: Flask
        '''

        from app.controllers import home_bp
        app.register_blueprint(home_bp, url_prefix='/api/v1')
from flask import Flask
from flask.views import MethodView

from .Users.resources import users_blueprint
from .Categories.resources import categories_blueprint

class HelloWorld(MethodView):
    #C -> Create -> POST
    #R -> Read -> GET
    #U -> Update -> PUT/PATCH
    #D -> Delete -> DELETE
    def get(self):
        return {'message': 'Hey there! Hello World :)'}
    
def create_app():
    app = Flask(__name__ )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sa:Desarrollo12@localhost/thincrs'
        
    hello_world=HelloWorld.as_view("hello_world")
    
    app.add_url_rule("/", view_func=hello_world)
    app.add_url_rule("/api/", view_func=hello_world)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(categories_blueprint)
    
    return app
from flask.views import MethodView
from flask import Blueprint, request


users_blueprint = Blueprint("users_blueprint",__name__, url_prefix='/api/')

class UserList(MethodView):
    def get(self):
        return [{"username": "Obed"},{"email": "obed_aguilar9@hotmail.com"}]
 
class UsersID(MethodView):
     def get(self, user_id):
         return [{"id":user_id, "Username": "usuario"}]
 
class Users(MethodView):
    def post(self):
        data = request.get_json() 
        
        email=data.get("email")
        username = data.get("username")
        
        if email is None:
            return {"message": "No has ingresado tu correo..."},400
        if username is None:
            return {"message": "No has ingresado tu Usuario..."},400
        
        return {"message": "Bienvenido :)"}

    
users_blueprint.add_url_rule(
    'users', view_func=UserList.as_view("users_list")
)

users_blueprint.add_url_rule(
    'users', view_func=Users.as_view("users")
)

users_blueprint.add_url_rule(
    'users<user_id>', view_func=UsersID.as_view("users_id")
)
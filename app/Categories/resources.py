from flask.views import MethodView
from flask import Blueprint, request


categories_blueprint = Blueprint("categories_blueprint",__name__, url_prefix='/api/')

# Retorna una lista de Categorias
class CategoriesList(MethodView):
    def get(self):
        return [{1:{'nameCategory':'Categoria 1',
                    'descriptionCategory':'Categoria 1 de prueba'
                    },
                 2:{'nameCategory':'Categoria 2',
                    'descriptionCategory':'Categoria 2 de prueba'
                    },
                 3:{'nameCategory':'Categoria 3',
                    'descriptionCategory':'Categoria 3 de prueba'
                    },
                 4:{'nameCategory':'Categoria 4',
                    'descriptionCategory':'Categoria 4 de prueba'
                    },
                 5:{'nameCategory':'Categoria 5',
                    'descriptionCategory':'Categoria 5 de prueba'
                    }
                 }
                ]
 
 # Obtener una categoria
class Category(MethodView):
    def get(self):
        data = request.get_json()
        id = data.get('id')
        
        CategoriesLst = [{1:{'nameCategory':'Categoria 1','descriptionCategory':'Categoria 1 de prueba'},2:{'nameCategory':'Categoria 2','descriptionCategory':'Categoria 2 de prueba'},3:{'nameCategory':'Categoria 3','descriptionCategory':'Categoria 3 de prueba'},4:{'nameCategory':'Categoria 4','descriptionCategory':'Categoria 4 de prueba'},5:{'nameCategory':'Categoria 5','descriptionCategory':'Categoria 5 de prueba'}}]

        return CategoriesLst.index(id)
        
 
 # Insertar una Categoria

# Agrega una categoria
class Categories(MethodView):
    def post(self):
        data = request.get_json() 
        
        nameCategory = data.get('nameCategory')
        descriptionCategory = data.get('description')

        
        if nameCategory is None:
            return {"message": "No has ingresado la categoria..."},400
        elif descriptionCategory is None:
            return {"message": "No has ingresado una descripcion de la categoria..."},400
        
        return {"message": "Categoria agregada exitosamente :)"}

    
categories_blueprint.add_url_rule(
    'categories', view_func=CategoriesList.as_view("categories_list")
)

categories_blueprint.add_url_rule(
    'categories', view_func=Categories.as_view("categories")
)

categories_blueprint.add_url_rule(
    'categories<id>', view_func=Category.as_view("category")
)
from flask import request, jsonify
from flask_restful import Resource
from main.maps import ProductoSchema
from main.services import ProductoService
from flask_jwt_extended import get_jwt_identity

producto_schema = ProductoSchema()
producto_service = ProductoService()

class ProductoController(Resource):
    
    def _verificar_permiso(self):
        current_user = get_jwt_identity()
        if current_user["role"] != "admin":
            raise PermissionError("No tienes autorización para realizar esta acción")

    def get(self, id):
        try:
            producto = producto_service.obtener_producto(id) 
            return producto_schema.dump(producto), 200
        except ValueError as e:
            return {"error": str(e)}, 404

    def delete(self, id):
        try:
            self._verificar_permiso()  
            message = producto_service.eliminar_producto(id)
            return {"message": message}, 204
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

    def put(self, id):
        try:
            datos = request.get_json()
            self._verificar_permiso()  
            producto_actualizada = producto_service.actualizar_producto(id, datos)
            return producto_schema.dump(producto_actualizada, many=False), 200
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404


class ProductosController(Resource):
    
    def get(self):
        
        filtros = request.get_json(silent=True) or {}
        productos = producto_service.obtener_total_productos(filtros)
        return jsonify([producto_schema.dump(producto) for producto in productos])

    def post(self):
        try:
            self._verificar_permiso()
            producto = producto_schema.load(request.get_json())
            return producto_schema.dump(producto_service.agregar_producto(producto)), 201
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404
    
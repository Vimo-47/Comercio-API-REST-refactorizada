from flask import request, jsonify
from flask_restful import Resource
from main.maps import CompraSchema
from main.services import CompraService
from flask_jwt_extended import get_jwt_identity

compra_schema = CompraSchema()
compra_service = CompraService()

class CompraController(Resource):
    
    def _verificar_permiso(self, compra):
        current_user = get_jwt_identity()
        if current_user["usuarioId"] != compra.usuarioId and current_user["role"] != "admin":
            raise PermissionError("No tienes autorización para realizar esta acción")

    def get(self, id):
        try:
            compra = compra_service.obtener_compra(id)
            self._verificar_permiso(compra)  
            return compra_schema.dump(compra), 200
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

    def delete(self, id):
        try:
            compra = compra_service.obtener_compra(id)
            self._verificar_permiso(compra)  
            message = compra_service.eliminar_compra(id)
            return {"message": message}, 204
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

    def put(self, id):
        try:
            datos = request.get_json()
            compra = compra_service.obtener_compra(id)
            self._verificar_permiso(compra)  
            compra_actualizada = compra_service.actualizar_compra(id, datos)
            return compra_schema.dump(compra_actualizada, many=False), 200
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404


class ComprasController(Resource):
    
    def get(self):
        current_user = get_jwt_identity()
        
        # Solo el admin puede ver todas las compras
        if current_user["role"] != "admin":
            return {"error": "No tienes autorización para ver todas las compras"}, 403

        filtros = request.get_json(silent=True) or {}
        compras = compra_service.obtener_total_compras(filtros)
        return jsonify([compra_schema.dump(compra) for compra in compras])

    def post(self):
        compra = compra_schema.load(request.get_json())
        return compra_schema.dump(compra_service.agregar_compra(compra)), 201
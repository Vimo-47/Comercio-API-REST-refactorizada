from flask import request, jsonify
from flask_restful import Resource
from main.maps import ProductoCompraSchema
from main.services import ProductoCompraService

productocompra_schema = ProductoCompraSchema()
productocompra_service = ProductoCompraService()

class ProductoCompraController(Resource):
    
    def get(self, id):
        try:
            productocompra = productocompra_service.obtener_productocompra(id)  
            return productocompra_schema.dump(productocompra), 200
        except ValueError as e:
            return {"error": str(e)}, 404

    def delete(self, id):
        try:
            message = productocompra_service.eliminar_productocompra(id)
            return {"message": message}, 204
        except ValueError as e:
            return {"error": str(e)}, 404

    def put(self, id):
        try:
            datos = request.get_json()
            productocompra_actualizada = productocompra_service.actualizar_productocompra(id, datos)
            return productocompra_schema.dump(productocompra_actualizada, many=False), 200
        except ValueError as e:
            return {"error": str(e)}, 404


class ProductosComprasController(Resource):
    
    def get(self):
        filtros = request.get_json(silent=True) or {}
        productocompras = productocompra_service.obtener_total_productocompras(filtros)
        return jsonify([productocompra_schema.dump(productocompra) for productocompra in productocompras])

    def post(self):
        productocompra = productocompra_schema.load(request.get_json())
        return productocompra_schema.dump(productocompra_service.agregar_productocompra(productocompra)), 201
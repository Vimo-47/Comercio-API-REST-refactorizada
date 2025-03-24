from  flask_restful import Resource
from main.maps import ProductoCompraSchema
from main.services import ProductoCompraService
from flask import request

#Interactua con el mundo exterior, recive y envia datos

productocompra_schema = ProductoCompraSchema()
productocompra_service = ProductoCompraService()

#Load = Recibir || Dump = Enviar

class ProductoCompraController(Resource):
    
    def get(self, id):
        productocompra= productocompra_service.obtener_productocompra(id)
        return productocompra_schema.dump(productocompra, many=False)
    
class ProductosComprasController(Resource):
    
    def post(self):
        productocompra = productocompra_schema.load(request.get_json())
        return productocompra_schema.dump(productocompra_service.agregar_productocompra(productocompra), many=False)
from  flask_restful import Resource
from main.maps import ProductoSchema
from main.services import ProductoService
from flask import request

#Interactua con el mundo exterior, recive y envia datos

producto_schema = ProductoSchema()
producto_service = ProductoService()

#Load = Recibir || Dump = Enviar

class ProductoController(Resource):
    
    def get(self, id):
        producto= producto_service.obtener_producto_descuento(id)
        return producto_schema.dump(producto, many=False)
    
class ProductosController(Resource):
    
    def post(self):
        producto = producto_schema.load(request.get_json())
        return producto_schema.dump(producto_service.agregar_producto(producto), many=False)
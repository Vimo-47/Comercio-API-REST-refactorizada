from  flask_restful import Resource
from main.maps import CompraSchema
from main.services import CompraService
from flask import request

#Interactua con el mundo exterior, recive y envia datos

compra_schema = CompraSchema()
compra_service = CompraService()

#Load = Recibir || Dump = Enviar

class CompraController(Resource):
    
    def get(self, id):
        compra= compra_service.obtener_compra(id)
        return compra_schema.dump(compra, many=False)
    
class ComprasController(Resource):
    
    def post(self):
        compra = compra_schema.load(request.get_json())
        return compra_schema.dump(compra_service.agregar_compra(compra), many=False)
    
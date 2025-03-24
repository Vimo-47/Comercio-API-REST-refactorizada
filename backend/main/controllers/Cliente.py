from  flask_restful import Resource
from main.maps import UsuarioSchema
from main.services import ClientesService
from flask import request

#Interactua con el mundo exterior, recive y envia datos

cliente_schema = UsuarioSchema()
cliente_service = ClientesService()

#Load = Recibir || Dump = Enviar

class ClienteController(Resource):
    
    def get(self, id):
        cliente= cliente_service.obtener_cliente(id)
        return cliente_schema.dump(cliente, many=False)
    
class ClientesController(Resource):
    
    def post(self):
        cliente = cliente_schema.load(request.get_json())
        return cliente_schema.dump(cliente_service.agregar_cliente(cliente), many=False)
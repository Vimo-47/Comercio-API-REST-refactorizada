from  flask_restful import Resource
from main.maps import UsuarioSchema
from main.services import UsuarioService
from flask import request

#Interactua con el mundo exterior, recive y envia datos

usuario_schema = UsuarioSchema()
usuario_service = UsuarioService()

#Load = Recibir || Dump = Enviar

class UsuarioController(Resource):
    
    def get(self, id):
        usuario= usuario_service.obtener_usuario(id)
        return usuario_schema.dump(usuario, many=False)
    
class UsuariosController(Resource):
    
    def post(self):
        usuario = usuario_schema.load(request.get_json())
        return usuario_schema.dump(usuario_service.agregar_usuario(usuario), many=False)
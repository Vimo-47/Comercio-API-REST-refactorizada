from flask import request, jsonify
from flask_restful import Resource
from main.maps import UsuarioSchema
from main.services import UsuarioService
from flask_jwt_extended import get_jwt_identity

usuario_schema = UsuarioSchema()
usuario_service = UsuarioService()

class ClienteController(Resource):

    def _verificar_permiso(self, usuario):
        current_user = get_jwt_identity()
        if current_user["usuarioId"] != usuario.id and current_user["role"] != "admin":
            raise PermissionError("No tienes autorización para realizar esta acción")

    def get(self, id):
        try:
            usuario = usuario_service.obtener_usuario(id)
            self._verificar_permiso(usuario)  
            return usuario_schema.dump(usuario), 200
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

    def delete(self, id):
        try:
            usuario = usuario_service.obtener_usuario(id)
            self._verificar_permiso(usuario)  
            message = usuario_service.eliminar_usuario(id)
            return {"message": message}, 204
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

    def put(self, id):
        try:
            datos = request.get_json()
            usuario = usuario_service.obtener_usuario(id)
            self._verificar_permiso(usuario)  
            usuario_actualizado = usuario_service.actualizar_usuario(id, datos)
            return usuario_schema.dump(usuario_actualizado, many=False), 200
        except PermissionError as e:
            return {"error": str(e)}, 403
        except ValueError as e:
            return {"error": str(e)}, 404

class ClientesController(Resource):

    def get(self):
        current_user = get_jwt_identity()

        # Solo el admin puede ver todos los clientes
        if current_user["role"] != "admin":
            return {"error": "No tienes autorización para ver todos los clientes"}, 403

        filtros = request.get_json(silent=True) or {}
        usuarios = usuario_service.obtener_todos_usuarios(filtros)
        return jsonify([usuario_schema.dump(usuario) for usuario in usuarios["usuarios"]])

    def post(self):
        cliente = usuario_schema.load(request.get_json())
        cliente.role = 'cliente'
        return usuario_schema.dump(usuario_service.agregar_usuario(cliente)), 201

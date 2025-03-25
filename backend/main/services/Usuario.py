from flask_jwt_extended import get_jwt_identity
from main.repositories import UsuarioRepository

#Se encarga de aplicarle la lógica

usuario_repository = UsuarioRepository()

class UsuarioService:

    def obtener_usuario(self,id):
        usuario = usuario_repository.find_one(id)
        return usuario

    def obtener_total_usuarios(self, filtros):
        
        page = int(filtros.get("page", 1))  # Convierte a int para evitar errores
        per_page = int(filtros.get("per_page", 5))

        usuarios = usuario_repository.find_all(page, per_page)  # Ahora sí usa la paginación

        return {
            "usuarios": [usuario.to_json() for usuario in usuarios.items],  # Lista de usuarios
            "total": usuarios.total,  # Total de usuarios en la BD
            "pages": usuarios.pages,  # Total de páginas disponibles
            "page": usuarios.page,  # Página actual
        }


    def eliminar_usuario(self, id):
        usuario_repository.delete(id)
        return "Usuario eliminado correctamente"
    
    def agregar_usuario(self, usuario):
        usuario = usuario_repository.create(usuario)
        return usuario

    def actualizar_usuario(self, id, datos):
        usuario = usuario_repository.find_one(id)

        for key, value in datos.items():
            setattr(usuario, key, value)

        return usuario_repository.update(usuario)
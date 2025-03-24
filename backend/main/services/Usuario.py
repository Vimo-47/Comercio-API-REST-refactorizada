from main.repositories import UsuarioRepository

#Se encarga de aplicar la lógica

usuarios_repository = UsuarioRepository()

class UsuarioService:
    

    def obtener_usuario(self,id):
        usuario = usuarios_repository.find_one(id)
        return usuario
    
    def obtener_total_usuarios(self):
        usuario = usuarios_repository.find_all()
        return usuario
    
    def eliminar_usuario(self,id):
        usuario = usuarios_repository.delete(id)
        return usuario
    
    def agregar_usuario(self, usuario):
        usuario = usuarios_repository.update(usuario)
        return usuario
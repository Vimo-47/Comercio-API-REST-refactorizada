from main.repositories import ClientesRepository

#Se encarga de aplicarle la lógica

clientes_repository = ClientesRepository()

class ClientesService:
    

    def obtener_cliente(self,id):
        cliente = clientes_repository.find_one(id)
        return cliente
    
    def obtener_total_clientes(self):
        cliente = clientes_repository.find_all()
        return cliente
    
    def eliminar_cliente(self,id):
        cliente = clientes_repository.delete(id)
        return cliente
    
    def agregar_cliente(self, usuario):
        cliente = clientes_repository.update(usuario)
        return cliente
    
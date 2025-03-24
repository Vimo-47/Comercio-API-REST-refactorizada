from main.repositories import CompraReposiroty

#Se encarga de aplicarle la lógica

compra_repository = CompraReposiroty()

class CompraService:
    

    def obtener_compra(self,id):
        compra = compra_repository.find_one(id)
        return compra
    
    def obtener_total_compras(self):
        compra = compra_repository.find_all()
        return compra
    
    def eliminar_compra(self,id):
        compra = compra_repository.delete(id)
        return compra
    
    def agregar_compra(self, compra):
        compra = compra_repository.update(compra)
        return compra
    

from main.repositories import ProductoCompraRepository

#Se encarga de aplicarle la lógica

productocompra_repository = ProductoCompraRepository()

class ProductoCompraService:
    
    def agregar_productocompra(self, productocompra):
        productocompra = productocompra_repository.create(productocompra)
        return productocompra
    
    def eliminar_productocompra(self,id):
        productocompra = productocompra_repository.delete(id)
        return productocompra

    def obtener_productocompra(self,id):
        productocompra = productocompra_repository.find_one(id)
        return productocompra
    
    def obtener_total_productoscompra(self):
        productocompra = productocompra_repository.find_all()
        return productocompra

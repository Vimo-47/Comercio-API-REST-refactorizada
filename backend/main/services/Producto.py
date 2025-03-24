from main.repositories import ProductoRepository

#Se encarga de aplicarle la lógica

producto_repository = ProductoRepository()

class ProductoService:
    
    def agregar_producto(self, producto):
        producto = producto_repository.create(producto)
        return producto
    
    def eliminar_producto(self,id):
        producto = producto_repository.delete(id)
        return producto

    def obtener_producto(self,id):
        producto = producto_repository.find_one(id)
        return producto
    
    def obtener_producto_descuento(self,id):
        producto = producto_repository.find_one(id)
        producto = producto * 0.8
        return producto
    
    def obtener_total_productos(self):
        producto = producto_repository.find_all()
        return producto


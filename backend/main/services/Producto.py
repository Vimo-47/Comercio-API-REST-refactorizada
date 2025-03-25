from main.repositories import ProductoRepository

#Se encarga de aplicarle la lógica

producto_repository = ProductoRepository()

class ProductoService:
    

    def obtener_producto(self,id):
        producto = producto_repository.find_one(id)
        return producto

    def obtener_total_productos(self, filtros):
        page = int(filtros.get("page", 1))  # Convierte a int para evitar errores
        per_page = int(filtros.get("per_page", 5))

        productos = producto_repository.find_all(page, per_page)  # Ahora sí usa la paginación

        return {
            "productos": [producto.to_json() for producto in productos.items],  # Lista de productos
            "total": productos.total,  # Total de productos en la BD
            "pages": productos.pages,  # Total de páginas disponibles
            "page": productos.page,  # Página actual
        }


    def eliminar_producto(self, id):
        producto_repository.delete(id)
        return "Producto eliminada correctamente"
    
    def agregar_producto(self, producto):
        producto = producto_repository.create(producto)
        return producto

    def actualizar_producto(self, id, datos):
        producto = producto_repository.find_one(id)

        for key, value in datos.items():
            setattr(producto, key, value)

        return producto_repository.update(producto)
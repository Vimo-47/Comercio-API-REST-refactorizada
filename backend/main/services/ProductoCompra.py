from main.repositories import ProductoCompraRepository

#Se encarga de aplicarle la lógica

productocompra_repository = ProductoCompraRepository()

class ProductoCompraService: 
    

    def obtener_productocompra(self,id):
        productocompra = productocompra_repository.find_one(id)
        return productocompra

    def obtener_total_productocompras(self, filtros):
        page = int(filtros.get("page", 1))  # Convierte a int para evitar errores
        per_page = int(filtros.get("per_page", 5))

        productocompras = productocompra_repository.find_all(page, per_page)  # Ahora sí usa la paginación

        return {
            "productocompras": [productocompra.to_json() for productocompra in productocompras.items],  # Lista de productocompras
            "total": productocompras.total,  # Total de productocompras en la BD
            "pages": productocompras.pages,  # Total de páginas disponibles
            "page": productocompras.page,  # Página actual
        }


    def eliminar_productocompra(self, id):
        productocompra_repository.delete(id)
        return "ProductoCompra eliminada correctamente"
    
    def agregar_productocompra(self, productocompra):
        productocompra = productocompra_repository.create(productocompra)
        return productocompra

    def actualizar_productocompra(self, id, datos):
        productocompra = productocompra_repository.find_one(id)

        for key, value in datos.items():
            setattr(productocompra, key, value)

        return productocompra_repository.update(productocompra)
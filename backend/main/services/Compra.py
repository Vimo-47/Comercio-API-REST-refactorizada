from main.repositories import CompraRepository

#Se encarga de aplicarle la lógica

compra_repository = CompraRepository()

class CompraService:
    

    def obtener_compra(self,id):
        compra = compra_repository.find_one(id)
        return compra

    def obtener_total_compras(self, filtros):
        page = int(filtros.get("page", 1))  # Convierte a int para evitar errores
        per_page = int(filtros.get("per_page", 5))

        compras = compra_repository.find_all(page, per_page)  # Ahora sí usa la paginación

        return {
            "compras": [compra.to_json() for compra in compras.items],  # Lista de compras
            "total": compras.total,  # Total de compras en la BD
            "pages": compras.pages,  # Total de páginas disponibles
            "page": compras.page,  # Página actual
        }


    def eliminar_compra(self, id):
        compra_repository.delete(id)
        return "Compra eliminada correctamente"
    
    def agregar_compra(self, compra):
        compra = compra_repository.create(compra)
        return compra

    def actualizar_compra(self, id, datos):
        compra = compra_repository.find_one(id)

        for key, value in datos.items():
            setattr(compra, key, value)

        return compra_repository.update(compra)
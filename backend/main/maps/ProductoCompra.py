from marshmallow import Schema, fields, post_load,post_dump
from main.models import ProductoCompraModel
# from .Producto import ProductoSchema
# from .Compra import CompraSchema
# Se usa la relaccion en string para evitar errores circulares

#Se encarga de cambiar las interfaces para hacer compatibles python objects con JSON

class ProductoCompraSchema(Schema):

    id = fields.Integer(dump_only=True)
    productoId = fields.Integer(dump_only=True)
    producto = fields.Nested('ProductoSchema')
    compraId = fields.Integer(dump_only=True)
    compra = fields.Nested('CompraSchema')
     

    @post_load
    def create_productocompra(self, data,**kwarg):
        return ProductoCompraModel(**data)

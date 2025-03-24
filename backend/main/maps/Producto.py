from marshmallow import Schema, fields, post_load,post_dump
from main.models import ProductoModel
from .ProductoCompra import ProductoCompraSchema

#Se encarga de cambiar las interfaces para hacer compatibles python objects con JSON

class ProductoSchema(Schema):

    id = fields.Integer(dump_only=True)
    nombre = fields.String(dump_only=True)
    precio = fields.Integer(dump_only=True)
    imagen = fields.String(dumb_only=True)
    descripcion = fields.String(dumb_only=True)
    stock = fields.Integer(dump_only=True)
    productoscompras = fields.Nested(ProductoCompraSchema)

    @post_load
    def create_producto(self, data,**kwarg):
        return ProductoModel(**data)
    
    #Retorna todo menos el usuarioID
    SKIP_VALUES = ['productoscompra']
    @post_dump
    def remove_skip_values(self,data,**kwargs):
        return{
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }
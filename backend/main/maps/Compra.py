from marshmallow import Schema, fields, post_load, post_dump
from main.models import CompraModel
from .Usuario import UsuarioSchema
from .ProductoCompra import ProductoCompraSchema

#Se encarga de cambiar las interfaces para hacer compatibles python objects con JSON

class CompraSchema(Schema):

    id = fields.Integer(dump_only=True)
    fecha_compra = fields.DateTime(required=False)
    usuarioId = fields.Integer(required=False)
    usuario = fields.Nested(UsuarioSchema)
    productocompra = fields.Nested(ProductoCompraSchema)

    @post_load
    def create_compra(self, data,**kwarg):
        return CompraModel(**data)
    
    #Retorna todo menos el usuarioID
    SKIP_VALUES = ['usuarioId']
    @post_dump
    def remove_skip_values(self,data,**kwargs):
        return{
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }
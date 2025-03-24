from .. import db
from main.models import ProductoCompraModel

#Se encarga de interactuar con la Base de Datos

class ProductoCompraRepository:

    __productocompra = ProductoCompraModel

    @property
    def productocompra(self):
        return self.__productocompra
    
    def find_one(self, id):
        object = db.session.query(self.productocompra).get(id)
        return object
    
    def find_all(self):
        object = db.session.query(self.productocompra).all()
        return object
    
    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    
    #Es igual que crear pero usamos otro nombre para evitar confusiones
    def update (self, object):
        return self.create(object)
    
    def delete(self, id):
        object = self.find_one(id)
        db.session.delete(object)
        db.session.commit()
        return object
from .. import db
from main.models import CompraModel

#Se encarga de interactuar con la Base de Datos

class CompraReposiroty:

    __modelo = CompraModel

    @property
    def modelo(self):
        return self.__modelo
    
    def find_one(self, id):
        object = db.session.query(self.modelo).get(id)
        if object is None:
            raise ValueError(f'Compra con la id {id} no encontrada')
        return object
    
    def find_all(self):
        object = db.session.query(self.modelo).all()
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

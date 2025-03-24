from .. import db
from main.models import UsuarioModel

#Se encarga de interactuar con la Base de Datos

class UsuarioRepository:

    __usuario = UsuarioModel

    @property
    def usuario(self):
        return self.__usuario
    
    def find_one(self, id):
        object = db.session.query(self.usuario).get(id)
        return object
    
    def find_all(self):
        object = db.session.query(self.usuario).all()
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
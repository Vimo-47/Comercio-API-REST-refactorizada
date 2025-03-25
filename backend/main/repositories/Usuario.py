from .. import db
from main.models import UsuarioModel

#Se encarga de interactuar con la Base de Datos

class UsuarioRepository:

    __modelo = UsuarioModel

    @property
    def modelo(self):
        return self.__modelo
    
    def find_one(self, id):
        object = db.session.query(self.modelo).get(id)
        if object is None:
            raise ValueError(f'Usuario con la id {id} no encontrada')
        return object
    

    def find_all(self, page=1, per_page=5, max_per_page=10):
        object = db.session.query(self.modelo).paginate(page=page, per_page=per_page, error_out=False, max_per_page=max_per_page)
        return object

    
    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    
    def update (self, object):
        db.session.merge(object)
        db.session.commit()
        return object
    
    def delete(self, id):
        object = self.find_one(id)
        db.session.delete(object)
        db.session.commit()
        return object
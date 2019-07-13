import uuid
class Alumno:
    def __init__(self,nombre,edad,grupo,promedio,sexo,uid=None):
        self.nombre = nombre
        self.edad = edad
        self.grupo = grupo
        self.promedio = promedio
        self.sexo = sexo
        self.uid = uid or uuid.uuid4()
    
    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return['nombre','edad','grupo','promedio','sexo','uid']
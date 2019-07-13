import csv
import os
from alumnos import Alumno

class Services:
    def __init__(self,Table_name):
        self.Table_name = Table_name
    
    def Alta_usuario(self,alumno):
        with open(self.Table_name,mode='a') as f:
            writer = csv.DictWriter(f,fieldnames=Alumno.schema())
            writer.writerow(alumno.to_dict())
    
    def Baja_usuario(self,alumno):
        tmp_table = self.Table_name+'.tmp'
        lista = [alumn for alumn in self.Consulta_usuario() if alumno.uid != alumn['uid']]
        with open(tmp_table,mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=Alumno.schema())
            writer.writerows(lista)
        os.remove(self.Table_name)
        os.rename(tmp_table,self.Table_name)

    def Cambio_usuario(self,alumno):
        tmp_table = self.Table_name+'.tmp'
        lista = self.Consulta_usuario()
        lista_act=[]
        for alumn in lista:
            if(alumn['uid']==alumno.uid):
                lista_act.append(alumno.to_dict())
            else:
                lista_act.append(alumn)
        with open(tmp_table,mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=Alumno.schema())
            writer.writerows(lista_act)
        os.remove(self.Table_name)
        os.rename(tmp_table,self.Table_name)

    def Consulta_usuario(self):
        with open(self.Table_name,mode='r') as f:
            reader = csv.DictReader(f,fieldnames=Alumno.schema())
            return list(reader)
    
    def _saveToDisk(self,alumnos):
        pass
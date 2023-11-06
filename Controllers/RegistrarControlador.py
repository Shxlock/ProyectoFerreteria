import bcrypt

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from Models.User_verification import User_verification
from Controllers.UsuarioExistente import UsuarioExistenteError
from Models.User import User
from Database.Conection import connection


class Registrar():
    
    def __init__(self):
        self.conn = connection()
        self.modelo_user = User(self.conn)
        self.modelo = User_verification(self.conn)
        self.usuario_existente = UsuarioExistenteError()
    
    def Datos(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        existe = self.modelo.verificar(self.usuario)
        if existe == True:
            raise UsuarioExistenteError("El usuario ya existe")
        
        else:      
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(self.contraseña.encode('utf-8'), salt)
            if self.usuario == "admin1":
                rol = "Administrador"
                self.modelo.agregar(self.usuario, hashed_password, salt,rol)
            else:
                rol = "Empleado"
                self.modelo.agregar(self.usuario,hashed_password, salt,rol)



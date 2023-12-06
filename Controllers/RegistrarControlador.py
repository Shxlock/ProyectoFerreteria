import bcrypt

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

# importaciones necesarias

from Models.User_verification import User_verification
from Controllers.UsuarioExistente import UsuarioExistenteError
from Models.User import User
from Models.empleado import Empleado
from Database.Conection import connection
from Controllers.controladorEmpleados import EmpleadoControlador


class Registrar():
    
    def __init__(self):             # instancias
        self.conn = connection()
        self.empleado = Empleado(self.conn)
        self.modelo_user = User(self.conn)
        self.modelo = User_verification(self.conn)
       
        self.usuario_existente = UsuarioExistenteError()
        self.empleado_controlador = EmpleadoControlador(self)
        
        
    def Datos(self, usuario, contraseña):        # recibimos por parametro los datos q queremos insertar en la base de datos
        cedula = self.empleado.obtenerCedula()        # guardamos el retorno del modelo empleado en cedula
        cedula = int(cedula)
        self.usuario = usuario         
        self.contraseña = contraseña
        existe = self.modelo.verificar(self.usuario)      # usamos el metodo verificar del modelo para asegurarnos que no existe otro empleado con el mismo usuario
        if existe == True:                     
            raise UsuarioExistenteError("El usuario ya existe")     # si existe otro empleado con el mismo usuario levantamos una excepcion, diciendole que ya existe un empleado con ese usuario
        else:      
            salt = bcrypt.gensalt()                                         # generamos un salt unico con ayuda de la libreria bcrypt
            hashed_password = bcrypt.hashpw(self.contraseña.encode('utf-8'), salt)          # le añadimos esta salt a la contraseña encriptada
            if self.usuario == "admin1":
                rol = "Administrador"                       
                self.modelo.agregar(self.usuario, hashed_password, salt, rol, cedula)      # si el usuario es admin1 le añadimos como rol "Administrador"
            else:
                rol = "Empleado"                                                          
                self.modelo.agregar(self.usuario, hashed_password, salt, rol, cedula)    # si es diferente a admin1 le añadirmos como rol "Empleado"

                
        
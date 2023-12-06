
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
 
#importaciones necesarias
 
from PyQt5 import QtWidgets
from Models.User_verification import User_verification
from Controllers.UsuarioExistente import UsuarioExistenteError
from Models.empleado import Empleado
from Models.User import User
from Models.User_login import User_login
from Database.Conection import connection


class LogInController():
    def __init__(self):
        self.conn = connection()          # instancia de la coneccion a la base de datos
        self.modelo_empleado = Empleado(self.conn)     # modelo empleado
        self.modelo_user = User(self.conn)            # modelo usuario
        self.modelo_user_login = User_login(self.conn)        
        self.modelo = User_verification(self.conn)
        self.usuario_existente = UsuarioExistenteError()

    def log_in(self, usuario, contraseña,Administrador,Empleado,Ui_Dialog): # este metodo recibe 4 parametros, el usuario, la contraseña, la ventana que va a abrir (Administrador o Empleado) y la ventana que va a cerrar (Ui_Dialog)
        existe = self.modelo.verificar(usuario)        # verificamos si el usuario existe en la base de datos
        if existe:                                      
            user_login = self.modelo_user_login.Log_In(usuario, contraseña)    # si si existe procedemos a enviar los datos
            if user_login == True:                                                   # si nos retorna true quiere decir que las credenciales son correctas
                self.autenticar(usuario,contraseña,Administrador,Empleado,Ui_Dialog)
                return True                            # devolvemos true 
        return False         # si no, devolvemos False 

    def autenticar(self, usuario, contraseña,Administrador,Empleado,Ui_Dialog):
        if usuario == "admin1" and contraseña == "admin123":         # verificamos is el usuario es admin1 y contraseña admin123
            rol = "Administrador"                                # Si es asi mostramos la interfaz de administrador
            self.Dialog = QtWidgets.QMainWindow()                        # mostramos la ventana
            self.Dialog.ui = Administrador()
            self.Dialog.ui.setupUi(self.Dialog)
            self.Dialog.show()
            print("Eres admin")
        else:                                                   # si no es admin1 y admin123 mostramos la interfaz de empleado
            rol = "Empleado"
            self.Dialog = QtWidgets.QMainWindow()
            self.Dialog.ui = Empleado()
            self.Dialog.ui.setupUi(self.Dialog)
            self.Dialog.show()
            print("Eres empleado")
        
       
       
        
 

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Models.User_verification import User_verification
from Controllers.UsuarioExistente import UsuarioExistenteError
from Models.User import User
from Models.User_login import User_login
from Database.Conection import connection
from Controllers.UsuarioExistente import UsuarioExistenteError



class LogInController():
    
    def __init__(self):
        self.conn = connection()
        self.modelo_user = User(self.conn)
        self.modelo_user_login = User_login(self.conn)
        self.modelo = User_verification(self.conn)
        self.usuario_existente = UsuarioExistenteError()


    
       
    def log_in(self, usuario, contraseña,Administrador,Empleado,Ui_Dialog):
        existe = self.modelo.verificar(usuario)
        if existe:
            user_login = self.modelo_user_login.Log_In(usuario, contraseña)
            if user_login == True:
                self.autenticar(usuario,contraseña,Administrador,Empleado,Ui_Dialog)
                return True
        return False

    def autenticar(self, usuario, contraseña,Administrador,Empleado,Ui_Dialog):
        if usuario == "admin1" and contraseña == "admin123":
            rol = "Administrador"
            self.Dialog = QtWidgets.QMainWindow()
            self.Dialog.ui = Administrador()
            self.Dialog.ui.setupUi(self.Dialog)
            self.Dialog.show()
            print("Eres admin")
        else:
            rol = "Empleado"
            self.Dialog = QtWidgets.QMainWindow()
            self.Dialog.ui = Empleado()
            self.Dialog.ui.setupUi(self.Dialog)
            self.Dialog.show()
            print("Eres empleado")
        
       
       
        
 
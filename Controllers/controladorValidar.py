
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtWidgets
import re

class ValidarControlador():
    def __init__(self,principal):
        
        self.principal = principal
        self.MENSAJE_CAMPOS_VACIOS = "Por favor, rellena todas las casillas."
        self.MENSAJE_DOCUMENTO_NO_VALIDO = "Documento no válido"
        self.MENSAJE_EMAIL_NO_VALIDO = "Por favor, ingresa un correo electrónico válido."
        self.MENSAJE_TODO_CORRECTO = "Datos Enviados!"

        
    def validarEmail(self,email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None

    def validarDocumento(self, documento):
        if documento.isdigit() and len(documento) >= 10:
            return True
        else:
            return False

    def validarTelefono(self,telefono):
        if isinstance(telefono, int):
            print("es telefono")
            return len(str(telefono)) == 10
        else:
            return False

    def validarDatos(self, datos):
        for campo in datos:
            if campo == "":
                print("Negativo")
                return False
        print("Positivo")
        return True
    
    def mostrarMensaje(self,mensaje,titulo):
        mensaje_box = QMessageBox()
        mensaje_box.setIcon(QMessageBox.Information)
        mensaje_box.setText(mensaje)
        mensaje_box.setWindowTitle(titulo)
        mensaje_box.exec_()
    
    
    def validarVenta(self, codigo, cantidad):
        cantidad = int(cantidad)
        return len(codigo) > 0 and cantidad > 0
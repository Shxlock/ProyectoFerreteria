# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\registrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.RegistrarControlador import Registrar
from Controllers.UsuarioExistente import UsuarioExistenteError

class Ui_Dialog(object):
    
    def __init__(self):
        self.registro_controlador = Registrar()
        self.usuario_existe = UsuarioExistenteError()
        
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Registrar Empleado")
        Dialog.resize(326, 300)
        self.lbl_Registrar = QtWidgets.QLabel(Dialog)
        self.lbl_Registrar.setGeometry(QtCore.QRect(-40, 0, 411, 51))
        self.lbl_Registrar.setStyleSheet("background-color: rgb(12, 67, 139);\n"
"font: 87 14pt \"Arial Black\";\n"
"color: rgb(243, 243, 243);")
        self.lbl_Registrar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Registrar.setObjectName("lbl_Registrar")
        self.lbl_espacioEnBlanco_2 = QtWidgets.QLabel(Dialog)
        self.lbl_espacioEnBlanco_2.setEnabled(False)
        self.lbl_espacioEnBlanco_2.setGeometry(QtCore.QRect(0, 50, 330, 10))
        self.lbl_espacioEnBlanco_2.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.lbl_espacioEnBlanco_2.setText("")
        self.lbl_espacioEnBlanco_2.setObjectName("lbl_espacioEnBlanco_2")
        self.lbl_degradadoAzul = QtWidgets.QLabel(Dialog)
        self.lbl_degradadoAzul.setGeometry(QtCore.QRect(0, 60, 331, 231))
        self.lbl_degradadoAzul.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.0511364 rgba(16, 93, 140, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 87 8pt \"Arial Black\";\n"
"font: 87 10pt \"Arial Black\";")
        self.lbl_degradadoAzul.setText("")
        self.lbl_degradadoAzul.setObjectName("lbl_degradadoAzul")
        self.lbl_alertaUsuarioContrasenia_2 = QtWidgets.QLabel(Dialog)
        self.lbl_alertaUsuarioContrasenia_2.setGeometry(QtCore.QRect(0, 281, 331, 20))
        self.lbl_alertaUsuarioContrasenia_2.setStyleSheet("background-color: rgb(253, 253, 253);")
        self.lbl_alertaUsuarioContrasenia_2.setText("")
        self.lbl_alertaUsuarioContrasenia_2.setObjectName("lbl_alertaUsuarioContrasenia_2")
        self.inputUsuario = QtWidgets.QLineEdit(Dialog)
        self.inputUsuario.setGeometry(QtCore.QRect(90, 110, 151, 21))
        self.inputUsuario.setObjectName("inputUsuario")
        self.inputContrasenia = QtWidgets.QLineEdit(Dialog)
        self.inputContrasenia.setGeometry(QtCore.QRect(90, 160, 151, 21))
        self.inputContrasenia.setObjectName("inputContrasenia")
        self.BtnIngresar_2 = QtWidgets.QPushButton(Dialog)
        self.BtnIngresar_2.setGeometry(QtCore.QRect(130, 210, 75, 23))
        self.BtnIngresar_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.0511364 rgba(16, 93, 140, 255), stop:1 rgba(255, 255, 255, 255));")
        self.BtnIngresar_2.setObjectName("BtnIngresar_2")
        self.BtnIngresar_2.clicked.connect(self.obtenerDatos)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Registrar Empleado", "Registrar Empleado"))
        self.lbl_Registrar.setText(_translate("Registrar Empleado", "Registrar"))
        self.inputUsuario.setPlaceholderText(_translate("Registrar Empleado", "Crea usuario"))
        self.inputContrasenia.setPlaceholderText(_translate("Registrar Empleado", "crea contraseña"))
        self.BtnIngresar_2.setText(_translate("Registrar Empleado", "Registrar"))
        

    def obtenerDatos(self):
        usuario = str(self.inputUsuario.text())
        contraseña = str(self.inputContrasenia.text())
        try:
            self.registro_controlador.Datos(usuario,contraseña)
            self.lbl_alertaUsuarioContrasenia_2.setText("Usuario registrado correctamente.")
            self.lbl_alertaUsuarioContrasenia_2.setStyleSheet('background:green;color:white')
        except UsuarioExistenteError as e:
            self.lbl_alertaUsuarioContrasenia_2.setText(str(e))
            self.lbl_alertaUsuarioContrasenia_2.setStyleSheet('background:tomato;color:white')

    


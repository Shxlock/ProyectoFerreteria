# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opcionesProveedores.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Recursos.imagenesPyQt5_rc import *
from Controllers.controladorProveedores import ControladorProveedores
from PyQt5.QtGui import QIntValidator

class OpcionesProveedores(object):
    
    def __init__(self):
        self.opciones_proveedor = ControladorProveedores(self)
        self.int_validator = QIntValidator()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 468)
        Dialog.setFixedSize(711, 468) 
        icon = QtGui.QIcon("Recursos/proveedor.ico")  # Ruta de la imagen del icono
        Dialog.setWindowIcon(icon)
        self.btnModificarProveedor = QtWidgets.QPushButton(Dialog)
        self.btnModificarProveedor.setGeometry(QtCore.QRect(540, 440, 121, 23))
        self.btnModificarProveedor.setObjectName("btnModificarProveedor")
        self.btnModificarProveedor.setEnabled(False)
        self.btnModificarProveedor.clicked.connect(self.opciones_proveedor.cambiarProveedor)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(560, 160, 101, 16))
        self.label_16.setObjectName("label_16")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(243, 30, 20, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.eliminarProveedor = QtWidgets.QComboBox(Dialog)
        self.eliminarProveedor.setGeometry(QtCore.QRect(380, 90, 69, 22))
        self.eliminarProveedor.setObjectName("eliminarProveedor")
        self.codigo_modificar_producto = QtWidgets.QLineEdit(Dialog)
        self.codigo_modificar_producto.setGeometry(QtCore.QRect(560, 70, 113, 20))
        self.codigo_modificar_producto.setObjectName("codigo_modificar_producto")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 100, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.modificarProveedor)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(470, 140, 231, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(270, 90, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 31))
        self.label.setStyleSheet("background-color: rgb(145, 145, 145);\n"
"font: 87 14pt \"Arial Black\";\n"
"color: rgb(249, 249, 249);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 51, 16))
        self.label_3.setObjectName("label_3")
        self.btnEliminarProveedor = QtWidgets.QPushButton(Dialog)
        self.btnEliminarProveedor.setGeometry(QtCore.QRect(300, 150, 121, 23))
        self.btnEliminarProveedor.setObjectName("btnEliminarProveedor")
        self.btnEliminarProveedor.clicked.connect(self.EliminarProveedor)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(510, 70, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(480, 190, 91, 16))
        self.label_12.setObjectName("label_12")
        self.nuevo_nombre_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nuevo_nombre_proveedor.setGeometry(QtCore.QRect(580, 190, 113, 20))
        self.nuevo_nombre_proveedor.setObjectName("nuevo_nombre_proveedor")
        self.nuevo_nombre_proveedor.setReadOnly(True)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(460, 30, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.BtnAgregarProveedor = QtWidgets.QPushButton(Dialog)
        self.BtnAgregarProveedor.setGeometry(QtCore.QRect(70, 340, 121, 23))
        self.BtnAgregarProveedor.setObjectName("BtnAgregarProveedor")
        self.BtnAgregarProveedor.clicked.connect(self.agregarProveedor)
        self.codigo_proveedor = QtWidgets.QLineEdit(Dialog)
        self.codigo_proveedor.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.codigo_proveedor.setObjectName("codigo_proveedor")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_5.setObjectName("label_5")
        self.nombre_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nombre_proveedor.setGeometry(QtCore.QRect(120, 130, 113, 20))
        self.nombre_proveedor.setObjectName("nombre_proveedor")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(570, 0, 41, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/logoFerreteria/logoferreteria.png-HD.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(60, 40, 141, 21))
        self.label_13.setStyleSheet("font: 8pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(290, 40, 141, 21))
        self.label_14.setStyleSheet("font: 8pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(520, 40, 141, 21))
        self.label_15.setStyleSheet("font: 8pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.telefono_proveedor = QtWidgets.QLineEdit(Dialog)
        self.telefono_proveedor.setGeometry(QtCore.QRect(120, 180, 113, 20))
        self.telefono_proveedor.setObjectName("telefono_proveedor")
        self.telefono_proveedor.setValidator(self.int_validator)
        self.email_proveedor = QtWidgets.QLineEdit(Dialog)
        self.email_proveedor.setGeometry(QtCore.QRect(120, 220, 113, 20))
        self.email_proveedor.setObjectName("email_proveedor")
        self.direccion_proveedor = QtWidgets.QLineEdit(Dialog)
        self.direccion_proveedor.setGeometry(QtCore.QRect(120, 260, 113, 20))
        self.direccion_proveedor.setObjectName("direccion_proveedor")
        self.ciudad_proveedor = QtWidgets.QLineEdit(Dialog)
        self.ciudad_proveedor.setGeometry(QtCore.QRect(120, 300, 113, 20))
        self.ciudad_proveedor.setObjectName("ciudad_proveedor")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 91, 16))
        self.label_8.setObjectName("label_8")
        self.nueva_ciudad_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nueva_ciudad_proveedor.setGeometry(QtCore.QRect(580, 350, 113, 20))
        self.nueva_ciudad_proveedor.setObjectName("nueva_ciudad_proveedor")
        self.nueva_ciudad_proveedor.setReadOnly(True)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(480, 350, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(480, 230, 101, 16))
        self.label_17.setObjectName("label_17")
        self.nuevo_email_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nuevo_email_proveedor.setGeometry(QtCore.QRect(580, 270, 113, 20))
        self.nuevo_email_proveedor.setObjectName("nuevo_email_proveedor")
        self.nuevo_email_proveedor.setReadOnly(True)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(480, 270, 81, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(480, 310, 101, 16))
        self.label_19.setObjectName("label_19")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(1000, 490, 121, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.nuevo_telefono_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nuevo_telefono_proveedor.setGeometry(QtCore.QRect(580, 230, 113, 20))
        self.nuevo_telefono_proveedor.setObjectName("nuevo_telefono_proveedor")
        self.nuevo_telefono_proveedor.setReadOnly(True)
        self.nueva_direccion_proveedor = QtWidgets.QLineEdit(Dialog)
        self.nueva_direccion_proveedor.setGeometry(QtCore.QRect(580, 310, 113, 20))
        self.nueva_direccion_proveedor.setObjectName("nueva_direccion_proveedor")
        self.nueva_direccion_proveedor.setReadOnly(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.opciones_proveedor.comboProveedor()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Opciones Proveedores", "Opciones Proveedores"))
        self.btnModificarProveedor.setText(_translate("Dialog", "Modificar Producto"))
        self.label_16.setText(_translate("Dialog", "Nuevos Valores"))
        self.pushButton_3.setText(_translate("Dialog", "Buscar"))
        self.label_9.setText(_translate("Dialog", "Proveedor a eliminar"))
        self.label.setText(_translate("Dialog", "Proveedores"))
        self.label_3.setText(_translate("Dialog", "Codigo"))
        self.btnEliminarProveedor.setText(_translate("Dialog", "Eliminar Proveedor"))
        self.label_11.setText(_translate("Dialog", "Codigo"))
        self.label_12.setText(_translate("Dialog", "Nombre Proveedor"))
        self.BtnAgregarProveedor.setText(_translate("Dialog", "Agregar Proveedor"))
        self.label_5.setText(_translate("Dialog", "Nombre Proveedor"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Agregar Proveedor</span></p><p><br/></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Eliminar Proveedor</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Modificar Proveedor</span></p><p><br/></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "Telefono Proveedor"))
        self.label_2.setText(_translate("Dialog", "Email Proveedor"))
        self.label_7.setText(_translate("Dialog", "Direccion Proveedor"))
        self.label_8.setText(_translate("Dialog", "Ciudad Proveedor"))
        self.label_10.setText(_translate("Dialog", "Ciudad Proveedor"))
        self.label_17.setText(_translate("Dialog", "Telefono Proveedor"))
        self.label_18.setText(_translate("Dialog", "Email Proveedor"))
        self.label_19.setText(_translate("Dialog", "Direccion Proveedor"))
        self.pushButton_5.setText(_translate("Dialog", "Modificar Producto"))
        
    def agregarProveedor(self):
        codigo = self.codigo_proveedor.text()
        nombre = self.nombre_proveedor.text()
        telefono = self.telefono_proveedor.text()
        email = self.email_proveedor.text()
        direccion = self.direccion_proveedor.text()
        ciudad = self.ciudad_proveedor.text()
        self.opciones_proveedor.agregarProveedor(codigo,nombre,telefono,email,direccion,ciudad)

    def EliminarProveedor(self):
        elemento_seleccionado = self.eliminarProveedor.currentText()
        print(elemento_seleccionado)
        self.opciones_proveedor.eliminarProveedor(elemento_seleccionado)

    def modificarProveedor(self):
        nit = self.codigo_modificar_producto.text()
        print(nit)
        self.opciones_proveedor.modificarProveedor(nit)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = OpcionesProveedores()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

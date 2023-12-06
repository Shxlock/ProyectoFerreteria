# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminResponsive.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtCore import QPropertyAnimation,QDate
from PyQt5.QtGui import QIntValidator


from Controllers.controladorPrincipal import PrincipalControlador
from Controllers.controladorVentas import VentaControlador
from Controllers.controladorFacturas import FacturaControlador
from Views.opcionesEmpleados import OpcionesEmpleados
from Views.opcionesProductos import OpcionesProductos
from Views.opcionesProveedores import OpcionesProveedores
        
class Administrador(object):
    def __init__(self):
        self.principal_controlador = PrincipalControlador(self)
        self.ventas = VentaControlador(self)
        self.facturas = FacturaControlador(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_encabezado = QtWidgets.QFrame(self.centralwidget)
        self.frame_encabezado.setMinimumSize(QtCore.QSize(90, 60))
        self.frame_encabezado.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_encabezado.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.frame_encabezado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_encabezado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_encabezado.setObjectName("frame_encabezado")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_encabezado)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_encabezado)
        self.frame.setMinimumSize(QtCore.QSize(200, 70))
        self.frame.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.menu_opciones = QtWidgets.QPushButton(self.frame)
        self.menu_opciones.setMinimumSize(QtCore.QSize(100, 40))
        self.menu_opciones.setMaximumSize(QtCore.QSize(100, 16777215))
        self.menu_opciones.setAutoFillBackground(False)
        self.menu_opciones.setStyleSheet("border-radius:50%;\n"
"image: url(:/logoFerreteria/menu.png);\n"
"\n"
"")
        self.menu_opciones.setText("")
        self.menu_opciones.setFlat(True)
        self.menu_opciones.setObjectName("menu_opciones")
        self.menu_opciones.clicked.connect(self.menu)
        self.gridLayout_3.addWidget(self.menu_opciones, 0, 0, 1, 1)
        self.nombre_ferreteria = QtWidgets.QLabel(self.frame)
        self.nombre_ferreteria.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.nombre_ferreteria.setObjectName("nombre_ferreteria")
        self.gridLayout_3.addWidget(self.nombre_ferreteria, 0, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMinimumSize(QtCore.QSize(100, 10))
        self.logo.setMaximumSize(QtCore.QSize(100, 40))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logoFerreteria/logoferreteria.png-HD.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout_3.addWidget(self.logo, 0, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_encabezado)
        self.frame_principal = QtWidgets.QFrame(self.centralwidget)
        self.frame_principal.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_principal.setMaximumSize(QtCore.QSize(30000, 16777215))
        self.frame_principal.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"\n"
"")
        self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_principal)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(self.frame_principal)
        self.frame_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu.setStyleSheet("margin: 10px;\n"
"background-color: rgb(214, 214, 214);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nombre_menu = QtWidgets.QLabel(self.frame_menu)
        self.nombre_menu.setMinimumSize(QtCore.QSize(100, 50))
        self.nombre_menu.setMaximumSize(QtCore.QSize(1000, 50))
        self.nombre_menu.setObjectName("nombre_menu")
        self.verticalLayout_2.addWidget(self.nombre_menu)
        self.nombre_edit = QtWidgets.QLineEdit(self.frame_menu)
        self.nombre_edit.setObjectName("nombre_edit")
        self.verticalLayout_2.addWidget(self.nombre_edit)
        self.email_menu = QtWidgets.QLabel(self.frame_menu)
        self.email_menu.setMinimumSize(QtCore.QSize(50, 50))
        self.email_menu.setMaximumSize(QtCore.QSize(50, 50))
        self.email_menu.setObjectName("email_menu")
        self.verticalLayout_2.addWidget(self.email_menu)
        self.email_edit = QtWidgets.QLineEdit(self.frame_menu)
        self.email_edit.setObjectName("email_edit")
        self.verticalLayout_2.addWidget(self.email_edit)
        self.label_3 = QtWidgets.QLabel(self.frame_menu)
        self.label_3.setMinimumSize(QtCore.QSize(100, 50))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.numero_edit = QtWidgets.QLineEdit(self.frame_menu)
        self.numero_edit.setObjectName("numero_edit")
        self.verticalLayout_2.addWidget(self.numero_edit)
        self.pushButton = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 9px;\n"
"padding-top: 19px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_menu)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_ferreteria = QtWidgets.QFrame(self.frame_principal)
        self.frame_ferreteria.setStyleSheet("")
        self.frame_ferreteria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ferreteria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ferreteria.setObjectName("frame_ferreteria")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_ferreteria)
        self.verticalLayout_3.setContentsMargins(50, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_superior = QtWidgets.QFrame(self.frame_ferreteria)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_superior)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_superior)
        self.frame_5.setMinimumSize(QtCore.QSize(280, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnProductos = QtWidgets.QPushButton(self.frame_5)
        self.btnProductos.setMinimumSize(QtCore.QSize(10, 10))
        self.btnProductos.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnProductos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProductos.setObjectName("btnProductos")
        self.btnProductos.clicked.connect(self.abrirProductos)
        self.horizontalLayout_5.addWidget(self.btnProductos)
        self.btnProveedores = QtWidgets.QPushButton(self.frame_5)
        self.btnProveedores.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnProveedores.setObjectName("btnProveedores")
        self.btnProveedores.clicked.connect(self.abrirProveedores)
        self.horizontalLayout_5.addWidget(self.btnProveedores)
        self.btnHistorialVentas = QtWidgets.QPushButton(self.frame_5)
        self.btnHistorialVentas.setMaximumSize(QtCore.QSize(90, 16777215))
        self.btnHistorialVentas.setObjectName("btnHistorialVentas")
        self.horizontalLayout_5.addWidget(self.btnHistorialVentas)
        self.btnEmpleados = QtWidgets.QPushButton(self.frame_5)
        self.btnEmpleados.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnEmpleados.setObjectName("btnEmpleados")
        self.btnEmpleados.clicked.connect(self.abrirVentana)
        self.horizontalLayout_5.addWidget(self.btnEmpleados)
        self.btnClientes = QtWidgets.QPushButton(self.frame_5)
        self.btnClientes.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btnClientes.setObjectName("btnClientes")
        self.horizontalLayout_5.addWidget(self.btnClientes)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_superior)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblBuscar = QtWidgets.QLabel(self.frame_6)
        self.lblBuscar.setMaximumSize(QtCore.QSize(93, 16777215))
        self.lblBuscar.setObjectName("lblBuscar")
        self.gridLayout_4.addWidget(self.lblBuscar, 0, 0, 1, 1)
        self.buscarProducto = QtWidgets.QLineEdit(self.frame_6)
        self.buscarProducto.setMinimumSize(QtCore.QSize(100, 0))
        self.buscarProducto.setMaximumSize(QtCore.QSize(300, 16777215))
        self.buscarProducto.setObjectName("buscarProducto")
        self.buscarProducto.textChanged.connect(self.buscador)
        self.gridLayout_4.addWidget(self.buscarProducto, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_superior)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setContentsMargins(25, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_48 = QtWidgets.QLabel(self.frame_8)
        self.label_48.setMinimumSize(QtCore.QSize(90, 0))
        self.label_48.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 0, 2, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.frame_8)
        self.label_50.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(60, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.frame_8)
        self.label_47.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 0, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.frame_8)
        self.label_49.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 0, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.frame_8)
        self.label_51.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 0, 5, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_2.setContentsMargins(60, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnAgregarVenta = QtWidgets.QPushButton(self.frame_9)
        self.btnAgregarVenta.setMinimumSize(QtCore.QSize(0, 6))
        self.btnAgregarVenta.setMaximumSize(QtCore.QSize(100, 25))
        self.btnAgregarVenta.setObjectName("btnAgregarVenta")
        self.btnAgregarVenta.clicked.connect(self.venta)
        self.gridLayout_2.addWidget(self.btnAgregarVenta, 0, 1, 1, 1)
        self.codigoProducto = QtWidgets.QLineEdit(self.frame_9)
        self.codigoProducto.setMaximumSize(QtCore.QSize(60, 16777215))
        self.codigoProducto.setObjectName("codigoProducto")
        self.gridLayout_2.addWidget(self.codigoProducto, 0, 0, 1, 1)
        self.nombreProducto = QtWidgets.QLineEdit(self.frame_9)
        self.nombreProducto.setMaximumSize(QtCore.QSize(120, 16777215))
        self.nombreProducto.setObjectName("nombreProducto")
        self.gridLayout_2.addWidget(self.nombreProducto, 0, 2, 1, 1)
        self.cantidadProducto = QtWidgets.QSpinBox(self.frame_9)
        self.cantidadProducto.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cantidadProducto.setObjectName("cantidadProducto")
        self.gridLayout_2.addWidget(self.cantidadProducto, 0, 3, 1, 1)
        self.precioUnitario = QtWidgets.QLineEdit(self.frame_9)
        self.precioUnitario.setMaximumSize(QtCore.QSize(120, 16777215))
        self.precioUnitario.setObjectName("precioUnitario")
        self.gridLayout_2.addWidget(self.precioUnitario, 0, 5, 1, 1)
        self.montoTotal = QtWidgets.QLineEdit(self.frame_9)
        self.montoTotal.setMaximumSize(QtCore.QSize(150, 16777215))
        self.montoTotal.setObjectName("montoTotal")
        self.gridLayout_2.addWidget(self.montoTotal, 0, 6, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(self.frame_ferreteria)
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_seccion_ventas = QtWidgets.QFrame(self.frame_inferior)
        self.frame_seccion_ventas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_seccion_ventas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_seccion_ventas.setObjectName("frame_seccion_ventas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_seccion_ventas)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_seccion_ventas)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnActualizar = QtWidgets.QPushButton(self.frame_2)
        self.btnActualizar.setMinimumSize(QtCore.QSize(120, 20))
        self.btnActualizar.setMaximumSize(QtCore.QSize(120, 10))
        self.btnActualizar.setStyleSheet("")
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnActualizar.clicked.connect(self.principal_controlador.actualizar)
        self.verticalLayout_7.addWidget(self.btnActualizar)
        self.tablaProductos = QtWidgets.QTableWidget(self.frame_2)
        self.tablaProductos.setObjectName("tablaProductos")
        self.tablaProductos.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(6, item)
        self.tablaProductos.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.verticalLayout_7.addWidget(self.tablaProductos)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_seccion_ventas)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 20, 0, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tablaVentas = QtWidgets.QTableWidget(self.frame_3)
        self.tablaVentas.setObjectName("tablaVentas")
        self.tablaVentas.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVentas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaVentas.setHorizontalHeaderItem(4, item)
        self.tablaVentas.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.verticalLayout_8.addWidget(self.tablaVentas)
        self.btnEliminarVenta = QtWidgets.QPushButton(self.frame_3)
        self.btnEliminarVenta.setMinimumSize(QtCore.QSize(120, 20))
        self.btnEliminarVenta.setMaximumSize(QtCore.QSize(120, 10))
        self.btnEliminarVenta.setObjectName("btnEliminarVenta")
        self.btnEliminarVenta.clicked.connect(self.ventas.borrarFila)
        self.verticalLayout_8.addWidget(self.btnEliminarVenta)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_seccion_ventas)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_43 = QtWidgets.QLabel(self.frame_10)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_9.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.frame_10)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_9.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.frame_10)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_9.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(self.frame_10)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_9.addWidget(self.label_46)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.valorVenta = QtWidgets.QLineEdit(self.frame_11)
        self.valorVenta.setObjectName("valorVenta")
        self.valorVenta.setReadOnly(True)
        self.horizontalLayout_10.addWidget(self.valorVenta)
        self.Descuento = QtWidgets.QLineEdit(self.frame_11)
        self.Descuento.setObjectName("Descuento")
        self.horizontalLayout_10.addWidget(self.Descuento)
        self.subTotal = QtWidgets.QLineEdit(self.frame_11)
        self.subTotal.setObjectName("subTotal")
        self.subTotal.setReadOnly(True)
        self.horizontalLayout_10.addWidget(self.subTotal)
        self.total = QtWidgets.QLineEdit(self.frame_11)
        self.total.setObjectName("total")
        self.total.setReadOnly(True)
        self.horizontalLayout_10.addWidget(self.total)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_4.addWidget(self.frame_seccion_ventas)
        self.frame_facturas = QtWidgets.QFrame(self.frame_inferior)
        self.frame_facturas.setMinimumSize(QtCore.QSize(280, 200))
        self.frame_facturas.setMaximumSize(QtCore.QSize(280, 16777215))
        self.frame_facturas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_facturas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_facturas.setObjectName("frame_facturas")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_facturas)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_facturas)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_40 = QtWidgets.QLabel(self.frame_15)
        self.label_40.setMinimumSize(QtCore.QSize(10, 10))
        self.label_40.setStyleSheet("margin-top:17px;")
        self.label_40.setIndent(-1)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_12.addWidget(self.label_40)
        self.label_53 = QtWidgets.QLabel(self.frame_15)
        self.label_53.setStyleSheet("margin-top:10px;")
        self.label_53.setObjectName("label_53")
        self.verticalLayout_12.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.frame_15)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_12.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.frame_15)
        self.label_55.setStyleSheet("margin-bottom:12px;")
        self.label_55.setObjectName("label_55")
        self.verticalLayout_12.addWidget(self.label_55)
        self.label_2 = QtWidgets.QLabel(self.frame_15)
        self.label_2.setStyleSheet("margin-bottom: 15px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.label_56 = QtWidgets.QLabel(self.frame_15)
        self.label_56.setStyleSheet("margin-bottom:14px;")
        self.label_56.setObjectName("label_56")
        self.verticalLayout_12.addWidget(self.label_56)
        self.label_57 = QtWidgets.QLabel(self.frame_15)
        self.label_57.setStyleSheet("margin-bottom:30px;")
        self.label_57.setObjectName("label_57")
        self.verticalLayout_12.addWidget(self.label_57)
        self.horizontalLayout_11.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")         
        self.fechaFactura = QtWidgets.QDateEdit(self.frame_16)
        self.fechaFactura.setObjectName("fechaFactura")
        self.fechaFactura.setCalendarPopup(True)
        self.fechaFactura.setDate(QDate.currentDate())
        self.fechaFactura.calendarWidget().setEnabled(False)
        self.fechaFactura.setDisplayFormat("yyyy-MM-dd")
        self.verticalLayout_13.addWidget(self.fechaFactura)
        self.documento = QtWidgets.QLineEdit(self.frame_16)
        self.documento.setObjectName("documento")
        self.int_validator = QIntValidator()
        self.documento.setValidator(self.int_validator)
        self.verticalLayout_13.addWidget(self.documento)
        self.tipoDePago = QtWidgets.QComboBox(self.frame_16)
        self.tipoDePago.setObjectName("tipoDePago")
        self.tipoDePago.addItem("Efectivo")
        self.tipoDePago.addItem("Tarjeta")
        self.tipoDePago.addItem("Otra/No sabe No responde")
        self.verticalLayout_13.addWidget(self.tipoDePago)
        self.vendedor = QtWidgets.QLineEdit(self.frame_16)
        self.vendedor.setObjectName("vendedor")
        self.vendedor.setValidator(self.int_validator)
        self.verticalLayout_13.addWidget(self.vendedor)
        self.email_factura = QtWidgets.QLineEdit(self.frame_16)
        self.email_factura.setObjectName("email")
        self.verticalLayout_13.addWidget(self.email_factura)
        self.cliente = QtWidgets.QLineEdit(self.frame_16)
        self.cliente.setObjectName("cliente")
        self.verticalLayout_13.addWidget(self.cliente)
        self.turnoVendedor = QtWidgets.QComboBox(self.frame_16)
        self.turnoVendedor.setStyleSheet("")
        self.turnoVendedor.setObjectName("turnoVendedor")
        self.turnoVendedor.addItem("Mañana")
        self.turnoVendedor.addItem("Tarde")
        self.turnoVendedor.addItem("Noche")
        self.verticalLayout_13.addWidget(self.turnoVendedor)
        self.horizontalLayout_11.addWidget(self.frame_16)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btnGenerarFactura = QtWidgets.QPushButton(self.frame_14)
        self.btnGenerarFactura.setMinimumSize(QtCore.QSize(30, 39))
        self.btnGenerarFactura.setMaximumSize(QtCore.QSize(90, 40))
        self.btnGenerarFactura.setObjectName("btnGenerarFactura")
        self.btnGenerarFactura.clicked.connect(self.facturas.validarCampos)
        self.horizontalLayout_12.addWidget(self.btnGenerarFactura)
        self.verticalLayout_11.addWidget(self.frame_14)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.horizontalLayout_4.addWidget(self.frame_facturas)
        self.verticalLayout_3.addWidget(self.frame_inferior)
        self.horizontalLayout.addWidget(self.frame_ferreteria)
        self.verticalLayout.addWidget(self.frame_principal)
        self.frame_principal.raise_()
        self.frame_encabezado.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.principal_controlador.actualizar()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_opciones.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.nombre_ferreteria.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-style:italic; color:#4d73c6;\">Aero</span><span style=\" font-size:22pt; font-style:italic; color:#f4340d;\">Norte</span></p></body></html>"))
        self.nombre_menu.setText(_translate("MainWindow", "Nombre"))
        self.email_menu.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Número telefonico"))
        self.pushButton.setText(_translate("MainWindow", "Guardar"))
        self.label.setText(_translate("MainWindow", "Ferretería Aeronorte  - Barrio Aeropuerto"))
        self.btnProductos.setText(_translate("MainWindow", "Productos"))
        self.btnProveedores.setText(_translate("MainWindow", "Proveedores"))
        self.btnHistorialVentas.setText(_translate("MainWindow", "Historial Ventas"))
        self.btnEmpleados.setText(_translate("MainWindow", "Empleados"))
        self.btnClientes.setText(_translate("MainWindow", "Clientes"))
        self.lblBuscar.setText(_translate("MainWindow", "Buscar Producto"))
        self.label_48.setText(_translate("MainWindow", "Nombre Producto"))
        self.label_50.setText(_translate("MainWindow", "Precio Unitario"))
        self.label_47.setText(_translate("MainWindow", "Codigo"))
        self.label_49.setText(_translate("MainWindow", "Cantidad"))
        self.label_51.setText(_translate("MainWindow", "Monto Total"))
        self.btnAgregarVenta.setText(_translate("MainWindow", "Agregar Venta"))
        self.btnActualizar.setText(_translate("MainWindow", "Actualizar Productos"))
        item = self.tablaProductos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tablaProductos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tablaProductos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tablaProductos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.tablaProductos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.tablaProductos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tablaProductos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Proveedor"))
        item = self.tablaVentas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo Venta"))
        item = self.tablaVentas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Codigo Producto"))
        item = self.tablaVentas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tablaVentas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.tablaVentas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cantidad"))
        
        self.btnEliminarVenta.setText(_translate("MainWindow", "Eliminar"))
        self.label_43.setText(_translate("MainWindow", "Valor Venta"))
        self.label_44.setText(_translate("MainWindow", "Descuento"))
        self.label_45.setText(_translate("MainWindow", "Sub Total"))
        self.label_46.setText(_translate("MainWindow", "Total General"))
        self.label_40.setText(_translate("MainWindow", "Fecha"))
        self.label_53.setText(_translate("MainWindow", "Documento"))
        self.label_54.setText(_translate("MainWindow", "Tipo de pago"))
        self.label_55.setText(_translate("MainWindow", "Vendedor"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_56.setText(_translate("MainWindow", "Cliente"))
        self.label_57.setText(_translate("MainWindow", "Turno"))
        self.btnGenerarFactura.setText(_translate("MainWindow", "Generar Factura"))
        
    def menu(self):    
        if True:
            width = self.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 300
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()         
        
    def buscador(self):    
        palabra = self.buscarProducto.text().lower() 
        controlador = self.principal_controlador.buscador(palabra)
        if controlador:
            print("Se ha encontrado")
        else:
            print("No se encontró")
            
    def venta(self,cantidad):
        codigo = self.codigoProducto.text()
        cantidad = self.cantidadProducto.text()
        controlador = self.ventas.agregar_venta(codigo,cantidad)
        if controlador:
            print("Vas bien")         

    def abrirVentana(self):
        self.principal_controlador.abrirVentana(OpcionesEmpleados)
        
    def abrirProductos(self):
        self.principal_controlador.abrirProductos(OpcionesProductos)
        
    def abrirProveedores(self):
        self.principal_controlador.abrirProveedores(OpcionesProveedores)
        
from Recursos.imagenesPyQt5_rc import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Administrador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

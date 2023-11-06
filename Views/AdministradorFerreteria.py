# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministradorFerreteria.ui'
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


class Administrador(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AeroNorte")
        MainWindow.resize(811, 827)
        MainWindow.setFixedSize(811, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 821, 841))
        self.label.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnHistorialVentas = QtWidgets.QPushButton(self.centralwidget)
        self.btnHistorialVentas.setGeometry(QtCore.QRect(370, 100, 101, 23))
        self.btnHistorialVentas.setObjectName("btnHistorialVentas")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(450, 300, 20, 441))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.nombreProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.nombreProducto.setGeometry(QtCore.QRect(300, 230, 91, 20))
        self.nombreProducto.setObjectName("nombreProducto")
        self.turnoVendedor = QtWidgets.QComboBox(self.centralwidget)
        self.turnoVendedor.setGeometry(QtCore.QRect(630, 610, 69, 22))
        self.turnoVendedor.setObjectName("turnoVendedor")
        self.btnGenerarFactura = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarFactura.setGeometry(QtCore.QRect(610, 690, 111, 23))
        self.btnGenerarFactura.setObjectName("btnGenerarFactura")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(540, 560, 71, 21))
        self.label_56.setObjectName("label_56")
        self.btnAgregarVenta = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarVenta.setGeometry(QtCore.QRect(180, 230, 91, 23))
        self.btnAgregarVenta.setObjectName("btnAgregarVenta")
        self.cantidadProducto = QtWidgets.QSpinBox(self.centralwidget)
        self.cantidadProducto.setGeometry(QtCore.QRect(430, 230, 42, 21))
        self.cantidadProducto.setObjectName("cantidadProducto")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(160, 690, 71, 16))
        self.label_44.setObjectName("label_44")
        self.btnProductos = QtWidgets.QPushButton(self.centralwidget)
        self.btnProductos.setGeometry(QtCore.QRect(110, 100, 91, 23))
        self.btnProductos.setObjectName("btnProductos")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(330, 690, 71, 16))
        self.label_46.setObjectName("label_46")
        self.precioUnitario = QtWidgets.QLineEdit(self.centralwidget)
        self.precioUnitario.setGeometry(QtCore.QRect(520, 230, 81, 20))
        self.precioUnitario.setObjectName("precioUnitario")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(640, 310, 61, 21))
        self.label_21.setObjectName("label_21")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(150, 280, 571, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.subTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.subTotal.setGeometry(QtCore.QRect(240, 710, 61, 20))
        self.subTotal.setObjectName("subTotal")
        self.vendedor = QtWidgets.QLineEdit(self.centralwidget)
        self.vendedor.setGeometry(QtCore.QRect(630, 510, 113, 20))
        self.vendedor.setObjectName("vendedor")
        self.areaVentas = QtWidgets.QScrollArea(self.centralwidget)
        self.areaVentas.setGeometry(QtCore.QRect(80, 530, 321, 131))
        self.areaVentas.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.areaVentas.setWidgetResizable(True)
        self.areaVentas.setObjectName("areaVentas")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 319, 129))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setGeometry(QtCore.QRect(0, 10, 51, 16))
        self.label_22.setObjectName("label_22")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 110, 301, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setGeometry(QtCore.QRect(70, 10, 51, 16))
        self.label_41.setObjectName("label_41")
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setGeometry(QtCore.QRect(230, 10, 71, 16))
        self.label_39.setObjectName("label_39")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(300, 0, 16, 131))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_52.setGeometry(QtCore.QRect(140, 10, 71, 16))
        self.label_52.setObjectName("label_52")
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setGeometry(QtCore.QRect(50, 0, 20, 111))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_8.setGeometry(QtCore.QRect(120, 0, 20, 111))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_9.setGeometry(QtCore.QRect(210, 0, 20, 111))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.areaVentas.setWidget(self.scrollAreaWidgetContents_2)
        self.codigoProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.codigoProducto.setGeometry(QtCore.QRect(90, 230, 61, 20))
        self.codigoProducto.setObjectName("codigoProducto")
        self.documento = QtWidgets.QLineEdit(self.centralwidget)
        self.documento.setGeometry(QtCore.QRect(630, 410, 113, 20))
        self.documento.setObjectName("documento")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(340, 790, 201, 16))
        self.label_59.setStyleSheet("font: 8pt \"Palatino Linotype\";")
        self.label_59.setObjectName("label_59")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(120, 20, 561, 41))
        self.label_37.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(145, 145, 145);\n"
"color: rgb(248, 248, 248);")
        self.label_37.setText("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.lblBuscar = QtWidgets.QLabel(self.centralwidget)
        self.lblBuscar.setGeometry(QtCore.QRect(110, 160, 81, 16))
        self.lblBuscar.setObjectName("lblBuscar")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(630, 160, 51, 21))
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(540, 410, 61, 21))
        self.label_53.setObjectName("label_53")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(430, 200, 51, 16))
        self.label_49.setObjectName("label_49")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(660, 200, 91, 16))
        self.label_51.setObjectName("label_51")
        self.fechaFactura = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaFactura.setGeometry(QtCore.QRect(630, 360, 110, 22))
        self.fechaFactura.setObjectName("fechaFactura")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(90, 200, 47, 13))
        self.label_47.setObjectName("label_47")
        self.areaProductos = QtWidgets.QScrollArea(self.centralwidget)
        self.areaProductos.setGeometry(QtCore.QRect(80, 300, 321, 191))
        self.areaProductos.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.areaProductos.setWidgetResizable(True)
        self.areaProductos.setObjectName("areaProductos")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 319, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(190, 10, 51, 16))
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(50, 0, 20, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(110, 0, 20, 191))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setGeometry(QtCore.QRect(170, 0, 20, 191))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(0, 170, 301, 20))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setGeometry(QtCore.QRect(250, 10, 51, 16))
        self.label_42.setObjectName("label_42")
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setGeometry(QtCore.QRect(230, 0, 20, 191))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(300, 0, 16, 191))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.areaProductos.setWidget(self.scrollAreaWidgetContents)
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(540, 460, 71, 21))
        self.label_54.setObjectName("label_54")
        self.btnEmpleados = QtWidgets.QPushButton(self.centralwidget)
        self.btnEmpleados.setGeometry(QtCore.QRect(510, 100, 101, 23))
        self.btnEmpleados.setObjectName("btnEmpleados")
        self.montoTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.montoTotal.setGeometry(QtCore.QRect(660, 230, 91, 20))
        self.montoTotal.setObjectName("montoTotal")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(300, 200, 91, 16))
        self.label_48.setObjectName("label_48")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(540, 360, 61, 21))
        self.label_40.setObjectName("label_40")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(240, 690, 71, 16))
        self.label_45.setObjectName("label_45")
        self.tipoDePago = QtWidgets.QComboBox(self.centralwidget)
        self.tipoDePago.setGeometry(QtCore.QRect(630, 460, 69, 22))
        self.tipoDePago.setObjectName("tipoDePago")
        self.cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.cliente.setGeometry(QtCore.QRect(630, 560, 113, 20))
        self.cliente.setObjectName("cliente")
        self.btnProveedores = QtWidgets.QPushButton(self.centralwidget)
        self.btnProveedores.setGeometry(QtCore.QRect(240, 100, 91, 23))
        self.btnProveedores.setObjectName("btnProveedores")
        self.menuOpciones = QtWidgets.QPushButton(self.centralwidget)
        self.menuOpciones.setGeometry(QtCore.QRect(50, 10, 41, 61))
        self.menuOpciones.setAutoFillBackground(False)
        self.menuOpciones.setStyleSheet("border-radius:50%;\n"
"image: url(:/logoFerreteria/menu.png);\n"
"\n"
"")
        self.menuOpciones.setText("")
        self.menuOpciones.setFlat(True)
        self.menuOpciones.setObjectName("menuOpciones")
        self.buscarProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.buscarProducto.setGeometry(QtCore.QRect(230, 160, 351, 20))
        self.buscarProducto.setObjectName("buscarProducto")
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setGeometry(QtCore.QRect(540, 610, 71, 21))
        self.label_57.setObjectName("label_57")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(320, 710, 81, 20))
        self.total.setObjectName("total")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(710, 20, 51, 41))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap(":/logoFerreteria/logoferreteria.png-HD.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.valorVenta = QtWidgets.QLineEdit(self.centralwidget)
        self.valorVenta.setGeometry(QtCore.QRect(80, 710, 71, 20))
        self.valorVenta.setObjectName("valorVenta")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(80, 690, 71, 16))
        self.label_43.setObjectName("label_43")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(330, 20, 141, 41))
        self.label_58.setObjectName("label_58")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(80, 270, 61, 21))
        self.label_19.setObjectName("label_19")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(520, 200, 91, 16))
        self.label_50.setObjectName("label_50")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(540, 510, 71, 21))
        self.label_55.setObjectName("label_55")
        self.Descuento = QtWidgets.QLineEdit(self.centralwidget)
        self.Descuento.setGeometry(QtCore.QRect(160, 710, 61, 20))
        self.Descuento.setObjectName("Descuento")
        self.btnClientes = QtWidgets.QPushButton(self.centralwidget)
        self.btnClientes.setGeometry(QtCore.QRect(670, 100, 75, 23))
        self.btnClientes.setObjectName("btnClientes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("AeroNorte", "AeroNorte"))
        self.btnHistorialVentas.setText(_translate("MainWindow", "Historial Ventas"))
        self.btnGenerarFactura.setText(_translate("MainWindow", "Generar Factura"))
        self.label_56.setText(_translate("MainWindow", "Cliente"))
        self.btnAgregarVenta.setText(_translate("MainWindow", "Agregar Venta"))
        self.label_44.setText(_translate("MainWindow", "Descuento"))
        self.btnProductos.setText(_translate("MainWindow", "Productos"))
        self.label_46.setText(_translate("MainWindow", "Total General"))
        self.label_21.setText(_translate("MainWindow", "Factura"))
        self.label_22.setText(_translate("MainWindow", "Producto"))
        self.label_41.setText(_translate("MainWindow", "Cantidad"))
        self.label_39.setText(_translate("MainWindow", "Total a pagar"))
        self.label_52.setText(_translate("MainWindow", "Precio Unitario"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Ferretería AeroNorte - Barrio Aeropuerto</span></p></body></html>"))
        self.lblBuscar.setText(_translate("MainWindow", "Buscar Producto"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.label_53.setText(_translate("MainWindow", "Documento"))
        self.label_49.setText(_translate("MainWindow", "Cantidad"))
        self.label_51.setText(_translate("MainWindow", "Monto Total"))
        self.label_47.setText(_translate("MainWindow", "Codigo"))
        self.label_2.setText(_translate("MainWindow", "Codigo"))
        self.label_3.setText(_translate("MainWindow", "Producto"))
        self.label_4.setText(_translate("MainWindow", "Cantidad"))
        self.label_5.setText(_translate("MainWindow", "Unidad"))
        self.label_42.setText(_translate("MainWindow", "P. Unidad"))
        self.label_54.setText(_translate("MainWindow", "Tipo de pago"))
        self.btnEmpleados.setText(_translate("MainWindow", "Empleados"))
        self.label_48.setText(_translate("MainWindow", "Nombre Producto"))
        self.label_40.setText(_translate("MainWindow", "Fecha"))
        self.label_45.setText(_translate("MainWindow", "Sub Total"))
        self.btnProveedores.setText(_translate("MainWindow", "Proveedores"))
        self.label_57.setText(_translate("MainWindow", "Turno"))
        self.label_43.setText(_translate("MainWindow", "Valor Venta"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#4d73c6;\">Aero</span><span style=\" font-size:22pt; font-style:italic; color:#f4340d;\">Norte</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Productos"))
        self.label_50.setText(_translate("MainWindow", "Precio Unitario"))
        self.label_55.setText(_translate("MainWindow", "Vendedor"))
        self.btnClientes.setText(_translate("MainWindow", "Clientes"))

from Recursos.imagenesPyQt5_rc import *


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Administrador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

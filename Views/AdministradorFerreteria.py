# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AdministradorFerreteria.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Administrador(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 831)
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(90, 510, 321, 131))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 319, 129))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_22.setObjectName("label_22")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 110, 301, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setGeometry(QtCore.QRect(70, 10, 51, 16))
        self.label_41.setObjectName("label_41")
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setGeometry(QtCore.QRect(210, 10, 71, 16))
        self.label_39.setObjectName("label_39")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(300, 0, 16, 131))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_52.setGeometry(QtCore.QRect(130, 10, 71, 16))
        self.label_52.setObjectName("label_52")
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setGeometry(QtCore.QRect(50, 0, 20, 111))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_8.setGeometry(QtCore.QRect(110, 0, 20, 111))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_9.setGeometry(QtCore.QRect(190, 0, 20, 111))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(420, 280, 20, 441))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(570, 580, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 220, 61, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(570, 330, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(570, 530, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_57 = QtWidgets.QLabel(Dialog)
        self.label_57.setGeometry(QtCore.QRect(480, 580, 71, 21))
        self.label_57.setObjectName("label_57")
        self.label_56 = QtWidgets.QLabel(Dialog)
        self.label_56.setGeometry(QtCore.QRect(480, 530, 71, 21))
        self.label_56.setObjectName("label_56")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 640, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(40, 20, 671, 41))
        self.label_37.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(145, 145, 145);\n"
"color: rgb(248, 248, 248);")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(570, 380, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 220, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 690, 81, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(160, 260, 571, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 220, 91, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(630, 220, 91, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 160, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 690, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(220, 480, 61, 21))
        self.label_20.setObjectName("label_20")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(570, 430, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_54 = QtWidgets.QLabel(Dialog)
        self.label_54.setGeometry(QtCore.QRect(480, 430, 71, 21))
        self.label_54.setObjectName("label_54")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 690, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(550, 280, 61, 21))
        self.label_21.setObjectName("label_21")
        self.label_50 = QtWidgets.QLabel(Dialog)
        self.label_50.setGeometry(QtCore.QRect(520, 200, 91, 16))
        self.label_50.setObjectName("label_50")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(570, 480, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(560, 160, 51, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 690, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_44 = QtWidgets.QLabel(Dialog)
        self.label_44.setGeometry(QtCore.QRect(170, 670, 71, 16))
        self.label_44.setObjectName("label_44")
        self.label_38 = QtWidgets.QLabel(Dialog)
        self.label_38.setGeometry(QtCore.QRect(80, 160, 81, 16))
        self.label_38.setObjectName("label_38")
        self.label_40 = QtWidgets.QLabel(Dialog)
        self.label_40.setGeometry(QtCore.QRect(480, 330, 61, 21))
        self.label_40.setObjectName("label_40")
        self.label_45 = QtWidgets.QLabel(Dialog)
        self.label_45.setGeometry(QtCore.QRect(250, 670, 71, 16))
        self.label_45.setObjectName("label_45")
        self.label_51 = QtWidgets.QLabel(Dialog)
        self.label_51.setGeometry(QtCore.QRect(630, 200, 91, 16))
        self.label_51.setObjectName("label_51")
        self.label_55 = QtWidgets.QLabel(Dialog)
        self.label_55.setGeometry(QtCore.QRect(480, 480, 71, 21))
        self.label_55.setObjectName("label_55")
        self.label_49 = QtWidgets.QLabel(Dialog)
        self.label_49.setGeometry(QtCore.QRect(440, 200, 51, 16))
        self.label_49.setObjectName("label_49")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(90, 280, 321, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 319, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(190, 10, 51, 16))
        self.label_4.setObjectName("label_4")
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
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(10, 140, 51, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(70, 40, 51, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setGeometry(QtCore.QRect(70, 60, 51, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(70, 80, 51, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(70, 100, 51, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setGeometry(QtCore.QRect(70, 120, 51, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setGeometry(QtCore.QRect(70, 140, 51, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setGeometry(QtCore.QRect(70, 160, 51, 16))
        self.label_18.setObjectName("label_18")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setGeometry(QtCore.QRect(130, 40, 51, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setGeometry(QtCore.QRect(130, 60, 51, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setGeometry(QtCore.QRect(130, 80, 51, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setGeometry(QtCore.QRect(130, 100, 51, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setGeometry(QtCore.QRect(130, 120, 51, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setGeometry(QtCore.QRect(130, 140, 51, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setGeometry(QtCore.QRect(130, 160, 51, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setGeometry(QtCore.QRect(190, 40, 51, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setGeometry(QtCore.QRect(190, 60, 51, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setGeometry(QtCore.QRect(190, 80, 51, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setGeometry(QtCore.QRect(190, 100, 51, 16))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setGeometry(QtCore.QRect(190, 120, 51, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setGeometry(QtCore.QRect(190, 140, 51, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setGeometry(QtCore.QRect(190, 160, 51, 16))
        self.label_36.setObjectName("label_36")
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_53 = QtWidgets.QLabel(Dialog)
        self.label_53.setGeometry(QtCore.QRect(480, 380, 61, 21))
        self.label_53.setObjectName("label_53")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(520, 220, 81, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_43 = QtWidgets.QLabel(Dialog)
        self.label_43.setGeometry(QtCore.QRect(90, 670, 71, 16))
        self.label_43.setObjectName("label_43")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(90, 260, 61, 21))
        self.label_19.setObjectName("label_19")
        self.label_48 = QtWidgets.QLabel(Dialog)
        self.label_48.setGeometry(QtCore.QRect(320, 200, 91, 16))
        self.label_48.setObjectName("label_48")
        self.label_47 = QtWidgets.QLabel(Dialog)
        self.label_47.setGeometry(QtCore.QRect(100, 200, 47, 13))
        self.label_47.setObjectName("label_47")
        self.label_46 = QtWidgets.QLabel(Dialog)
        self.label_46.setGeometry(QtCore.QRect(340, 670, 71, 16))
        self.label_46.setObjectName("label_46")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(440, 220, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 80, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 80, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 80, 101, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 80, 101, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(610, 80, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_22.setText(_translate("Dialog", "Producto"))
        self.label_41.setText(_translate("Dialog", "Cantidad"))
        self.label_39.setText(_translate("Dialog", "Total a pagar"))
        self.label_52.setText(_translate("Dialog", "Precio Unitario"))
        self.label_57.setText(_translate("Dialog", "Turno"))
        self.label_56.setText(_translate("Dialog", "Cliente"))
        self.pushButton_3.setText(_translate("Dialog", "Generar Factura"))
        self.label_37.setText(_translate("Dialog", "AeroNorte"))
        self.pushButton_2.setText(_translate("Dialog", "Agregar Venta"))
        self.label_20.setText(_translate("Dialog", "Ventas"))
        self.label_54.setText(_translate("Dialog", "Tipo de pago"))
        self.label_21.setText(_translate("Dialog", "Factura"))
        self.label_50.setText(_translate("Dialog", "Precio Unitario"))
        self.pushButton.setText(_translate("Dialog", "Buscar"))
        self.label_44.setText(_translate("Dialog", "Descuento"))
        self.label_38.setText(_translate("Dialog", "Buscar Producto"))
        self.label_40.setText(_translate("Dialog", "Fecha"))
        self.label_45.setText(_translate("Dialog", "Sub Total"))
        self.label_51.setText(_translate("Dialog", "Monto Total"))
        self.label_55.setText(_translate("Dialog", "Vendedor"))
        self.label_49.setText(_translate("Dialog", "Cantidad"))
        self.label.setText(_translate("Dialog", "Codigo"))
        self.label_2.setText(_translate("Dialog", "Producto"))
        self.label_3.setText(_translate("Dialog", "Cantidad"))
        self.label_4.setText(_translate("Dialog", "Unidad"))
        self.label_5.setText(_translate("Dialog", "Codigo"))
        self.label_6.setText(_translate("Dialog", "Codigo"))
        self.label_7.setText(_translate("Dialog", "Codigo"))
        self.label_8.setText(_translate("Dialog", "Codigo"))
        self.label_9.setText(_translate("Dialog", "Codigo"))
        self.label_10.setText(_translate("Dialog", "Codigo"))
        self.label_11.setText(_translate("Dialog", "Codigo"))
        self.label_12.setText(_translate("Dialog", "Producto"))
        self.label_13.setText(_translate("Dialog", "Producto"))
        self.label_14.setText(_translate("Dialog", "Producto"))
        self.label_15.setText(_translate("Dialog", "Producto"))
        self.label_16.setText(_translate("Dialog", "Producto"))
        self.label_17.setText(_translate("Dialog", "Producto"))
        self.label_18.setText(_translate("Dialog", "Producto"))
        self.label_23.setText(_translate("Dialog", "Cantidad"))
        self.label_24.setText(_translate("Dialog", "Cantidad"))
        self.label_25.setText(_translate("Dialog", "Cantidad"))
        self.label_26.setText(_translate("Dialog", "Cantidad"))
        self.label_27.setText(_translate("Dialog", "Cantidad"))
        self.label_28.setText(_translate("Dialog", "Cantidad"))
        self.label_29.setText(_translate("Dialog", "Cantidad"))
        self.label_30.setText(_translate("Dialog", "Cantidad"))
        self.label_31.setText(_translate("Dialog", "Cantidad"))
        self.label_32.setText(_translate("Dialog", "Cantidad"))
        self.label_33.setText(_translate("Dialog", "Cantidad"))
        self.label_34.setText(_translate("Dialog", "Cantidad"))
        self.label_35.setText(_translate("Dialog", "Cantidad"))
        self.label_36.setText(_translate("Dialog", "Cantidad"))
        self.label_42.setText(_translate("Dialog", "P. Unidad"))
        self.label_53.setText(_translate("Dialog", "Documento"))
        self.label_43.setText(_translate("Dialog", "Valor Venta"))
        self.label_19.setText(_translate("Dialog", "Productos"))
        self.label_48.setText(_translate("Dialog", "Nombre Producto"))
        self.label_47.setText(_translate("Dialog", "Codigo"))
        self.label_46.setText(_translate("Dialog", "Total General"))
        self.pushButton_4.setText(_translate("Dialog", "Productos"))
        self.pushButton_5.setText(_translate("Dialog", "Proveedores"))
        self.pushButton_6.setText(_translate("Dialog", "Historial Ventas"))
        self.pushButton_7.setText(_translate("Dialog", "Empleados"))
        self.pushButton_8.setText(_translate("Dialog", "Clientes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Administrador()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

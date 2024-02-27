from Models.detallesFacturas import DetallesFacturas

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Conection import connection




class ControladorHistorial():

    def __init__(self,principal):
        self.principal = principal
        
        self.historial = DetallesFacturas(connection())
        
        
    def actualizar_historial(self):
        tablaHistorial = self.principal.tablaHistorialVentas          # Accedemos a la tabla de productos 
        print("estas en el metodo actualizar")
        print("este es el historial")
        historial = self.historial.obtener_historial() #almacenamos el retorno del modelo producto en la variable productos
        tablaHistorial.setRowCount(0)
        for fila,info_fila in enumerate(historial):   #recorremos la variable productos usando el metodo enumerate (recuerden que el modelo devuelve una tupla)
            tablaHistorial.insertRow(fila)
            for columna, info in enumerate(info_fila):                   
                tablaHistorial.setItem(fila,columna,QtWidgets.QTableWidgetItem(str(info))) #añadimos cada item a la tabla productos
        print(historial)
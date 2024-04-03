from Models.cliente import Cliente

from PyQt5 import QtWidgets
from Database.Conection import connection

class ControladorClientes():

    def __init__(self,principal):
        self.principal = principal
        self.cliente = Cliente(connection())

    def actualizar_clientes(self):
        tablaClientes = self.principal.tableWidget   # Accedemos a la tabla de productos 
        
        print("estas en el metodo actualizar")
        print("estos son los clientes")
        clientes = self.cliente.obtenerClientes() #almacenamos el retorno del modelo producto en la variable productos
        tablaClientes.setRowCount(0)
        for fila,info_fila in enumerate(clientes):   #recorremos la variable productos usando el metodo enumerate (recuerden que el modelo devuelve una tupla)
            tablaClientes.insertRow(fila)
            for columna, info in enumerate(info_fila):                   
                tablaClientes.setItem(fila,columna,QtWidgets.QTableWidgetItem(str(info))) #añadimos cada item a la tabla productos
        print(clientes)

       


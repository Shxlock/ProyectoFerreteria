import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)      # Importaciones necesarias para nevegar entre carpetas
 

from PyQt5 import QtWidgets                     
from PyQt5.QtWidgets import QMessageBox       


from Database.Conection import connection       #importaciones de Base de datos y modelos utilizados en este controlador
from Models.proveedor import Proveedor
# from Models.producto import Producto
from Models.categoriaProducto import CategoriaProducto
from Models.producto import Producto

class PrincipalControlador():
    def __init__(self,principal):
        self.categoriaProducto = CategoriaProducto(connection())  #Instancias del modelo categoriaProducto
        self.proveedor = Proveedor(connection())                  #Instancia del modelo proveedor
        self.producto = Producto(connection())                    #Instancia de producto
        self.principal = principal                                #Instancia de la vista principal (administradorFerreteria.py)
        
    def actualizar(self):                           #Metodo para actualizar productos
        tabla = self.principal.tablaProductos          # Accedemos a la tabla de productos 
        print("estas en el metodo actualizar")
        print("esto son los productos")
        productos = self.producto.obtenerProductos() #almacenamos el retorno del modelo producto en la variable productos
        tabla.setRowCount(0)
        for fila,info_fila in enumerate(productos):   #recorremos la variable productos usando el metodo enumerate (recuerden que el modelo devuelve una tupla)
            tabla.insertRow(fila)
            for columna, info in enumerate(info_fila):                   
                tabla.setItem(fila,columna,QtWidgets.QTableWidgetItem(str(info))) #añadimos cada item a la tabla productos
        print(productos)
        
    def buscador(self, palabra):                             #buscador de productos de la interfaz principal
        resultados = self.principal.tablaProductos               #tabla productos
        resultados.setRowCount(0)
        productos_encontrados = self.producto.buscador(palabra)    #guardamos lo q retorna el metodo buscador del modelo producto

        if productos_encontrados:                                   #nuevamente lo recorremos el valor almacenado
            for fila, item in enumerate(productos_encontrados):
                resultados.insertRow(fila)                    
                for columna, valor in enumerate(item):
                    resultados.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor))) #si hay coincidencias mostramos los valores en la tabla
                    print("encontrado")
        else:
            print("No se encontró")
        
    def abrirVentana(self,OpcionesEmpleados):   # metodo para abrir la ventana empleado 
        self.Dialog = QtWidgets.QMainWindow()
        self.Dialog.ui = OpcionesEmpleados()
        self.Dialog.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def abrirProductos(self,OpcionesProductos): #metodo para abrir la ventana productos, le pasamos como parametro la clase que deseamos abrir
        self.Dialog = QtWidgets.QMainWindow()
        self.Dialog.ui = OpcionesProductos()
        self.Dialog.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def abrirProveedores(self,OpcionesProveedores): #metodo para abrir la ventana proveedores, le pasamos como parametro la clase que deseamos abrir
        self.Dialog = QtWidgets.QMainWindow()           #creamos un widget tipo main waindow
        self.Dialog.ui = OpcionesProveedores()        #creamos una instancia de la clase que recibimos como parametro
        self.Dialog.ui.setupUi(self.Dialog)           # llamamos al metodo setupUi de la clase
        self.Dialog.show()                         # mostramos la ventana
        
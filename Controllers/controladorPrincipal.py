import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


from Database.Conection import connection
from Models.inventario import Inventario
from Models.proveedor import Proveedor
# from Models.producto import Producto
from Models.categoriaProducto import CategoriaProducto
from Models.producto import Producto

class PrincipalControlador():
    def __init__(self,principal):
        self.categoriaProducto = CategoriaProducto(connection())
        self.inventario = Inventario(connection())
        self.proveedor = Proveedor(connection())
        self.producto = Producto(connection())
        self.principal = principal
        
    def actualizar(self):
        tabla = self.principal.tablaProductos
        consulta = """SELECT codigo_producto,nombre_producto,cantidad,descripcion,precio_unitario, c.nombre_categoria,p.nombre_proveedor FROM producto
            inner join categoria_producto c on c.id_categoria_producto = producto.id_categoria inner join
            proveedor p on p.nit_proveedor = producto.nit_proveedor
            
            """
        productos = self.producto.obtenerProductos(consulta)
        tabla.setRowCount(0)
        for fila,info_fila in enumerate(productos):
            tabla.insertRow(fila)
            for columna, info in enumerate(info_fila):
                tabla.setItem(fila,columna,QtWidgets.QTableWidgetItem(str(info)))
        print(productos)
        
    def buscador(self, palabra):
        resultados = self.principal.tablaProductos
        resultados.setRowCount(0)
        productos_encontrados = self.producto.buscador(palabra)

        if productos_encontrados:
            for fila, item in enumerate(productos_encontrados):
                resultados.insertRow(fila)
                for columna, valor in enumerate(item):
                    resultados.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(valor)))
        else:
            print("No se encontró")
        
        
        
    
        
        
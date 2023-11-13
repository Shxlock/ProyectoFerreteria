import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Database.Conection import connection
from Models.empleado import Empleado
from Models.cliente import Cliente
from Models.factura import Factura
from Models.venta import Venta
from Models.producto import Producto
import uuid


class VentaControlador():
    def __init__(self,principal):
        self.empleado = Empleado(connection())
        self.cliente = Cliente(connection())
        self.venta = Venta(connection())
        self.factura = Factura(connection())
        self.producto = Producto(connection())
        self.principal = principal
    def generar_codigo(self):
        codigo_venta = str(uuid.uuid4())
        codigo_venta = codigo_venta[:6]  
        codigo_venta = codigo_venta.upper()
        return codigo_venta
    
    def agregar_venta(self,codigo,cantidad):
        codigo = int(codigo)
        verificar = self.producto.codigo(codigo)
        if verificar:
            codigo_venta = self.generar_codigo()
            consulta = """SELECT codigo_producto, nombre_producto, precio_unitario from producto where codigo_producto = %s"""
            modelo = self.producto.ventaProductos(consulta,codigo)
            print(modelo)
            if modelo:
                tabla = self.principal.tablaVentas
                tabla.insertRow(0)
                columna = 0
                tabla.setItem(0,columna,QtWidgets.QTableWidgetItem(str(codigo_venta)))
                for columna, info in enumerate(modelo, start=1):
                    tabla.setItem(0, columna, QtWidgets.QTableWidgetItem(str(info)))
                columna = 4
                tabla.setItem(0,columna, QtWidgets.QTableWidgetItem(str(cantidad)))
                self.calcularPrecio(cantidad)
        else:
            print("No existe un producto con dicho codigo")
            
    def calcularPrecio(self,cantidad):
        codigos = []
        tabla = self.principal.tablaVentas
        for row in range(tabla.rowCount()):
            item = tabla.item(row, 1)
            if item is not None:
                codigos.append(item.text())
        print(codigos)
        precios = []
        for row in range(tabla.rowCount()):
            item = tabla.item(row, 3)
            if item is not None:
                item = int(item.text())
                precios.append(item)
        print(precios)
        suma = sum(precios)
        print(suma)
        
            
        
    
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget, QTableWidgetItem


from Database.Conection import connection
from Models.empleado import Empleado
from Models.cliente import Cliente
from Models.factura import Factura
from Models.producto import Producto
import uuid
from Controllers.controladorValidar import ValidarControlador

class VentaControlador():
    def __init__(self,principal):  # recibe la interfaz por parametro en el constructor
        self.empleado = Empleado(connection())  # crea las instancias a usar
        self.cliente = Cliente(connection())
        self.factura = Factura(connection())
        self.producto = Producto(connection())
        self.principal = principal      # instancia de la interfaz
        self.validar = ValidarControlador(principal)
        self.productos = []



    def generar_codigo(self):         # metodo para generar un codigo
        codigo_venta = str(uuid.uuid4())  # usamos la libreria uuid para generar el codigo
        codigo_venta = codigo_venta[:8]   # hacemos que el codigo sea de solo 8 caracteres
        codigo_venta = codigo_venta.upper()   # convertirmos los caracteres a mayusculas
        return codigo_venta        # retornamos el codigo
    
    def agregar_venta(self, codigo, cantidad):      # metodo para agregar una venta en la tablaVentas
        
        if self.validar.validarVenta(codigo, cantidad):  # validamos que los datos obteniedos no esten vacios
            verificar = self.producto.codigo(codigo)    # verificamos que dicho codigo SI exista en nuestra base de datos
            tablaVentas = self.principal.tablaVentas     # tabla ventas
            tablaProductos = self.principal.tablaProductos # tabla productos
            if verificar:              # si el codigo si existe procedemos con el proceso
                for row in range(tablaProductos.rowCount()):     # recorremos la tabla productos con el metodo rowCount() que cuenta el numero de filas de esta tabla
                    if tablaProductos.item(row, 0) is not None and tablaProductos.item(row, 0).text() == codigo: # en el indice 0 se encuentra el codigo, entonces lo obtenemos y verificamos q no este vacio y que sea igual al codigo q nos pasaron por parametro
                        cantidad_producto = int(tablaProductos.item(row, 2).text()) if tablaProductos.item(row, 2) is not None else 0 # verificamos que la cantidad de la tablaProducto (se encuentra en el indice 2) no sea ni None ni sea igual a 0

                        if int(cantidad) <= cantidad_producto:      # verificamos que la cantidad pasada por parametro (es decir, la cantidad a comprar/vender) sea inferior o igual a la cantidad que tiene la tabla
                            nueva_cantidad_producto = cantidad_producto - int(cantidad) # creamos una variable la cual restamos la cantidad q hay en la tabla con la cantidad a vender
                            tablaProductos.setItem(row, 2, QTableWidgetItem(str(nueva_cantidad_producto))) # le pasamos esa variable a ese campo, de este modo actualizamos la cantidad en la tablaProductos

                            codigo_venta = self.generar_codigo() # guardamos el retorno del metodo generar_codigo en la variable codigo_venta
                            consulta = """SELECT codigo_producto, nombre_producto, precio_unitario from producto where codigo_producto = %s"""
                            modelo = self.producto.ventaProductos(consulta, codigo) #creamos la consulta y se la pasamos al modelo, junto con el codigo
                            if modelo:                          
                                posicion = tablaVentas.rowCount() # obtenemos la posicion que es la cantidad de filas de la tablaVentas
                                tablaVentas.insertRow(posicion)     # insertamos la fila
                                columna = 0              
                                tablaVentas.setItem(posicion, columna, QtWidgets.QTableWidgetItem(str(codigo_venta))) # al campo con indice 0, le añadimos el codigo obtenido, es decir, codigo_venta
                                for columna, info in enumerate(modelo, start=1):   # empezamos a iterar la tabla desde el indice 1 (ya añadimos un item al indice 0)
                                    tablaVentas.setItem(posicion, columna, QtWidgets.QTableWidgetItem(str(info))) # recorremos la tupla obtenida por el modelo y lo insertamos en la tablaVentas desde el indice 1
                                columna = 4             
                                tablaVentas.setItem(posicion, columna, QtWidgets.QTableWidgetItem(str(cantidad))) # le añadimos la cantidad al indice 4
                                self.calcularPrecio()     # llamamos a metodo calcular precio
                        else:
                            print("Cantidad insuficiente")
                        break
            else:
                print("no existe un producto con dicho codigo")
        else:
            self.validar.mostrarMensaje("Rellena los datos", "Datos faltantes")

    
    def borrarFila(self): # metodo para borrar una fila de la tablaVentas
        tablaVentas = self.principal.tablaVentas
        tablaProductos = self.principal.tablaProductos
        fila_seleccionada = tablaVentas.currentRow()  # la fila seleccionada, es decir, a la fila en la cual hemos dado click

        if fila_seleccionada != -1:                      
            codigo_producto = tablaVentas.item(fila_seleccionada, 1).text() # obteemos el codigo_producto
            cantidad_venta = int(tablaVentas.item(fila_seleccionada, 4).text()) # obtenemos la cantidad_venta

            # Buscar el producto en la tabla de productos y sumar la cantidad vendida
            for row in range(tablaProductos.rowCount()):   # recorremos la cantidad de filas de la tablaProductos
                if tablaProductos.item(row, 0) is not None and tablaProductos.item(row, 0).text() == codigo_producto: # lo mismo que en la tablaVentas, me da pereza escribirlo de nuevo :)
                    cantidad_producto = int(tablaProductos.item(row, 2).text()) if tablaProductos.item(row, 2) is not None else 0 # lo mismo
                    nueva_cantidad_producto = cantidad_producto + cantidad_venta # en este caso en lugar de restar, sumamos, ya que estamos cancelando una venta y debemos volver a tener la cantidad tal y como estaba en un principio
                    tablaProductos.setItem(row, 2, QTableWidgetItem(str(nueva_cantidad_producto))) # le añadimos esa variable a la columna con indice 2
                    # Eliminar la venta de la tabla de ventas
                    tablaVentas.removeRow(fila_seleccionada)  
                    break
        else:
            print("Selecciona una fila para eliminar")
    
    def calcularPrecio(self):               # metodo para calcular precio
        tabla = self.principal.tablaVentas       
        precios = []                # creamos una lista para guardar los precios
        
        print("estmoas en el metodo calcularPrecio")
        for row in range(tabla.rowCount()):       # recorremos la tablaVentas
            item_codigo = tabla.item(row, 1)      # en la columna con indice 1, obtenemos el codigo del producto
            item_precio = tabla.item(row, 3)      # en la columna con indice 3, obtenemos el precio
            item_cantidad = tabla.item(row, 4)    # en la columna con indice 4, la cantidad
            if item_codigo is not None and item_precio is not None and item_cantidad is not None:
                codigo = int(item_codigo.text()) 
                precio_unitario = int(item_precio.text())      # convertimos el precio a entero
                cantidad_producto = int(item_cantidad.text())      # convertimos la cantidad a entero
                self.productos.append([codigo,precio_unitario,cantidad_producto])
                precios.append(precio_unitario * cantidad_producto) # añadimos a la lista la multiplicacion de estos dos ultimos
                self.precios(precios)           # le pasamos la lista al metodo precios
                
    def actualizarCantidad(self, item_codigo, cantidadComprar):       # metodo para actualizar la cantidad
        print("entramos a actualizar cantidad")             
        tabla = self.principal.tablaProductos           
        codigo = 0
        cantidad = 2
        codigo_a_buscar = item_codigo.text()
        cantidad_actual = 0
        print(cantidadComprar)
        print(codigo_a_buscar)
        cantidadComprar = int(cantidadComprar)  
        print(cantidadComprar)
        for row in range(self.principal.tablaProductos.rowCount()): # recorremos la tablaProductos
            codigo_actual = tabla.item(row, codigo).text()       # en la columna cero, obtenemos el codigo
            print(codigo_actual)
            print("dentro del for")
            print(codigo_actual)
            print(codigo_a_buscar)          
            if codigo_actual == codigo_a_buscar:    # si elcodigo es igual al codigo que recibimos por parametros procedemos
                print(codigo_a_buscar)
                print("dentro del if")
                print(cantidadComprar)
                cantidad_actual = int(tabla.item(row, cantidad).text())
                nueva_cantidad = max(0, cantidad_actual - cantidadComprar)    # utilizamos el metodo max para asegurarnos q la cantidad nunca sera inferior a cero y.
                tabla.setItem(row, cantidad, QTableWidgetItem(str(nueva_cantidad)))
                break

    def precios(self,precios):
        if self.principal.tablaVentas.rowCount() != 0: # nos aseguramos que la cantida de filas es diferente a cero
            print("La tabla no está vacía")
            suma = sum(precios)
            print("La cantidad total de los productos es: ", suma)
            print(precios)
            suma = str(suma)                    # le pasamos la suma de los valores 
            btnVenta = self.principal.valorVenta   
            btnVenta.setText(suma)           # definimos como texto la suma
            btnSubtotal = self.principal.subTotal
            btnSubtotal.setText(suma)     # lo mismo
            btnTotal = self.principal.total
            btnTotal.setText(suma)      # lo mismo
        else:             # si la cantidad de filas es igual a cero
            btnVenta = self.principal.valorVenta
            btnVenta.setText("0")      # definimos los textos en cero
            btnSubtotal = self.principal.subTotal
            btnSubtotal.setText("0")      # cero
            btnTotal = self.principal.total
            btnTotal.setText("0")        # cero
            print("La tabla está vacía")
        
    
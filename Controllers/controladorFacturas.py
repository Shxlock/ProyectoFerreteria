import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Conection import connection
from PyQt5.QtWidgets import QMessageBox

from Models.empleado import Empleado
from Models.cliente import Cliente
from Models.detallesFacturas import DetallesFacturas
import re
from Models.factura import Factura
from Models.producto import Producto
from Controllers.controladorVentas import VentaControlador
from Controllers.controladorValidar import ValidarControlador
from Controllers.controladorPrincipal import PrincipalControlador

import uuid
import smtplib

class FacturaControlador():
    def __init__(self,principal):
        self.empleado = Empleado(connection())
        self.cliente = Cliente(connection())
        self.factura = Factura(connection())
        self.producto = Producto(connection())
        self.principal = principal
        self.controlador_principal = PrincipalControlador(principal)
        self.ventaControlador = VentaControlador(self.principal)
        self.detalles_facturas = DetallesFacturas(connection())
        self.validar = ValidarControlador(principal)

    # generamos el codigo de la factura con la libreria uuid

    def generarCodigo(self):
        mi_uuid = uuid.uuid4()
        codigo_numerico = int(mi_uuid.int) # en esta ocasion sera solo numeros
        codigo_numerico = codigo_numerico % 10000 
        return codigo_numerico
    
    def validarCampos(self):
        print("Iniciando evento")
        fecha = self.principal.fechaFactura.text()
        documento = self.principal.documento.text()
        tipoDePago = self.principal.tipoDePago.currentText()
        vendedor = self.principal.vendedor.text()
        email_factura = self.principal.email_factura.text()
        cliente = self.principal.cliente.text()
        turnoVendedor = self.principal.turnoVendedor.currentText()
        datos = [fecha, documento, tipoDePago, vendedor, email_factura, cliente, turnoVendedor]
        if self.validar.validarDatos(datos): # verificamos q los campos no esten vacios
            print("datos correctos")
            if self.validar.validarDocumento(documento) and self.validar.validarDocumento(vendedor): # verificamos q documento y vendendor esten correctos
                print("documento correcto")
                if self.validar.validarEmail(email_factura): # verificamos que email_factura tenga un formato de correo electronico
                    if self.empleado.existeCedula(vendedor): # verificamos si la cedula del vendedor existe en nuestra base de datos
                        print("todo bien")
                        if self.principal.tablaVentas.rowCount() > 0: # verificamos q la cantidad de filas de la tablaVentas sea mayor a cero
                            codigo_factura = self.generarCodigo() # generamos el codigo
                            
                            self.tabla_cliente(documento,cliente,email_factura) # llamamos al metodo tabla_cliente
                            
                            self.tabla_factura(codigo_factura,tipoDePago,email_factura,turnoVendedor,fecha,documento,vendedor) # llamamos al metodo tabla_factura
                            tablaVentas = self.principal.tablaVentas
                            num_filas = tablaVentas.rowCount()
                            acumulador = f''     # creamos un acumulador de texto usando una f string
                                
                            for row in range(num_filas): # iteramos sobre el numero de filas de la tablaVentas
                                codigo_detalles = tablaVentas.item(row, 0).text()    # obtenemos los datos necesarios
                                codigo_producto = tablaVentas.item(row, 1).text()
                                nombre_producto = tablaVentas.item(row, 2).text()
                                cantidad = tablaVentas.item(row, 4).text()
                                precio_unitario = tablaVentas.item(row, 3).text()
                                cantidad = int(cantidad)                    # los pasamos al formato en q los necesitemos
                                codigo_producto = int(codigo_producto)
                                precio_unitario = int(precio_unitario)
                                precios = precio_unitario * cantidad
                                datosDetalles = [codigo_detalles,codigo_factura,codigo_producto,cantidad,precio_unitario]
                                acumulador += f'Producto: {nombre_producto} Cantidad: {cantidad} Precio: {precio_unitario}\n' # le añadimos al acumulador la informacion de cada fila
                                datosProductos = [cantidad,codigo_producto]
                                self.detalles_facturas.insertarDatos(datosDetalles) # llamamos al metodo insertarDatos del modelo detalles_factura
                                self.producto.actualizarCantidad(datosProductos) # llamamos al metodo actualizarCantidad del modelo producto
                                self.controlador_principal.actualizar() # llamamos al metodo actualizar
                                print(datosDetalles)
                            self.principal.tablaProductos.update() # forzamos un update en la tablaProductos
                            precios = self.principal.total.text() # obtenemos el precio total
                            acumulador += f'Total a pagar: {precios}' # lo añadimos al acumulador
                            print(acumulador)
                            self.generarCorreo(email_factura,cliente,acumulador)                 # llamamos a la funcion q envia el correo y le pasamos la informacion a usar      
                            self.validar.mostrarMensaje(self.validar.MENSAJE_TODO_CORRECTO,self.validar.MENSAJE_TODO_CORRECTO) # mostramos un mensaje en pantalla de q todo ta piola
                            self.limpiar(self.principal.valorVenta,self.principal.subTotal,self.principal.Descuento,self.principal.total,self.principal.documento,self.principal.vendedor,self.principal.email_factura,self.principal.cliente)        # limpiamos los widgets        
                            self.principal.tablaVentas.setRowCount(0)   # limpiamos la tablaVentasa
                        else:
                            print("No hay ventas registradas")
                    else:
                        print("no existe dicha cedula")
                else:
                    self.validar.mostrarMensaje(self.validar.MENSAJE_EMAIL_NO_VALIDO,self.validar.MENSAJE_EMAIL_NO_VALIDO)
            else:
                self.validar.mostrarMensaje(self.validar.MENSAJE_DOCUMENTO_NO_VALIDO,self.validar.MENSAJE_DOCUMENTO_NO_VALIDO)
        else:
            self.validar.mostrarMensaje(self.validar.MENSAJE_CAMPOS_VACIOS,self.validar.MENSAJE_CAMPOS_VACIOS)
        
        
    
    def tabla_cliente(self,documento,nombre,email):
        documento = int(documento)
        datos = [documento,nombre,email]
        if self.cliente.existeCliente(documento) == False: # verifica si la cedula no existe
            self.cliente.insertarDatos(datos) # si no existe crea el cliente
        else:
            print("ya existe el cliente") # si ya existe no hace nada :))
        
    def tabla_factura(self,codigo_factura,tipoDePago,email_factura,turnoVendedor,fecha,documento,vendedor):
        documento = int(documento)
        vendedor = int(vendedor)
        datos = [codigo_factura,tipoDePago,email_factura,turnoVendedor,fecha,documento,vendedor]
        print(datos)
        self.factura.insertarDatos(datos) # le pasamos la lista al metodo insertarDatos del modelo factura
  
    def limpiar(self,*args): # recibe los widgets y les aplica el metodo clear() para dejarlos impecables
        for arg in args:
            arg.clear()
        print("limpio")
        
    def generarCorreo(self,correo,cliente,acumulador): # genera el correo
        HOST = "smtp-mail.outlook.com"
        PORT = 587
        FROM_EMAIL = "shxlock07@outlook.com" 
        TO_EMAIL = correo  
        PASSWORD = "" # contraseña

        #genera el mensaje con el acumulador 
        MESSAGE  = f"""Subject: Factura Ferreteria AeroNorte,

        Querido {cliente}, esta es su factura: 
        
            {acumulador} 
        
        Ferreteria AeroNorte.

        Saludos!"""

        smtp = smtplib.SMTP(HOST,PORT)

        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        status_code,response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        print(f"[*] Logging in: {status_code} {response}")

        smtp.sendmail(FROM_EMAIL,TO_EMAIL,MESSAGE)
        smtp.quit()
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Conection import connection
from Models.proveedor import Proveedor
from Controllers.controladorValidar import ValidarControlador

class ControladorProveedores():
    def __init__(self, OpcionesProveedores):
        self.proveedor = Proveedor(connection())
        self.opcionesProveedor = OpcionesProveedores
        self.validar = ValidarControlador(OpcionesProveedores)
    
    def agregarProveedor(self,codigo,nombre,telefono,email,direccion,ciudad):
        datos = [codigo,nombre,telefono,email,direccion,ciudad]
        validar = self.validar.validarDatos(datos)
        if validar:
            if len(codigo) == 3 and int(codigo) > 0:
                telefono = int(telefono)
                if self.validar.validarTelefono(telefono):
                    print("telefono correcto")
                    if self.validar.validarEmail(email):
                        codigo = int(codigo)
                        telefono = int(telefono)
                        datos = [codigo,nombre,telefono,email,direccion,ciudad]
                        self.proveedor.agregarProveedor(datos)
                        self.validar.mostrarMensaje(self.validar.MENSAJE_TODO_CORRECTO,self.validar.MENSAJE_TODO_CORRECTO)
                        self.limpiar(self.opcionesProveedor.codigo_proveedor,self.opcionesProveedor.nombre_proveedor,self.opcionesProveedor.telefono_proveedor,self.opcionesProveedor.email_proveedor,self.opcionesProveedor.direccion_proveedor,self.opcionesProveedor.ciudad_proveedor)
                        self.comboProveedor()
                    else:
                        self.validar.mostrarMensaje(self.validar.MENSAJE_EMAIL_NO_VALIDO,self.validar.MENSAJE_EMAIL_NO_VALIDO)
                else:
                    self.validar.mostrarMensaje("El telefono debe ser de solo 10 digitos", "Telefono incorrecto")
            else:
                self.validar.mostrarMensaje("El codigo debe ser 3 de números. Ni mas ni menos", "Codigo Incorrecto")        
            
        else:
            self.validar.mostrarMensaje("Rellena todos lo campos", "Rellna todos los campos")
            
    def limpiar(self,*args):
        for arg in args:
            arg.clear()
        print("limpio")
        
    def eliminarProveedor(self,proveedorEliminar):
        print(proveedorEliminar)
        self.proveedor.EliminarProveedor(proveedorEliminar)
        self.validar.mostrarMensaje("Proveedor Eliminado Exitosamente", "Proveedor Eliminado")
        self.comboProveedor()
        
    def modificarProveedor(self,nit):
        if nit != "" and not None and len(nit) == 3:
            print("NIT correcto")
            
            if self.proveedor.buscarProveedor(nit) :
                print("Bien")
                self.opcionesProveedor.nuevo_nombre_proveedor.setReadOnly(False)   
                self.opcionesProveedor.nuevo_telefono_proveedor.setReadOnly(False) 
                self.opcionesProveedor.nuevo_email_proveedor.setReadOnly(False)
                self.opcionesProveedor.nueva_direccion_proveedor.setReadOnly(False)
                self.opcionesProveedor.nueva_ciudad_proveedor.setReadOnly(False)
                self.opcionesProveedor.btnModificarProveedor.setEnabled(True)
                self.cambios(nit)
            else:
                print("mal")
        else:
            self.validar.mostrarMensaje("Ingresa un NIT correcto", "Ingresa un NIT")
            
    def cambios(self, nit):
        datos = self.proveedor.buscarProveedor(nit)
        if datos:
            nombre_proveedor = datos[0]
            self.opcionesProveedor.nuevo_nombre_proveedor.setText(nombre_proveedor)
            self.opcionesProveedor.nuevo_telefono_proveedor.setText(str(datos[1]))
            self.opcionesProveedor.nuevo_email_proveedor.setText(datos[2])
            self.opcionesProveedor.nueva_direccion_proveedor.setText(datos[3])
            self.opcionesProveedor.nueva_ciudad_proveedor.setText(datos[4])
        else:
            print("Proveedor no encontrado o datos vacíos")
            
    def cambiarProveedor(self):
        nit = self.opcionesProveedor.codigo_modificar_producto.text()
        nombre = self.opcionesProveedor.nuevo_nombre_proveedor.text()
        telefono = self.opcionesProveedor.nuevo_telefono_proveedor.text()
        email = self.opcionesProveedor.nuevo_email_proveedor.text()
        direccion = self.opcionesProveedor.nueva_direccion_proveedor.text()
        ciudad = self.opcionesProveedor.nueva_ciudad_proveedor.text()
        datos = [nombre,telefono,email,direccion,ciudad]
        validar = self.validar.validarDatos(datos)
        if validar:
            telefono = int(telefono)
            if self.validar.validarTelefono(telefono):
                print("telefono correcto")
                if self.validar.validarEmail(email):
                    codigo = int(nit)
                    telefono = int(telefono)
                    datos = [nombre,telefono,email,direccion,ciudad,codigo]
                    self.proveedor.modificarProveedor(datos)
                    self.validar.mostrarMensaje(self.validar.MENSAJE_TODO_CORRECTO,self.validar.MENSAJE_TODO_CORRECTO)
                    self.limpiar(self.opcionesProveedor.codigo_modificar_producto,self.opcionesProveedor.nuevo_nombre_proveedor,self.opcionesProveedor.nuevo_telefono_proveedor,self.opcionesProveedor.nuevo_email_proveedor,self.opcionesProveedor.nueva_direccion_proveedor,self.opcionesProveedor.nueva_ciudad_proveedor)
                    self.comboProveedor()
                    self.opcionesProveedor.nuevo_nombre_proveedor.setReadOnly(True)
                    self.opcionesProveedor.nuevo_telefono_proveedor.setReadOnly(True)
                    self.opcionesProveedor.nuevo_email_proveedor.setReadOnly(True)
                    self.opcionesProveedor.nueva_direccion_proveedor.setReadOnly(True)
                    self.opcionesProveedor.nueva_ciudad_proveedor.setReadOnly(True)
                    self.opcionesProveedor.btnModificarProveedor.setEnabled(False)
                else:
                    self.validar.mostrarMensaje(self.validar.MENSAJE_EMAIL_NO_VALIDO,self.validar.MENSAJE_EMAIL_NO_VALIDO)
            else:
                self.validar.mostrarMensaje("El telefono debe ser de solo 10 digitos", "Telefono incorrecto")      
        else:
            self.validar.mostrarMensaje("Rellena todos lo campos", "Rellna todos los campos")
        
    
                
    def comboProveedor(self):
        self.limpiar(self.opcionesProveedor.eliminarProveedor)
        proveedores = self.proveedor.obtenterProveedores()
        self.opcionesProveedor.eliminarProveedor.addItem("Selecciona Proveedor")
        for cedula in proveedores:
            self.opcionesProveedor.eliminarProveedor.addItem(cedula[0])
        self.opcionesProveedor.eliminarProveedor.setCurrentIndex(0)
    
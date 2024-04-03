import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.controladorValidar import ValidarControlador
from Models.empleado import Empleado
from Models.User import User
from Database.Conection import connection
from PyQt5.QtGui import QIntValidator
from Controllers.UsuarioExistente import UsuarioExistenteError


class EmpleadoControlador():
    
    def __init__(self, opciones_empleados):
        self.validar = ValidarControlador(opciones_empleados)
        self.opciones_empleados = opciones_empleados
        self.empleadoTabla = Empleado(connection())
        self.user = User(connection())
        
    def validarDatos(self,cedula,nombre,telefono,email,apellido,direccion,RegistrarEmpleado):
        datos = [cedula,nombre,telefono,email,apellido,direccion]
        if self.validar.validarDatos(datos):
            print("datos correctos")
            if self.validar.validarDocumento(cedula) and self.validar.validarDocumento(telefono):
                print("documento correcto")
                if self.validar.validarEmail(email):
                    cedula = int(cedula)
                    nombre = str(nombre)
                    telefono = int(telefono)
                    email = str(email)
                    apellido = str(apellido)
                    direccion = str(direccion)
                    empleado = [cedula,nombre,telefono,email,apellido,direccion]
                    
                    self.abrir_ventana(RegistrarEmpleado)
                    #self.EnviarDatos(cedula,nombre,telefono,email,apellido,direccion)
                    #self.validar.mostrarMensaje(self.validar.MENSAJE_TODO_CORRECTO,self.validar.MENSAJE_TODO_CORRECTO) 
                    self.crearEmpleado(empleado)
                else:
                    self.validar.mostrarMensaje(self.validar.MENSAJE_EMAIL_NO_VALIDO,self.validar.MENSAJE_EMAIL_NO_VALIDO)
            else:
                self.validar.mostrarMensaje(self.validar.MENSAJE_DOCUMENTO_NO_VALIDO,self.validar.MENSAJE_DOCUMENTO_NO_VALIDO)
        else:
            self.validar.mostrarMensaje(self.validar.MENSAJE_CAMPOS_VACIOS,self.validar.MENSAJE_CAMPOS_VACIOS)

    def abrir_ventana(self,RegistrarEmpleado):
        self.Dialog = QtWidgets.QMainWindow()
        self.Dialog.ui = RegistrarEmpleado()
        self.Dialog.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    
    def crearEmpleado(self, datos):
        try:
            print(datos)
            self.empleadoTabla.insertarDatos(datos)
            print("creando empleado")
        except Exception as e:
            print("Error al insertar datos en la tabla 'empleado':", str(e))


    def obtenerCedula(self):
        pass 


    def obtenerCedulas(self):
        sql = """SELECT cedula_empleado from empleado""" 
        cedulas = self.empleadoTabla.Cedulas(sql)
        cedula = [(str(cedula[0]),) for cedula in cedulas]
        return cedula
        
    def eliminarEmpleado(self,eliminar_empleado):
        self.obtenerCedulas()
        if eliminar_empleado != "Seleccionar cédula":
            print(eliminar_empleado)
            self.user.eliminarUsuario(eliminar_empleado)
            self.opciones_empleados.cedulas()
        else:
            print("Error. No se puede convertir a entero")
            self.validar.mostrarMensaje("Selecciona una cedula", "Cedula Incorrecta")
            
    def modificarEmpleado(self,cedula):
        print("----------Modificando empleado--------------")
        datos = self.empleadoTabla.obtenerDatos(cedula)
        if datos is not None:
            
            self.opciones_empleados.nuevo_nombre_empleado.setReadOnly(False)
            self.opciones_empleados.nuevo_telefono_empleado.setReadOnly(False)
            self.opciones_empleados.nuevo_email_empleado.setReadOnly(False)
            self.opciones_empleados.nuevo_apellido_empleado.setReadOnly(False)
            self.opciones_empleados.nueva_direccion_empleado.setReadOnly(False)
            self.opciones_empleados.nuevo_nombre_empleado.setText(datos[0])
            self.opciones_empleados.nuevo_telefono_empleado.setText(str(datos[1]))
            self.opciones_empleados.nuevo_email_empleado.setText(datos[2])
            self.opciones_empleados.nuevo_apellido_empleado.setText(datos[3])
            self.opciones_empleados.nueva_direccion_empleado.setText(datos[4])
            self.opciones_empleados.btnModificarEmpleado.setEnabled(True)
            
        else:
            self.validar.mostrarMensaje("Cedula no valida. Ingresa una cedula valida", "Ingresa cedula valida")
        
    def soloLeer(self):
        self.opciones_empleados.nuevo_nombre_empleado.setReadOnly(True)
        self.opciones_empleados.nuevo_telefono_empleado.setReadOnly(True)
        self.opciones_empleados.nuevo_email_empleado.setReadOnly(True)
        self.opciones_empleados.nuevo_apellido_empleado.setReadOnly(True)
        self.opciones_empleados.nueva_direccion_empleado.setReadOnly(True)
        
    def limpiar(self):
        self.opciones_empleados.btnBuscarEmpleado.clear()
        self.opciones_empleados.nuevo_nombre_empleado.clear()
        self.opciones_empleados.nuevo_telefono_empleado.clear()
        self.opciones_empleados.nuevo_email_empleado.clear()
        self.opciones_empleados.nuevo_apellido_empleado.clear()
        self.opciones_empleados.nueva_direccion_empleado.clear()
        
    def modificar(self):
        cedula = self.opciones_empleados.btnBuscarEmpleado.text()
        cedula = int(cedula)
        nombre = self.opciones_empleados.nuevo_nombre_empleado.text()
        if nombre != "":
            telefono = self.opciones_empleados.nuevo_telefono_empleado.text()
            telefono = int(telefono)
            email = self.opciones_empleados.nuevo_email_empleado.text()
            validar = self.validar.validarTelefono(telefono)
            if validar:
                if self.validar.validarEmail(email):
                    apellido =  self.opciones_empleados.nuevo_apellido_empleado.text()
                    if apellido != "":
                        direccion = self.opciones_empleados.nueva_direccion_empleado.text()
                        if direccion != "":
                            datos = [nombre,telefono,email,apellido,direccion,cedula]
                            print(datos)
                            self.empleadoTabla.modificarEmpleado(datos)
                            self.opciones_empleados.btnModificarEmpleado.setEnabled(False)
                            self.limpiar()
                            self.soloLeer()
                        else:
                            self.validar.mostrarMensaje("Ingresa una direccion valida", "direccion incorrecta.")
                    else:
                        self.validar.mostrarMensaje("Ingresa un apellido valido", "apellido incorrecto.")
                else:
                    self.validar.mostrarMensaje("Ingresa un Email valido", "Email incorrecto.")
            else:
                self.validar.mostrarMensaje("Ingresa un telefono correcto", "Telefono incorrecto")
        else:
            self.validar.mostrarMensaje("Ingresa un nombre", "Nombre incorrecto")
        
        
        
        
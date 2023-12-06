import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Conection import connection
from Controllers.controladorValidar import ValidarControlador
from Models.categoriaProducto import CategoriaProducto
from Models.proveedor import Proveedor
from Models.producto import Producto

class ProductoControlador():
    def __init__(self, OpcionesProductos): # recibe la interfaz
        self.validar = ValidarControlador(OpcionesProductos) # instancias
        self.opcionesProductos = OpcionesProductos
        self.categoria = CategoriaProducto(connection()) # instancias de modelos, le pasa la conexion a la base de datos
        self.proveedor = Proveedor(connection())
        self.producto = Producto(connection())
        
    # CRUD CATEGORIAS
        
    def agregarCategoria(self,id,nombre,descripcion): # metodo para agregar una categoria
        id = str(id)                        # esto ya lo entienden, juraria
        nombre = str(nombre)
        descripcion = str(descripcion)
        datos = [id,nombre,descripcion]
        lleno = self.validar.validarDatos(datos)
        if lleno == True:
            if len(id) == 3 and id != "0":
                print("Vas bien")
                id = int(id)
                datos = [id,nombre,descripcion]
                print(datos)
                self.categoria.agregarCategoria(datos)
                self.limpiarCategoria(self.opcionesProductos.agrProductoId,self.opcionesProductos.agrNombreProducto,self.opcionesProductos.descripcion_categoria)
            else:
                self.validar.mostrarMensaje("Deben ser 3 digitos como ID", "Solo 3 digitos como ID")
        else:
            self.validar.mostrarMensaje("Rellana los campos", "Rellena todos los campos")
       
    def obtenerCategorias(self):      # obtenemos las categorias
        categorias = self.categoria.obtenerCategoria() # llamamos al metodo obtenerCategoria del modelo categoria
        return categorias
       
    def modificarCategoria(self, id):
        print("----------Modificando empleado--------------")
        datos = self.categoria.obtenerDatos(id)
        if datos:
            self.opcionesProductos.modificar_nombre_categoria.setReadOnly(False)
            self.opcionesProductos.modificar_descripcion.setReadOnly(False)
            self.opcionesProductos.modificar_nombre_categoria.setText(datos[0])
            self.opcionesProductos.modificar_descripcion.setPlainText(datos[1])
            self.opcionesProductos.btnModificarCategoria.setEnabled(True)
        else:
            self.validar.mostrarMensaje("Ingresa un ID válido","ID no válido")
       
    def eliminarCategoria(self,eliminar_empleado):
        if eliminar_empleado != "Seleccionar cédula":
            print(eliminar_empleado)
            self.categoria.eliminarCategoria(eliminar_empleado)
            self.opcionesProductos.nombreCategorias()
        else:
            print("Error. No se puede convertir a entero")
            self.validar.mostrarMensaje("Selecciona una categoria", "Categoria incorrecta")
        
      
    def modificar(self):
        id = self.opcionesProductos.modificar_id_buscar.text()
        id = int(id)
        nombre = self.opcionesProductos.modificar_nombre_categoria.text()
        descripcion = self.opcionesProductos.modificar_descripcion.toPlainText()
        datos = [nombre, descripcion, id]
        if self.validar.validarDatos(datos):
            print("todo bien")
            self.categoria.modificarCategoria(datos)
            self.validar.mostrarMensaje("Modificacion Hecha!", "Has modificado una categoria")
            self.limpiarCategoria(self.opcionesProductos.modificar_id_buscar,self.opcionesProductos.modificar_nombre_categoria,self.opcionesProductos.modificar_descripcion)
            
        else:
            self.validar.mostrarMensaje("Rellena los campos", "Rellena los campos")
            print("Error")
            
    def limpiarCategoria(self,agrProductoId,agrNombreProducto,descripcion_categoria):
        agrProductoId.clear()
        agrNombreProducto.clear()
        descripcion_categoria.clear()
        
       
        
        
    def categorias(self):
        self.opcionesProductos.id_categoria_producto.clear()
        categorias = self.categoria.obtenerIdsCategoria()
        self.opcionesProductos.id_categoria_producto.addItem("Seleccionar categoria")
        for categoria in categorias:
            self.opcionesProductos.id_categoria_producto.addItem(str(categoria[0]))
        self.opcionesProductos.id_categoria_producto.setCurrentIndex(0)

    def proveedorDatos(self):
        self.opcionesProductos.nit_proveedor_producto.clear()
        proveedores = self.proveedor.obtenerIdProveedores()
        self.opcionesProductos.nit_proveedor_producto.addItem("Seleccionar proveedor")
        for proveedor in proveedores:
            self.opcionesProductos.nit_proveedor_producto.addItem(str(proveedor[0]))
        self.opcionesProductos.nit_proveedor_producto.setCurrentIndex(0)
    
    
    # CRUD PRODUCTOS
    
    def agregarProducto(self):
        codigo = self.opcionesProductos.codigo_producto.text()
        nombre = self.opcionesProductos.nombre_producto.text()
        cantidad = self.opcionesProductos.cantidad_producto.text()
        descripcion = self.opcionesProductos.descripcion_producto.toPlainText()
        precio = self.opcionesProductos.precio_producto.text()
        categoria = self.opcionesProductos.id_categoria_producto.currentText()
        proveedor = self.opcionesProductos.nit_proveedor_producto.currentText()
        fecha_vencimiento = self.opcionesProductos.fecha_vencimiento.text() 
        datos = [codigo,nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento]
        if self.validar.validarDatos(datos):
            print("OK")
            if len(codigo) == 4:
                print("CODIGO OK")
                if categoria != "Seleccione Categoria" and proveedor != "Seleccione Proveedor":
                    print("Categoria y Proveedor OK")
                    codigo = int(codigo)
                    cantidad = int(cantidad)
                    precio = int(precio)
                    categoria = int(categoria)
                    proveedor = int(proveedor)
                    print(fecha_vencimiento)
                    if fecha_vencimiento == "2000-01-01":
                        print("todo perfecto")
                        fecha_vencimiento = None
                        enviar = [codigo,nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento]
                        self.producto.agregarProducto(enviar)
                    else:
                        print("todo correcto")
                        enviar = [codigo,nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento]
                        self.producto.agregarProducto(enviar)
                        
                else:
                    print("CATEGONT")
            else:
                print("CODIGON'T")
        else:
            print("NOT OK")
        
        
    def eliminarProducto(self):
        codigo = self.opcionesProductos.producto_a_eliminar.currentText()
        if codigo != "Seleccionar producto":
            codigo = int(codigo)
            print(codigo)
            self.producto.eliminarProducto(codigo)
        else:
            print("selecciona un producto")
        
    def modificarProducto(self):
        codigo = self.opcionesProductos.codigo_modificar_producto.text()
        print(codigo)
        if codigo is not None or "":
            codigo = int(codigo)
            productos = self.producto.buscarProducto(codigo)
            print(productos)
            self.modiProducto(codigo,productos)
        else:
            print("Ingresa un codigo correcto")
            
    def modiProducto(self,codigo,productos):
        if productos:
            nombre_proveedor = productos[0]
            self.opcionesProductos.nuevo_nombre_producto.setText(str(productos[0]))
            self.opcionesProductos.nuevo_nombre_producto_2.setValue(int(productos[1]))
            self.opcionesProductos.nueva_descripcion_producto.setPlainText(str(productos[2]))
            self.opcionesProductos.nuevo_precio_producto.setText(str(productos[3]))
            self.modiCategoria()
            self.modiProveedor()
            self.opcionesProductos.nuevo_nombre_producto.setReadOnly(False)
            self.opcionesProductos.nuevo_nombre_producto_2.setReadOnly(False)
            self.opcionesProductos.nueva_descripcion_producto.setReadOnly(False) 
            self.opcionesProductos.nuevo_precio_producto.setReadOnly(False) 
            self.opcionesProductos.nuevo_id_categoria_producto.setEditable(False)
            self.opcionesProductos.nuevo_nit_proveedor_producto.setEditable(False)
            self.opcionesProductos.nueva_fecha_vencimiento.setReadOnly(False) 
            self.opcionesProductos.btnModificar.setEnabled(True) 
        else:
            print("Proveedor no encontrado o datos vacíos") 
            
    def cambiarDatos(self):
        codigo = self.opcionesProductos.codigo_modificar_producto.text()
        nombre = self.opcionesProductos.nuevo_nombre_producto.text()
        cantidad = self.opcionesProductos.nuevo_nombre_producto_2.text()
        descripcion = self.opcionesProductos.nueva_descripcion_producto.toPlainText()
        precio = self.opcionesProductos.nuevo_precio_producto.text()
        categoria = self.opcionesProductos.nuevo_id_categoria_producto.currentText()
        proveedor = self.opcionesProductos.nuevo_nit_proveedor_producto.currentText()
        fecha_vencimiento = self.opcionesProductos.nueva_fecha_vencimiento.text()
        print(fecha_vencimiento)
        datos = [nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento]
        if self.validar.validarDatos(datos):
            print("ok")
            if categoria != "Seleccionar categoria" and proveedor != "Seleccionar proveedor":
                print("mas que bien")
                if int(cantidad) > 0:
                    cantidad = int(cantidad)
                    precio = int(precio)
                    categoria = int(categoria)
                    proveedor = int(proveedor)
                    codigo = int(codigo)
                    if fecha_vencimiento == "1/01/2000":
                        fecha_vencimiento = None
                        enviar = [nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento,codigo]
                        self.producto.modificarProducto(enviar)
                        print("todo perfecto")
                    else:
                        enviar = [nombre,cantidad,descripcion,precio,categoria,proveedor,fecha_vencimiento,codigo]
                        self.producto.modificarProducto(enviar)
                        print("todo perfe")
                else:
                    print("ingresa una cantidad valida")
            else:
                print("ingresa una categoria y proveedor")
        else:
            print("not ok")

    def productos(self):
        self.opcionesProductos.producto_a_eliminar.clear()
        productos = self.producto.productos()
        self.opcionesProductos.producto_a_eliminar.addItem("Seleccionar producto")
        for producto in productos:
            self.opcionesProductos.producto_a_eliminar.addItem(str(producto[0]))
        self.opcionesProductos.producto_a_eliminar.setCurrentIndex(0)
    
    def modiCategoria(self):
        self.opcionesProductos.nuevo_id_categoria_producto.clear()
        categorias = self.categoria.obtenerIdsCategoria()
        self.opcionesProductos.nuevo_id_categoria_producto.addItem("Seleccionar categoria")
        for categoria in categorias:
            self.opcionesProductos.nuevo_id_categoria_producto.addItem(str(categoria[0]))
        self.opcionesProductos.nuevo_id_categoria_producto.setCurrentIndex(0)

    def modiProveedor(self):
        self.opcionesProductos.nuevo_nit_proveedor_producto.clear()
        proveedores = self.proveedor.obtenerIdProveedores()
        self.opcionesProductos.nuevo_nit_proveedor_producto.addItem("Seleccionar proveedor")
        for proveedor in proveedores:
            self.opcionesProductos.nuevo_nit_proveedor_producto.addItem(str(proveedor[0]))
        self.opcionesProductos.nuevo_nit_proveedor_producto.setCurrentIndex(0)
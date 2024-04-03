from Models.categoriaProducto import CategoriaProducto
from Models.proveedor import Proveedor


class Producto:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS producto
                (codigo_producto INT NOT NULL,
                nombre_producto VARCHAR(90) NOT NULL,
                cantidad INT NOT NULL,
                descripcion VARCHAR(200) NOT NULL,
                precio_unitario INT NOT NULL,
                id_categoria INT NOT NULL,
                nit_proveedor INT NOT NULL,
                fecha_vencimiento DATE,
                FOREIGN KEY (id_categoria) REFERENCES categoria_producto(id_categoria_producto)  ON DELETE CASCADE,
                FOREIGN KEY (nit_proveedor) REFERENCES proveedor(nit_proveedor)  ON DELETE CASCADE,
                PRIMARY KEY (codigo_producto)
                )"""
            cursor.execute(sql)
        self.conn.commit()

   
    def obtenerProductos(self):
        try:
            with self.conn.cursor() as cursor:
                sql = """
                    SELECT producto.codigo_producto,producto.nombre_producto,producto.cantidad,producto.descripcion,producto.precio_unitario, c.nombre_categoria,p.nombre_proveedor FROM producto
                    inner join categoria_producto c on c.id_categoria_producto = producto.id_categoria inner join
                    proveedor p on p.nit_proveedor = producto.nit_proveedor         
                    """
                cursor.execute(sql)
                consulta = cursor.fetchall()
                self.conn.commit()
                cursor.close()
                return consulta
        except Exception as e:
            print(f"Error al ejecutar consulta: {str(e)}")
            return []  # Devolver una lista vacía en caso de error
      
    def ventaProductos(self,consulta,codigo):
        with self.conn.cursor() as cursor:
            sql = consulta
            cursor.execute(sql,(codigo,))
            consulta = cursor.fetchone()
            return consulta
        
    def buscador(self, palabra):
        with self.conn.cursor() as cursor:
            #sql = """SELECT * FROM producto WHERE nombre_producto LIKE %s OR codigo_producto LIKE %s"""
            sql = """SELECT producto.codigo_producto,producto.nombre_producto,producto.cantidad,producto.descripcion,producto.precio_unitario, c.nombre_categoria,p.nombre_proveedor FROM producto
            inner join categoria_producto c on c.id_categoria_producto = producto.id_categoria inner join
            proveedor p on p.nit_proveedor = producto.nit_proveedor WHERE nombre_producto LIKE %s OR codigo_producto LIKE %s"""
            cursor.execute(sql, ('%' + palabra + '%', '%' + palabra + '%'))
            resultados = cursor.fetchall()
            return resultados
        
    def agregarProducto(self,datos):
        try:
            with self.conn.cursor() as cursor:
                datos_a_insertar = datos
                consulta = """INSERT INTO producto (codigo_producto, nombre_producto, cantidad,descripcion,precio_unitario,id_categoria,nit_proveedor,fecha_vencimiento) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"""
                cursor.execute(consulta, datos_a_insertar)
                self.conn.commit()
                print("Datos insertados correctamente en la tabla 'producto'")
                cursor.close()
        except Exception as e:
            print(f"Error al insertar datos en la tabla 'producto': {e}")
        
        
    def codigo(self,codigo):
        with self.conn.cursor() as cursor:
            sql = """SELECT codigo_producto FROM producto WHERE codigo_producto = %s"""
            cursor.execute(sql, (codigo,))
            resultados = cursor.fetchall()
            return bool(resultados)
        
    def productos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codigo_producto from producto"""
            cursor.execute(sql)
            consulta = cursor.fetchall()
            cursor.close()
            print(consulta)
        return consulta
    
    def eliminarProducto(self,codigo):
        with self.conn.cursor() as cursor:
            consulta = """DELETE FROM producto WHERE codigo_producto = %s"""
            cursor.execute(consulta, codigo)
            self.conn.commit()
            cursor.close()
            print("producto eliminado")
    
    def buscarProducto(self,codigo):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_producto,cantidad,descripcion,precio_unitario,id_categoria,nit_proveedor,fecha_vencimiento from producto WHERE codigo_producto = %s"""
            cursor.execute(consulta,codigo)
            consulta = cursor.fetchone()
            cursor.close()
            print(consulta)
            return consulta
        
    def modificarProducto(self,datos):
        with self.conn.cursor() as cursor:
            consulta = """UPDATE producto SET nombre_producto = %s, cantidad = %s,descripcion = %s,precio_unitario = %s,id_categoria = %s,nit_proveedor = %s,fecha_vencimiento = %s WHERE codigo_producto = %s"""
            cursor.execute(consulta,datos)
            self.conn.commit()
            cursor.close()
            print(datos)
            print("datos modificados") 
            
    def actualizarCantidad(self,datos):
        print("ENTRASTE A ACTUALIZAR CANTIDAD")
        with self.conn.cursor() as cursor:
            consulta = """UPDATE producto SET cantidad = cantidad - %s WHERE codigo_producto = %s"""
            cursor.execute(consulta,datos)
            self.conn.commit()
            cursor.close()
            print("datos modificados") 
    
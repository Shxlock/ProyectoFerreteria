from Models.categoriaProducto import CategoriaProducto
from Models.proveedor import Proveedor
from Models.inventario import Inventario

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
                id_inventario INT NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categoria_producto(id_categoria_producto),
                FOREIGN KEY (nit_proveedor) REFERENCES proveedor(nit_proveedor),
                FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario),
                PRIMARY KEY (codigo_producto)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
        
    def obtenerProductos(self,consulta):
        with self.conn.cursor() as cursor:
            sql = consulta
            cursor.execute(sql)
            consulta = cursor.fetchall()
            return consulta
        
    def ventaProductos(self,consulta,codigo):
        with self.conn.cursor() as cursor:
            sql = consulta
            cursor.execute(sql,(codigo,))
            consulta = cursor.fetchone()
            return consulta
        
    def buscador(self, palabra):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM producto WHERE nombre_producto LIKE %s OR codigo_producto LIKE %s"""
            cursor.execute(sql, ('%' + palabra + '%', '%' + palabra + '%'))
            resultados = cursor.fetchall()
            return resultados
        
    def codigo(self,codigo):
        with self.conn.cursor() as cursor:
            sql = """SELECT codigo_producto FROM producto WHERE codigo_producto = %s"""
            cursor.execute(sql, (codigo,))
            resultados = cursor.fetchall()
            return bool(resultados)
        
    # def ventas(self):
    #     with self.conn.cursor() as cursor:
    #         sql = """SELECT codigo_producto FROM producto WHERE codigo_producto = %s"""
    #         cursor.execute(sql, (codigo,))
    #         resultados = cursor.fetchall()
    #         return resultados
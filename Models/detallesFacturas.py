from Models.factura import Factura
from Models.producto import Producto
from Models.empleado import Empleado
class DetallesFacturas:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS detalles_facturas
                (codigo_detalles VARCHAR(10) NOT NULL,
                codigo_factura INT NOT NULL,
                codigo_producto INT NOT NULL,
                cantidad INT NOT NULL,
                precio_unitario INT NOT NULL,
                FOREIGN KEY (codigo_factura) REFERENCES factura(codigo_factura) ON DELETE CASCADE,  
                FOREIGN KEY (codigo_producto) REFERENCES producto(codigo_producto) ON DELETE CASCADE,  
                PRIMARY KEY (codigo_detalles)
                )"""

            cursor.execute(sql)
        self.conn.commit()
        
    def obtener_historial(self):
        with self.conn.cursor() as cursor:
            consulta = """
            SELECT df.codigo_detalles,f.codigo_factura,f.cedula_empleado,e.nombre_empleado,f.nit_cliente,f.fecha,p.codigo_producto,p.nombre_producto, df.cantidad,df.precio_unitario FROM detalles_facturas as df
            inner join factura f on df.codigo_factura = f.codigo_factura inner join producto p on  df.codigo_producto = p.codigo_producto
            inner join empleado e on f.cedula_empleado = e.cedula_empleado
            """
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            self.conn.commit()
            cursor.close()
            print(consulta)
            return consulta 


    def insertarDatos(self,datos):
        with self.conn.cursor() as cursor:
            datos_a_insertar = datos
            consulta = """INSERT INTO detalles_facturas (codigo_detalles,codigo_factura,codigo_producto,cantidad,precio_unitario) VALUES (%s,%s, %s, %s, %s)"""
            cursor.execute(consulta, datos_a_insertar)
            self.conn.commit()
            cursor.close()
            return "Hecho detalles"
from Models.factura import Factura
from Models.producto import Producto
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
                FOREIGN KEY (codigo_factura) REFERENCES factura(codigo_factura),  
                FOREIGN KEY (codigo_producto) REFERENCES producto(codigo_producto),  
                PRIMARY KEY (codigo_detalles)
                )"""

            cursor.execute(sql)
        self.conn.commit()
        
        
    def insertarDatos(self,datos):
        with self.conn.cursor() as cursor:
            datos_a_insertar = datos
            consulta = """INSERT INTO detalles_facturas (codigo_detalles,codigo_factura,codigo_producto,cantidad,precio_unitario) VALUES (%s,%s, %s, %s, %s)"""
            cursor.execute(consulta, datos_a_insertar)
            self.conn.commit()
            cursor.close()
            return "Hecho detalles"
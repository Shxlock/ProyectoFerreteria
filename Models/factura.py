from Models.cliente import Cliente
from Models.empleado import Empleado

class Factura:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS factura
                (codigo_factura INT NOT NULL,
                tipo_de_pago VARCHAR(90) NOT NULL,
                email VARCHAR(100),
                turno VARCHAR(49) NOT NULL,
                fecha DATE NOT NULL,
                nit_cliente INT NOT NULL,
                cedula_empleado INT NOT NULL,
                FOREIGN KEY (nit_cliente) REFERENCES cliente(nit_cliente) ON DELETE CASCADE,
                FOREIGN KEY (cedula_empleado) REFERENCES empleado(cedula_empleado) ON DELETE CASCADE,
                PRIMARY KEY (codigo_factura)
                )"""

            cursor.execute(sql)
        self.conn.commit()
        
    def insertarDatos(self,datos):
        with self.conn.cursor() as cursor:
            datos_a_insertar = datos
            consulta = """INSERT INTO factura (codigo_factura,tipo_de_pago,email,turno,fecha,nit_cliente,cedula_empleado) VALUES (%s, %s, %s,%s,%s,%s,%s)"""
            cursor.execute(consulta, datos_a_insertar)
            self.conn.commit()
            cursor.close()
            return "Factura creada"
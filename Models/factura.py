from cliente import Cliente
from empleado import Empleado

class Factura:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS factura
                (codigo_factura INT NOT NULL,
                tipo_de_pago VARCHAR(90) NOT NULL,
                email VARCHAR(100) NOT NULL,
                turno VARCHAR(49) NOT NULL,
                fecha VARCHAR(200) INT NOT NULL,
                nit_cliente INT NOT NULL,
                cedula_empleado INT NOT NULL,
                FOREIGN KEY (nit_cliente) REFERENCES cliente(nit_cliente),
                FOREIGN KEY (cedula_empleado) REFERENCES empleado(cedula_empleado),
                PRIMARY KEY (codigo_factura)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
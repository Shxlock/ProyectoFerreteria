from cliente import Cliente
from producto import Producto
from factura import Factura

class Venta:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS venta
                (codigo_venta INT(20) NOT NULL,
                fecha_venta VARCHAR(90) NOT NULL,
                nit_cliente INT NOT NULL,
                codigo_producto INT NOT NULL,
                codigo_factura INT NOT NULL,
                FOREIGN KEY (nit_cliente) REFERENCES cliente(nit_cliente),
                FOREIGN KEY (codigo_producto) REFERENCES producto(nit_proveedor),
                FOREIGN KEY (codigo_factura) REFERENCES factura(codigo_factura),
                PRIMARY KEY (codigo_venta)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
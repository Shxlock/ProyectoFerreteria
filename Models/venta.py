from Models.cliente import Cliente
from Models.producto import Producto


class Venta:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS venta
                (codigo_venta VARCHAR(6) NOT NULL,
                fecha_venta VARCHAR(90) NOT NULL,
                nit_cliente INT NOT NULL,
                codigo_producto INT NOT NULL,
                FOREIGN KEY (nit_cliente) REFERENCES cliente(nit_cliente),
                FOREIGN KEY (codigo_producto) REFERENCES producto(codigo_producto),
                PRIMARY KEY (codigo_venta)
                )"""

            cursor.execute(sql)
        self.conn.commit()
        
    def ObtenerDatos(self):
        pass 
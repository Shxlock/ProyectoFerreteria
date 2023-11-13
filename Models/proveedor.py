class Proveedor:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS proveedor
                (nit_proveedor INT NOT NULL,
                nombre_proveedor VARCHAR(90) NOT NULL,
                telefono_proveedor INT NOT NULL,
                email_proveedor VARCHAR(90) NOT NULL,
                direccion_proveedor VARCHAR(90) NOT NULL,
                ciudad_proveedor VARCHAR(90) NOT NULL,
                PRIMARY KEY (nit_proveedor)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
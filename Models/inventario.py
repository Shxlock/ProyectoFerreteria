class Inventario:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS inventario
                (id_inventario INT(20) NOT NULL,
                nombre_inventario VARCHAR(90) NOT NULL,
                stock_inventario INT(1000) NOT NULL,
                precio_unitario INT NOT NULL,
                PRIMARY KEY (id_inventario)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
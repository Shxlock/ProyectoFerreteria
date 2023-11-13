class Cliente:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS cliente
            (nit_cliente INT NOT NULL,
            nombre_cliente VARCHAR(90) NOT NULL,
            apellido_cliente VARCHAR(90) NOT NULL,
            telefono_cliente INT NOT NULL,
            email_cliente VARCHAR(90) NOT NULL,
            PRIMARY KEY (nit_cliente)
            )"""

            cursor.execute(sql)
        self.conn.commit()
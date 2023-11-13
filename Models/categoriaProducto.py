class CategoriaProducto:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS categoria_producto
                (id_categoria_producto INT NOT NULL AUTO_INCREMENT,
                nombre_categoria VARCHAR(90) NOT NULL,
                PRIMARY KEY (id_categoria_producto)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
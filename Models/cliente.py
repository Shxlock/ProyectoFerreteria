class Cliente:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS cliente
            (nit_cliente INT NOT NULL,
            nombre_cliente VARCHAR(90) NOT NULL,
            email_cliente VARCHAR(90),
            PRIMARY KEY (nit_cliente)
            )"""

            cursor.execute(sql)
        self.conn.commit()
        
    def obtenerClientes(self):
        with self.conn.cursor() as cursor:
            consulta = "SELECT * FROM cliente"
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            self.conn.commit()
            cursor.close()
            print(consulta)
            return consulta 

    def insertarDatos(self,datos):
        with self.conn.cursor() as cursor:
            consulta = "INSERT INTO cliente (nit_cliente, nombre_cliente, email_cliente) VALUES (%s, %s, %s)"
            cursor.execute(consulta, datos)
            self.conn.commit()
            cursor.close()
            return "Hecho Cliente"
        
    def existeCliente(self, cliente):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nit_cliente FROM cliente WHERE nit_cliente = %s"""
            cursor.execute(consulta, (cliente,))
            resultado = cursor.fetchone()
            return resultado is not None

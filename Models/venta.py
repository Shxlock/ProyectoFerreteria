# from Models.cliente import Cliente


# class Venta:
#     def __init__(self,conn):
#         self.conn = conn
#         with self.conn.cursor() as cursor:
#             sql = """
#                 CREATE TABLE IF NOT EXISTS venta
#                 (codigo_venta VARCHAR(6) NOT NULL,
#                 fecha_venta VARCHAR(90) NOT NULL,
#                 nit_cliente INT NOT NULL,
#                 FOREIGN KEY (nit_cliente) REFERENCES cliente(nit_cliente),
#                 PRIMARY KEY (codigo_venta)
#                 )"""

#             cursor.execute(sql)
#         self.conn.commit()
        
#     def ObtenerDatos(self):
#         pass 
    
#     def insertDatos(self,datos):
#         with self.conn.cursor() as cursor:
#             datos_a_insertar = datos
#             consulta = """INSERT INTO venta (codigo_venta,fecha_venta,nit_cliente) VALUES (%s, %s, %s)"""
#             cursor.execute(consulta, datos_a_insertar)
#             self.conn.commit()
#             cursor.close()
#             return "Hecho venta"
        
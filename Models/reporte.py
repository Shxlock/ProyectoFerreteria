# from User import User

# class Reporte:
#     def __init__(self,conn):
#         self.conn = conn
#         with self.conn.cursor() as cursor:
#             sql = """CREATE TABLE IF NOT EXISTS reporte
#                 (id_reporte INT NOT NULL AUTO_INCREMENT
#                 id_usuario INT NOT NULL,
#                 datos_nuevos VARCHAR(200) NOT NULL,
#                 datos_viejos VARCHAR(200) NOT NULL,
#                 FOREIGN KEY (id_usuario) REFERENCES user(user_id),
#                 PRIMARY KEY (id_reporte)
#                 )"""

#             cursor.execute(sql)
#         self.conn.commit()
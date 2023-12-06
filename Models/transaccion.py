# from User import User

# class Transaccion:
#     def __init__(self,conn):
#         self.conn = conn
#         with self.conn.cursor() as cursor:
#             sql = """CREATE TABLE IF NOT EXISTS transaccion
#                 (id_transaccion INT NOT NULL AUTO_INCREMENT
#                 id_usuario INT NOT NULL,
#                 FOREIGN KEY (id_usuario) REFERENCES user(user_id),
#                 PRIMARY KEY (id_transaccion)
#                 )"""

#             cursor.execute(sql)
#         self.conn.commit()
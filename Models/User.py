class User:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS user
                (user_id INT NOT NULL AUTO_INCREMENT,
                user VARCHAR(191) NOT NULL,
                password VARCHAR(191) NOT NULL,
                salt VARCHAR(255) NOT NULL,
                rol VARCHAR(50) NOT NULL,
                PRIMARY KEY (user_id)
                )"""

            cursor.execute(sql)
        self.conn.commit()
class User:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS user
                (user_id VARCHAR(21) NOT NULL,
                user VARCHAR(191) NOT NULL,
                password VARCHAR(191) NOT NULL,
                salt VARCHAR(255) NOT NULL
                )"""
                    
            cursor.execute(sql)
            self.conn.commit()
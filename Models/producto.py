from categoriaProducto import CategoriaProducto
from proveedor import Proveedor
from inventario import Inventario

class Producto:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS producto
                (codigo_producto INT(20) NOT NULL,
                nombre_producto VARCHAR(90) NOT NULL,
                cantidad INT NOT NULL,
                descripcion VARCHAR NOT NULL,
                precio_unitario INT NOT NULL,
                id_categoria INT NOT NULL,
                nit_proveedor INT NOT NULL,
                id_inventario INT NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categoria_producto(id_categoria_producto),
                FOREIGN KEY (nit_proveedor) REFERENCES proveedor(nit_proveedor),
                FOREIGN KEY (id_inventario) REFERENCES inventario(id_inventario),
                PRIMARY KEY (codigo_producto)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()
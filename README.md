Este es un proyecto creado con Python usando PyQt5. 

Para el correcto funcionamiento de esta GUI se ha de instalar las siguientes librerias:

pip install PyQt5
pip install pymysql
pip install uuid
pip install bcrypt

Además de esto,  se debe configurar tanto el xampp como la direccion de correo electronico y su contraseña (Se recomienda usar variables de entorno y contraseñas de aplicacion)


Configuracion Correo Electronico:

en el archivo controladorCorreos.py:

remitente = "" # correo
contraseña = "" # contraseña

cambiar esas lineas por su correspondiente correo y contraseña

Configuracion XAMPP:
![image](https://github.com/Shxlock/ProyectoFerreteria/assets/149827696/1e85ff95-eff6-4a8a-a69b-449d63a981a6)

segun tu configuracion del xampp cambiar las siguientes lineas de codigo:

import pymysql

def connection():
    conn = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "",
        database = "ferreteria_proyecto",
)

Ahora solo faltaría abrir el admin de MySQL en xampp, crear la base de datos e importar la base de datos.

Tras haber hecho esto, ya podrias utilizar la GUI sin ningun problema. 

    

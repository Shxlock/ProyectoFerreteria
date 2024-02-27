import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_correo(destinatario, asunto,precio,cantidad,total_pagar):
    # Configuración de las credenciales
    remitente = "igshylock07@gmail.com"
    contraseña = "cljb kbag yhkr xahg"

    # Configurar el servidor SMTP de Gmail
    servidor_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    servidor_smtp.login(remitente, contraseña)

    # Crear el objeto del mensaje
    mensaje_correo = MIMEMultipart('alternative')
    mensaje_correo['From'] = remitente
    mensaje_correo['To'] = destinatario
    mensaje_correo['Subject'] = asunto

    # Crear el cuerpo del mensaje en formato HTML
    cuerpo_html = f"""
    <html>
      <head></head>
      <body style="display: flex;justify-content:center; flex-direction:column;">
        <div>
        <img src="https://pbs.twimg.com/profile_images/1580464685480132608/_ZonfdcY_400x400.jpg">
        <p style="color: blue; font-size: 18px; display:block; text-align:center;">¡Hola!</p><br>
        <p>Este es un correo de prueba con <b>estilos y etiquetas HTML</b>.</p><br>
        <p>El precio es: {precio} y la cantidad: {cantidad}</p><br>
        <p>El total a pagar es: {total_pagar}</p>
        </div>
      </body>
    </html>
    """
    mensaje_html = MIMEText(cuerpo_html, 'html')

    # Adjuntar el cuerpo del mensaje HTML al objeto del mensaje
    mensaje_correo.attach(mensaje_html)

    



    # Enviar el correo electrónico
    servidor_smtp.sendmail(remitente, destinatario, mensaje_correo.as_string())

    # Cerrar la conexión con el servidor SMTP
    servidor_smtp.quit()

# Ejemplo de uso
destinatario = 'wilmeralexanderberbesimartinez@gmail.com'
asunto = 'Correo de prueba con HTML'

precio = 1000
cantidad = 4
total_pagar = precio * cantidad


enviar_correo(destinatario, asunto, precio,cantidad, total_pagar)
print("mensaje enviado")










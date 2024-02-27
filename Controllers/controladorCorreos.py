import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ControladorCorreos():

    def __init__(self,principal):
        self.principal = principal

    def enviar_correo(self,destinatario,productos,cliente,total_pagar):
        remitente = "" # correo
        contraseña = "" # contraseña
        servidor_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        servidor_smtp.login(remitente, contraseña)
        mensaje_correo = MIMEMultipart('alternative')
        mensaje_correo['From'] = remitente
        mensaje_correo['To'] = destinatario
        mensaje_correo['Subject'] = 'Factura AeroNorte'

        cuerpo_html = f"""
        <html>
        <head></head>
        <body style="display: flex;justify-content:center; flex-direction:column;">
            <div>
            <img src="https://i.postimg.cc/xCGJjsR2/logoferreteria-png-HD.png">
            <p style="color: blue; font-size: 18px; display:block; text-align:center;">¡Hola! {cliente}</p><br>
            <p>Aqui esta tu factura de <b>AeroNorte</b>.</p><br>
            <p>{total_pagar}</p><br>
            </div>
        </body>
        </html>
        """
        mensaje_html = MIMEText(cuerpo_html, 'html')
        mensaje_correo.attach(mensaje_html)
        servidor_smtp.sendmail(remitente, destinatario, mensaje_correo.as_string())
        servidor_smtp.quit()
        destinatario = destinatario
        print("mensaje enviado") 

        

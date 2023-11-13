import uuid

def generar_codigo_venta():
    codigo_venta = str(uuid.uuid4())
    codigo_venta = codigo_venta[:6]  
    codigo_venta = codigo_venta.upper()
    return codigo_venta

codigo_venta_generado = generar_codigo_venta()
print("Código de venta generado:", codigo_venta_generado)

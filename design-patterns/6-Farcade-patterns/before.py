#
# CÓDIGO INICIAL: EL CLIENTE CONOCE TODA LA COMPLEJIDAD
#

# --- El subsistema complejo ---
class SistemaInventario:
    def verificar_stock(self, producto_id: str) -> bool:
        print(f"INVENTARIO: Verificando stock para el producto {producto_id}...")
        # Lógica compleja para verificar en múltiples almacenes...
        return True

class SistemaPagos:
    def procesar_pago(self, usuario_id: str, monto: float) -> bool:
        print(f"PAGOS: Procesando pago de ${monto} para el usuario {usuario_id}...")
        # Lógica compleja para interactuar con la pasarela de pago...
        return True

class SistemaEnvios:
    def crear_envio(self, usuario_id: str, producto_id: str):
        print(f"ENVIOS: Creando envío del producto {producto_id} para el usuario {usuario_id}...")
        # Lógica compleja para calcular costos y generar una guía...
        return "GUIA-XYZ-123"

# --- Código cliente (ej: un endpoint de una API) ---
def cliente_realizar_pedido(usuario_id: str, producto_id: str, precio: float):
    print("\nCLIENTE: Intentando realizar un pedido...")
    
    # El cliente tiene que conocer y orquestar todo el proceso.
    inventario = SistemaInventario()
    pagos = SistemaPagos()
    envios = SistemaEnvios()

    if inventario.verificar_stock(producto_id):
        print("CLIENTE: Hay stock.")
        if pagos.procesar_pago(usuario_id, precio):
            print("CLIENTE: El pago fue exitoso.")
            guia = envios.crear_envio(usuario_id, producto_id)
            print(f"CLIENTE: Pedido completado. Guía de envío: {guia}")
        else:
            print("CLIENTE: El pago falló. Pedido cancelado.")
    else:
        print("CLIENTE: No hay stock. Pedido cancelado.")

# --- Simulación ---
print("Ejecutando el código problemático:")
cliente_realizar_pedido(usuario_id="user-001", producto_id="ps5", precio=499.99)
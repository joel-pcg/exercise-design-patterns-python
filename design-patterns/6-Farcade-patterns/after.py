#
# CÓDIGO FINAL: APLICANDO FACADE
#

# El subsistema complejo sigue siendo el mismo. No lo tocamos.
class SistemaInventario:
    def verificar_stock(self, producto_id: str) -> bool:
        print(f"INVENTARIO: Verificando stock para el producto {producto_id}...")
        return True

class SistemaPagos:
    def procesar_pago(self, usuario_id: str, monto: float) -> bool:
        print(f"PAGOS: Procesando pago de ${monto} para el usuario {usuario_id}...")
        return True

class SistemaEnvios:
    def crear_envio(self, usuario_id: str, producto_id: str):
        print(f"ENVIOS: Creando envío del producto {producto_id} para el usuario {usuario_id}...")
        return "GUIA-XYZ-123"

# --- Pasos 2, 3 y 4: La Fachada ---
class FachadaPedidos:
    """
    La Fachada. Oculta la complejidad del subsistema de pedidos.
    Es el único punto de entrada para el cliente.
    """
    def __init__(self):
        # La fachada puede crear las instancias del subsistema o recibirlas.
        self._inventario = SistemaInventario()
        self._pagos = SistemaPagos()
        self._envios = SistemaEnvios()

    def realizar_pedido(self, usuario_id: str, producto_id: str, precio: float) -> bool:
        print("\nFACHADA: Orquestando el proceso de pedido...")
        
        if not self._inventario.verificar_stock(producto_id):
            print("FACHADA: No hay stock. Pedido cancelado.")
            return False
        
        if not self._pagos.procesar_pago(usuario_id, precio):
            print("FACHADA: El pago falló. Pedido cancelado.")
            return False
            
        guia = self._envios.crear_envio(usuario_id, producto_id)
        print(f"FACHADA: Pedido completado. Guía de envío: {guia}")
        return True

# --- Código cliente (ahora mucho más simple) ---
def cliente_refactorizado(usuario_id: str, producto_id: str, precio: float):
    print("\nCLIENTE: Intentando realizar un pedido (con fachada)...")
    fachada = FachadaPedidos()
    fachada.realizar_pedido(usuario_id, producto_id, precio)

# --- Simulación ---
print("\nEjecutando el código refactorizado con Facade:")
cliente_refactorizado(usuario_id="user-001", producto_id="ps5", precio=499.99)
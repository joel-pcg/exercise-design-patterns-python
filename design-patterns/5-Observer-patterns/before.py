#
# CÓDIGO INICIAL: ALTO ACOPLAMIENTO
#

class NotificadorEmail:
    def enviar_alerta_stock(self, nombre_producto: str):
        print(f"EMAIL: ¡El producto '{nombre_producto}' está de vuelta en stock!")

class NotificadorSMS:
    def enviar_alerta_stock(self, nombre_producto: str):
        print(f"SMS: ¡Hey! '{nombre_producto}' ya está disponible. ¡Cómpralo ya!")

class Producto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._disponible = False
    
    @property
    def disponible(self) -> bool:
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor: bool):
        if valor and not self._disponible:
            print(f"\nPRODUCTO: '{self.nombre}' ha cambiado su estado a DISPONIBLE.")
            self._disponible = valor
            # !!! PROBLEMA: La clase Producto está acoplada a los notificadores.
            # !!! Conoce las clases concretas y cómo llamarlas.
            email_notifier = NotificadorEmail()
            email_notifier.enviar_alerta_stock(self.nombre)
            
            sms_notifier = NotificadorSMS()
            sms_notifier.enviar_alerta_stock(self.nombre)
        elif not valor and self._disponible:
            print(f"PRODUCTO: '{self.nombre}' ha cambiado su estado a NO DISPONIBLE.")
            self._disponible = valor

# --- Código cliente ---
print("Ejecutando el código problemático:")
ps5 = Producto("PlayStation 5")
ps5.disponible = True
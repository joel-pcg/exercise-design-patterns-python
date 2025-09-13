#
# CÓDIGO FINAL : APLICANDO DECORATOR PATTERN
#

from abc import ABC, abstractmethod

class ComponenteNotificador(ABC):
    """Interfaz común para el notificador y los decoradores.""" 
    @abstractmethod
    def enviar(self, mensaje: str):
        pass
    

class Notificador(ComponenteNotificador):
    def enviar(self, mensaje: str):
        print(f"Notificación base (consola): '{mensaje}'")


class DecoradorBase(ComponenteNotificador):
    """
        El decorador base sigue la misma interfaz que los otros componentes.
        Mantiene una referencia al objeto envuelto.
    """
    _componente: ComponenteNotificador 

    def __init__(self, componente: ComponenteNotificador):
        self._componente = componente

    @property
    def componente(self) -> ComponenteNotificador:
        """Permite acceder al componente decorado."""
        return self._componente
    
    def enviar(self, mensaje: str):
        # Delega el trabajo al componente envuelto.
        self._componente.enviar(mensaje)

class DecoradorSlack(DecoradorBase):
    def enviar(self, mensaje: str):
        # Llama al método del componente base.
        super().enviar(mensaje)
        # Añade la funcionalidad específica de Slack.
        print(f"Enviando a Slack: '{mensaje}'")

class DecoradorSMS(DecoradorBase):
    def enviar(self, mensaje: str):
        # Llama al método del componente base.
        super().enviar(mensaje)
        # Añade la funcionalidad específica de SMS.
        print(f"Enviando a SMS: '{mensaje}'")



# --- Código cliente ---
print("\nEjecutando el código refactorizado con Decorator:")

# 1. Empezamos con el componente simple.
notificador_simple = Notificador()
print("Cliente: Tengo un componente simple:")
notificador_simple.enviar("Hola Mundo")
print("-" * 20)

# 2. Ahora lo decoramos dinámicamente.
# Podemos envolverlo con un decorador de Slack.
notificador_con_slack = DecoradorSlack(notificador_simple)
print("Cliente: Ahora tengo un componente decorado con Slack:")
notificador_con_slack.enviar("El build ha terminado.")
print("-" * 20)

# 3. Podemos apilar decoradores. ¡Aquí está la magia!
# Quiero que notifique a la consola, luego a SMS y luego a Slack.
print("Cliente: Ahora tengo un componente con MÚLTIPLES decoradores:")
notificador_completo = DecoradorSlack(DecoradorSMS(notificador_simple))
notificador_completo.enviar("El servidor está caído.")


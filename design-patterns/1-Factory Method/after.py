#
# CÓDIGO INICIAL: PROBLEMA DE ACOPLAMIENTO
#
from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class NotificacionEmail(Notificacion):
    """Un producto concreto para enviar emails."""
    def enviar(self, mensaje: str):
        print(f"Enviando por Email: '{mensaje}'")

class NotificacionSMS(Notificacion):
    """Un producto concreto para enviar SMS."""
    def enviar(self, mensaje: str):
        print(f"Enviando por SMS: '{mensaje}'")

# --- Paso 3: Creador Abstracto (La Fábrica) ---


class CreadorNotificacion(ABC):
    """
    La clase 'Creador' (factory) declara el factory method que debe
    devolver un objeto de la clase Notificacion.
    """
    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        """
            Este es el factory method que crea un objeto Notificacion.
        """
        pass

    def enviar_notificacion(self, mensaje: str):
        """
        El código cliente usa este método. No conoce la clase concreta del notificador,
        solo sabe que puede '.enviar()'
        """
        notificador = self.crear_notificacion()
        notificador.enviar(mensaje)

# --- Paso 4: Creadores Concretos (Las fábricas concretas) ---
class CreaadorNotificacionEmail(CreadorNotificacion):
    """Una factory concreta para crear notificaciones por email."""
    def crear_notificacion(self) -> Notificacion:
        return NotificacionEmail()

class CreadorNotificacionSMS(CreadorNotificacion):
    """Un factory concreta para crear notificaciones por SMS."""
    def crear_notificacion(self) -> Notificacion:
        return NotificacionSMS()

def cliente(creador: CreadorNotificacion, mensaje: str):
    """
     El código cliente funciona con una instancia de un creador concreto,
    aunque a través de su interfaz base. Mientras el cliente siga trabajando
    con el creador base, puedes pasarle cualquier subclase de creador.
    """
    creador.enviar_notificacion(mensaje)

print("Ejecutando el código refactorizado con Factory Method:")
cliente(CreaadorNotificacionEmail(), "Tu pedido ha sido enviado.")
cliente(CreadorNotificacionSMS(), "Tu código de verificación es 12345.")
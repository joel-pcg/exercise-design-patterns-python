#
# CÓDIGO INICIAL: PROBLEMA DE ACOPLAMIENTO
#

class NotificacionEmail:
    """Una clase concreta para enviar emails."""
    def enviar(self, mensaje: str):
        print(f"Enviando por Email: '{mensaje}'")

class NotificacionSMS:
    """Una clase concreta para enviar SMS."""
    def enviar(self, mensaje: str):
        print(f"Enviando por SMS: '{mensaje}'")

def enviar_notificacion(tipo: str, mensaje: str):
    """
    Esta función crea y envía la notificación.
    !!! PROBLEMA: Está acoplada a las clases concretas.
    !!! Si añadimos un nuevo tipo (ej. Push), TENEMOS que modificar esta función.
    """
    if tipo == "email":
        notificador = NotificacionEmail()
        notificador.enviar(mensaje)
    elif tipo == "sms":
        notificador = NotificacionSMS()
        notificador.enviar(mensaje)
    else:
        raise ValueError("Tipo de notificación no soportado")

# --- Código cliente ---
print("Ejecutando el código problemático:")
enviar_notificacion("email", "Tu pedido ha sido enviado.")
enviar_notificacion("sms", "Tu código de verificación es 12345.")
# enviar_notificacion("push", "Esto fallará") # Descomentar para ver el error
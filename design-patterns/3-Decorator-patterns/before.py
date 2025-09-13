#
# CÓDIGO INICIAL: PROBLEMA DE LA "EXPLOSIÓN DE CLASES"
#

class NotificadorBase:
    def enviar(self, mensaje: str):
        print(f"Notificación base: '{mensaje}'")

# Si queremos añadir funcionalidades, la herencia nos tienta...
class NotificadorSlack(NotificadorBase):
    def enviar(self, mensaje: str):
        super().enviar(mensaje)
        print(f"Enviando a Slack: '{mensaje}'")

class NotificadorSMS(NotificadorBase):
    def enviar(self, mensaje: str):
        super().enviar(mensaje)
        print(f"Enviando a SMS: '{mensaje}'")

# !!! PROBLEMA: ¿Y si queremos AMBOS, Slack y SMS?
# Necesitamos una nueva clase para esa combinación específica.
class NotificadorSlackYsms(NotificadorBase):
    def enviar(self, mensaje: str):
        super().enviar(mensaje)
        print(f"Enviando a Slack: '{mensaje}'")
        print(f"Enviando a SMS: '{mensaje}'")

# --- Código cliente ---
print("Ejecutando el código problemático:")
notificador_completo = NotificadorSlackYsms()
notificador_completo.enviar("El servidor se reiniciará en 5 minutos.")

# Este enfoque no escala. Si añadimos Email, las combinaciones se disparan.
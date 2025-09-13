#
# CÓDIGO FINAL : APLICANDO OBSERVER PATTERN
#

from abc import ABC, abstractmethod
from typing import List

class ISubject(ABC):
    """
    
    """
    @abstractmethod
    def attach(self, observer: 'IObserver'):
        """Añade un observador al sujeto."""
        pass
    @abstractmethod
    def detach(self, observer: 'IObserver'):    
        pass
    @abstractmethod
    def notify(self):
        """Notifica a todos los observadores."""
        pass
    ...

class IObserver(ABC):
    @abstractmethod
    def update(self, subject: ISubject) -> None:
        pass


class Producto(ISubject):


    _observes: List[IObserver] = []
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._disponible = False
    

    def attach(self, observer: IObserver):
        print(f"ATTACH: Un observador se ha suscrito a '{self.nombre}'.")
        self._observes.append(observer)
    def detach(self, observer: IObserver):
            print(f"DETACH: Un observador se ha desuscrito de '{self.nombre}'.")
            self._observes.remove(observer)

    def notify(self):
        print("NOTIFY: Notificando a todos los observadores...")
        for observer in self._observes:
            observer.update(self)

    
    @property
    def disponible(self) -> bool:
        return self._disponible
    
    @disponible.setter
    def disponible(self, valor: bool):
        if valor and not self._disponible:
            print(f"\nPRODUCTO: '{self.nombre}' ha cambiado su estado a DISPONIBLE.")
            self._disponible = valor
            self.notify()
        elif not valor and self._disponible:
            print(f"PRODUCTO: '{self.nombre}' ha cambiado su estado a NO DISPONIBLE.")
            self._disponible = valor

class ObservadorEmail(IObserver):
    def update(self, subject: Producto) -> None: #type:ignore[override]
        if subject.disponible:
            print(f"EMAIL: ¡El producto '{subject.nombre}' está de vuelta en stock!")

class ObservadorSMS(IObserver):
    def update(self, subject: Producto) -> None: #type:ignore[override]
        if subject.disponible:
            print(f"SMS: ¡Hey! '{subject.nombre}' ya está disponible. ¡Cómpralo ya!")


# --- Código cliente ---
print("\nEjecutando el código refactorizado con Observer:")
# Creamos el sujeto
ps5 = Producto("PlayStation 5")

# Creamos los observadores
email_fan = ObservadorEmail()
sms_fan = ObservadorSMS()

# El cliente suscribe los observadores al sujeto
ps5.attach(email_fan)
ps5.attach(sms_fan)

# Cambiamos el estado del producto. Esto disparará las notificaciones.
ps5.disponible = True

# Un cliente decide que ya no quiere notificaciones por SMS
ps5.detach(sms_fan)

# Si el producto se agota y vuelve a estar disponible, solo se notifica por email
print("\n--- El producto se agota y vuelve ---")
ps5.disponible = False
ps5.disponible = True
#
# CÓDIGO FINAL: aplicnado el patrón Strategy
#

from abc import ABC, abstractmethod


class EstrategiaEnvio(ABC):
    """La interfaz para todas las estrategias de cálculo de envío."""
    @abstractmethod
    def calcular(self,orden: 'Orden') -> float:
        pass

class EstrategiaEnvioEstandar(EstrategiaEnvio):
    def calcular(self, orden: 'Orden') -> float:
        return max(5.0, orden.total_orden * 0.05)

class EstrategiaEnvioExpress(EstrategiaEnvio):
    def calcular(self, orden: 'Orden') -> float:
        return max(10.0, orden.total_orden * 0.10)

class EstrategiaEnvioPrioritario(EstrategiaEnvio):
    def calcular(self, orden: 'Orden') -> float:
        return 20.0

class Orden:
    def __init__(self, total_orden: float, estrategia: EstrategiaEnvio):
        self.total_orden = total_orden
        self.estrategia = estrategia

    def calcular_costo_envio(self) -> float:
        """
        Delega el cálculo a su objeto de estrategia.
        Ya no hay if/elif/else. La clase Orden no conoce los detalles del cálculo.
        """
        costo = self.estrategia.calcular(self)
        nombre_estrategia = self.estrategia.__class__.__name__.replace("EstrategiaEnvio", "").lower()
        print(f"Costo de envío ({nombre_estrategia}): ${costo:.2f}")
        return costo
    

# --- Código cliente ---
print("Ejecutando el código refactorizado con Strategy:")
orden_1 = Orden(total_orden=300.0, estrategia=EstrategiaEnvioEstandar())
orden_1.calcular_costo_envio()

orden_2 = Orden(total_orden=350.0,estrategia=EstrategiaEnvioExpress())
orden_2.calcular_costo_envio()

orden_3 = Orden(total_orden=600.0, estrategia=EstrategiaEnvioPrioritario())
orden_3.calcular_costo_envio()
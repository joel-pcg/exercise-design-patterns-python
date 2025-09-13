#
# CÓDIGO INICIAL: PROBLEMA CON CONDICIONALES
#

class Orden:
    def __init__(self, total_orden: float):
        self.total_orden = total_orden

    def calcular_costo_envio(self, metodo: str) -> float:
        """
        Calcula el costo de envío basado en una cadena de texto.
        !!! PROBLEMA: Un gran bloque if/elif/else.
        !!! Difícil de extender y mantener.
        """
        costo = 0.0
        if metodo == "estandar":
            # Lógica para envío estándar: 5% del total o un mínimo de 5
            costo = max(5.0, self.total_orden * 0.05)
        elif metodo == "express":
            # Lógica para envío express: 10% del total o un mínimo de 10
            costo = max(10.0, self.total_orden * 0.10)
        elif metodo == "prioritario":
            # Lógica para envío prioritario: Tarifa plana de 20
            costo = 20.0
        else:
            raise ValueError(f"Método de envío '{metodo}' no soportado.")
        
        print(f"Costo de envío ({metodo}): ${costo:.2f}")
        return costo

# --- Código cliente ---
print("Ejecutando el código problemático:")
orden_1 = Orden(total_orden=150.0)
orden_1.calcular_costo_envio("estandar")

orden_2 = Orden(total_orden=50.0)
orden_2.calcular_costo_envio("express")

orden_3 = Orden(total_orden=200.0)
orden_3.calcular_costo_envio("prioritario")
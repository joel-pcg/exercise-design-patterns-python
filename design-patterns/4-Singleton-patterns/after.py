#
# CÓDIGO FINAL: APLICANDO SINGLETON PATTERN
#



class singletonMeta(type):
    """
    Metaclase que convierte a una clase en Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class GestorConfiguracion(metaclass=singletonMeta):
    def __init__(self, config_file: str):
        self.settings = {}
        # Simulamos la carga de un fichero de configuración
        print(f"--- LEYENDO FICHERO {config_file} (operación costosa) ---")
        self.settings = {"database_url": "db_url_inicial", "api_key": "key_inicial"}

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings[key] = value

# --- Código cliente ---
print("Ejecutando el código problemático:")

# El Módulo A de la aplicación necesita la configuración
print("Módulo A:")
config_a = GestorConfiguracion("prod.json")
print(f"API Key: {config_a.get('api_key')}")

# El Módulo B, en otra parte de la app, también necesita la config
print("\nMódulo B:")
config_b = GestorConfiguracion("prod.json") # ¡¡Vuelve a leer el fichero!!

# Ahora, el Módulo A actualiza un valor
print("\nMódulo A actualiza un setting:")
config_a.set("api_key", "NUEVA_API_KEY_12345")
print(f"API Key en A: {config_a.get('api_key')}")

# *** SOLUCION: El Módulo B ahora ve el cambio por que es el mismo objeto.
print(f"API Key en B: {config_b.get('api_key')}")

# Comprobamos que son dos objetos diferentes en memoria
print(f"\n¿Son config_a y config_b el mismo objeto? {config_a is config_b}")
"""
Clase base: Vehiculo
--------------------
Representa un vehículo genérico. 
Más adelante se usará como clase padre de Coche, Autobus, Camion y Moto.
"""

class Vehiculo:
    # Atributo de clase (compartido por todas las instancias)
    total_vehiculos = 0

    def __init__(self, marca, modelo, color, velocidad_maxima, combustible):
        """
        Método constructor (__init__):
        Se ejecuta automáticamente al crear un nuevo objeto Vehiculo.
        Define los atributos básicos del vehículo.
        """
        self._marca = marca                # atributo protegido (convención: _nombre)
        self._modelo = modelo
        self._color = color
        self._velocidad_maxima = velocidad_maxima
        self._encendido = False            # estado inicial: apagado
        self._combustible = combustible

        # Cada vez que se crea un vehículo, se incrementa el contador de clase
        Vehiculo.total_vehiculos += 1

    # ========================
    #   MÉTODOS GETTER / SETTER
    # ========================

    def get_marca(self):
        """Devuelve la marca del vehículo."""
        return self._marca

    def set_marca(self, nueva_marca):
        """Cambia la marca del vehículo."""
        if not nueva_marca:
            raise ValueError("La marca no puede estar vacía.")
        self._marca = nueva_marca

    def get_color(self):
        """Devuelve el color actual del vehículo."""
        return self._color

    def set_color(self, nuevo_color):
        """Permite cambiar el color del vehículo."""
        if not isinstance(nuevo_color, str):
            raise ValueError("El color debe ser una cadena de texto.")
        self._color = nuevo_color

    def get_velocidad_maxima(self):
        """Devuelve la velocidad máxima."""
        return self._velocidad_maxima

    def set_velocidad_maxima(self, nueva_velocidad):
        """Cambia la velocidad máxima, con validación."""
        if nueva_velocidad <= 0:
            raise ValueError("La velocidad máxima debe ser positiva.")
        self._velocidad_maxima = nueva_velocidad


    #=================================
    #Getter and setter utilizando Property
    #====================================
    @property
    def combustible(self):
        return self._combustible

    @combustible.setter
    def combustible(self, valor_combustible):
        if isinstance(valor_combustible, str):
            self._combustible = valor_combustible
        else:
            raise ValueError ("El nombre debe ser un string") 

        

    




    # ========================
    #   MÉTODOS DE INSTANCIA
    # ========================

    def encender(self):
        """Cambia el estado del vehículo a encendido."""
        if self._encendido:
            print("El vehículo ya está encendido.")
        else:
            self._encendido = True
            print("Vehículo encendido.")

    def apagar(self):
        """Cambia el estado del vehículo a apagado."""
        if not self._encendido:
            print("El vehículo ya está apagado.")
        else:
            self._encendido = False
            print("Vehículo apagado.")

    # ========================
    #   MÉTODO ESTÁTICO
    # ========================

    @staticmethod
    def es_vehiculo_pesado(peso):
        """
        Determina si un vehículo se considera 'pesado'.
        No depende de ninguna instancia, por eso es estático.
        """
        return peso > 3500  # kg

    # ========================
    #   MÉTODO DE CLASE
    # ========================

    @classmethod
    def mostrar_total_vehiculos(cls):
        """
        Método de clase:
        Permite acceder o modificar atributos de clase.
        En este caso, muestra cuántos vehículos se han creado.
        """
        print(f"Actualmente existen {cls.total_vehiculos} vehículos registrados.")

    # ========================
    #   REPRESENTACIÓN DEL OBJETO
    # ========================

    def __str__(self):
        """
        Representación legible del objeto.
        Se ejecuta al usar print() o str() sobre una instancia.
        """
        estado = "Encendido" if self._encendido else "Apagado"
        return (f"[Vehículo] Marca: {self._marca} | Modelo: {self._modelo} | "
                f"Color: {self._color} | Velocidad Máxima: {self._velocidad_maxima} km/h | Estado: {estado}")
    

# ========================
#   BLOQUE DE PRUEBA (solo se ejecuta si el archivo se ejecuta directamente)
# ========================
if __name__ == "__main__":
    # Crear varios vehículos
    v1 = Vehiculo("Toyota", "Corolla", "Rojo", 180,"Diesel")
    v2 = Vehiculo("Mercedes", "Actros", "Blanco", 120, "Gasolina")


    # Usar getters y setters
    print(v1.get_marca(), "-", v1.get_color())
    v1.set_color("Negro")
    print("Nuevo color:", v1.get_color())

    v1.combustible = "Hibrido"
    print (v1.combustible)

    # Probar métodos de instancia
    v1.encender()
    print(v1)
    v1.apagar()

    # Método estático: comprobar si un vehículo es pesado
    print("¿El camión es pesado?", Vehiculo.es_vehiculo_pesado(8000))

    # Método de clase: mostrar cuántos vehículos se han creado
    Vehiculo.mostrar_total_vehiculos()

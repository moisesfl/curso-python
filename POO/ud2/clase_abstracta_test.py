from abc import ABC, abstractmethod

# 1. Definimos la clase abstracta (hereda de ABC)
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método normal: Todos los vehículos hacen esto igual
    def encender(self):
        print(f"El {self.marca} {self.modelo} ha encendido el motor.")

    # Método abstracto: Es obligatorio, pero cada hijo lo hace de forma diferente
    @abstractmethod
    def arreglar(self):
        pass


# 2. Creamos una clase hija concreta: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Implementación OBLIGATORIA del método abstracto
    def arreglar(self):
        print(f"🔧 Conectando la computadora de diagnóstico al coche {self.marca} {self.modelo}.")


# 3. Creamos otra clase hija concreta: Moto
class Moto(Vehiculo):
    # Hereda el constructor del padre automáticamente al no declarar un __init__ propio

    # Implementación OBLIGATORIA del método abstracto
    def arreglar(self):
        print(f"⚙️ Ajustando y engrasando la cadena de la moto {self.marca} {self.modelo}.")


##INTERFACES

import dis
from typing import Protocol, runtime_checkable

@runtime_checkable
class Repostable(Protocol):
    """
    Interfaz que define la capacidad de repostar.
    Cualquier clase que implemente 'repostar()' se considera Repostable.
    """
    def repostar(self, litros: float) -> None:
        print (f"Se han repostado {litros} l") 


# # Extensiones con la interfaz Repostable
# class CocheRepostable(Coche, Repostable):
#     def repostar(self, litros: float):
#         print(f"El coche {self._marca} ha repostado {litros} litros de gasolina.")

# class MotoRepostable(Moto, Repostable):
#     pass


# Esta función exige que el objeto cumpla con el protocolo 'Arrancable'
def iniciar_operacion(dispositivo: Repostable):
    if (isinstance(dispositivo, Repostable)):
        dispositivo.repostar()
    else:
        raise TypeError(f"Error: El objeto de tipo '{type(dispositivo).__name__}")
    


def pruebas():
    # Esto fallará con un TypeError porque Vehiculo es abstracta
    #mi_vehiculo = Vehiculo("Generic", "X") 
    mr = Moto("ddddddd", "sdf")
    iniciar_operacion(mr)
    #mr.repostar()

    # Creamos instancias de las clases hijas
    mi_coche = Coche("Toyota", "Corolla", 4)
    mi_moto = Moto("Yamaha", "MT-07")

    # Ambos pueden usar los métodos normales del padre
    mi_coche.encender()  # Imprime: El Toyota Corolla ha encendido el motor.
    mi_moto.encender()   # Imprime: La Yamaha MT-07 ha encendido el motor.

    # Cada uno ejecuta su propia versión especializada del método abstracto
    mi_coche.arreglar()  # Imprime: 🔧 Conectando la computadora de diagnóstico...
    mi_moto.arreglar()   # Imprime: ⚙️ Ajustando y engrasando la cadena...


    
if __name__ == "__main__":
    pruebas()   
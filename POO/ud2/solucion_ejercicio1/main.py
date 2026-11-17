from zoo import (
    Animal, Perro, Aguila, Serpiente,
    Sonoro, Alimentable, ZooUtils,
    PesoInvalido, EdadInvalida, AlimentacionInvalida
)


def mostrar_animal(animal: Animal) -> None:
    print("\n" + "=" * 50)
    print(animal)
    print(f"Tipo / raza: {animal.getTipo()}")
    animal.moverse()

    if isinstance(animal, Sonoro):
        animal.hacerSonido()

    if isinstance(animal, Alimentable):
        try:
            animal.alimentar(0.1)
        except AlimentacionInvalida as error:
            print(f"Error al alimentar: {error}")

    print(
        "Estado del peso:",
        ZooUtils.es_peso_saludable(animal.especie, animal.edad, animal.peso_kg)
    )


def main() -> None:
    animales = [
        Aguila("Fénix", 15.0, 5, "Imperial", 60.5),
        Perro("Calcetines", 20.3, 8, "Pastor Alemán"),
        Serpiente("Sisosa", 5.8, 3, "Culebra", False),
    ]

    # Nacimientos: cada clase crea un objeto de su propio tipo.
    animales.append(Aguila.parir("Águila recién nacida"))
    animales.append(Perro.parir("Perro recién nacido"))
    animales.append(Serpiente.parir("Serpiente recién nacida"))

    for animal in animales:
        mostrar_animal(animal)

    print("\nNúmero total de animales creados:", Animal.total_animales)

    # Ejemplos de validación y excepciones.
    print("\nPruebas de errores:")
    try:
        Perro("Inválido", -2, 3, "Desconocida")
    except PesoInvalido as error:
        print("Peso:", error)

    try:
        Perro("Inválido", 10, -1, "Desconocida")
    except EdadInvalida as error:
        print("Edad:", error)

    try:
        animales[0].alimentar(0)
    except AlimentacionInvalida as error:
        print("Alimentación:", error)


if __name__ == "__main__":
    main()

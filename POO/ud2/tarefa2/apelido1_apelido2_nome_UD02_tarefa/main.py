"""Demostración del sistema de domótica."""
from domotica import (
    Hub, Utils, DatoInvalido, Duplicado, NoEncontrado,
    SensorTemperatura, BombillaInteligente, CerraduraInteligente,
    Medible, Conmutable, Actualizable,
)


def main():
    print("=== DEMO DOMÓTICA — INICIO ===")
    hub = Hub()
    definiciones = [
        {"id": "S001", "tipo": "sensor", "nombre": "Sensor Cocina",
         "fabricante": "Acme", "celsius": 22.5},
        {"id": "B001", "tipo": "bombilla", "nombre": "Bombilla Salón",
         "fabricante": "Lumen", "brillo": 80},
        {"id": "C001", "tipo": "cerradura", "nombre": "Puerta Principal",
         "fabricante": "SafeCo"},
        {"id": "S002", "tipo": "sensor", "nombre": "Sensor Dormitorio",
         "fabricante": "Acme", "celsius": 19.3},
        {"id": "B002", "tipo": "bombilla", "nombre": "Bombilla Pasillo",
         "fabricante": "Lumen", "brillo": 50},
        {"id": "001", "tipo": "sensor", "nombre": "ID incorrecto",
         "fabricante": "Acme", "celsius": 20},
        {"id": "B001", "tipo": "bombilla", "nombre": "Bombilla duplicada",
         "fabricante": "Lumen", "brillo": 20},
    ]

    clases = {
        "sensor": lambda d: SensorTemperatura(
            d["id"], d["nombre"], d["fabricante"], d["celsius"]),
        "bombilla": lambda d: BombillaInteligente(
            d["id"], d["nombre"], d["fabricante"], d["brillo"]),
        "cerradura": lambda d: CerraduraInteligente(
            d["id"], d["nombre"], d["fabricante"], d.get("bloqueada", True)),
    }

    print("Creando Hub… OK")
    print("Validando e instanciando:")
    for datos in definiciones:
        id_disp = datos.get("id", "")
        if not Utils.validar_id(id_disp):
            print(f"* ERROR: id {id_disp!r} inválido → se omite")
            continue
        try:
            if datos["tipo"] not in clases:
                raise DatoInvalido(f"Tipo desconocido: {datos['tipo']}")
            dispositivo = clases[datos["tipo"]](datos)
            hub.registrar(dispositivo)
            print(f"* OK: {dispositivo}")
        except Duplicado as error:
            print(f"* ERROR: {error} → se omite")
        except DatoInvalido as error:
            print(f"* ERROR: {error} → se omite")
        except KeyError as error:
            print(f"* ERROR: falta el dato {error} → se omite")

    dispositivos = hub.listar()
    print(f"\nRegistro en Hub completado: {len(dispositivos)} dispositivos.")
    print("\nListado de dispositivos:")
    for d in dispositivos:
        print("*", d)

    print("\nCapacidades detectadas:")
    for d in dispositivos:
        capacidades = []
        if isinstance(d, Medible):
            capacidades.append("Medible")
        if isinstance(d, Conmutable):
            capacidades.append("Conmutable")
        if isinstance(d, Actualizable):
            capacidades.append("Actualizable")
        print(f"* {d.id} → {', '.join(capacidades) if capacidades else 'Ninguna'}")

    print("\nOperar todos (polimorfismo):")
    hub.operar_todos()

    print("\nAcciones específicas:")
    sensor = hub.obtener("S001")
    if isinstance(sensor, SensorTemperatura):
        sensor.calibrar(0.70)
        print(f"* Calibrar S001 con offset +0.70 → nueva lectura = {sensor.leer_valor():.2f} ºC")

    bombilla = hub.obtener("B001")
    if isinstance(bombilla, BombillaInteligente):
        previo = bombilla.brillo
        bombilla.brillo = 90
        print(f"* B001: brillo previo = {previo} → brillo nuevo = {bombilla.brillo}")
        bombilla.actualizar_firmware("1.2.3")
        print('* B001: actualizar_firmware("1.2.3") → OK')

    bombilla2 = hub.obtener("B002")
    try:
        bombilla2.actualizar_firmware("1.0")
    except DatoInvalido as error:
        print(f"* B002: actualizar_firmware(\"1.0\") → ERROR: {error}")

    cerradura = hub.obtener("C001")
    if isinstance(cerradura, CerraduraInteligente):
        print(f"* C001: estado → {'bloqueada' if cerradura.bloqueada else 'desbloqueada'}")
        cerradura.desbloquear()
        print("* C001: desbloquear() → OK")
        cerradura.bloquear()
        print("* C001: bloquear() → OK")

    print("\nEstadísticas por tipo:")
    for tipo, cantidad in hub.estadisticas().items():
        print(f"* {tipo}: {cantidad}")
    print(f"Total dispositivos: {len(dispositivos)}")

    print("\nResumen de capacidades:")
    print(f"* Medibles: {sum(isinstance(d, Medible) for d in dispositivos)}")
    print(f"* Conmutables: {sum(isinstance(d, Conmutable) for d in dispositivos)}")
    print(f"* Actualizables: {sum(isinstance(d, Actualizable) for d in dispositivos)}")

    print("\nPruebas de errores controlados:")
    try:
        hub.registrar(hub.obtener("B001"))
    except Duplicado as error:
        print(f"* Registrar de nuevo B001 → ERROR: {error}")
    print(f'* Validar id "A_01" → {Utils.validar_id("A_01")} (carácter "_" no permitido)')
    try:
        bombilla2.actualizar_firmware("v1.2.3")
    except DatoInvalido as error:
        print(f"* Actualizar firmware B002 a v1.2.3 → ERROR: {error}")
    try:
        hub.obtener("X999")
    except NoEncontrado as error:
        print(f"* Obtener X999 → ERROR: {error}")

    print("\n=== DEMO DOMÓTICA — FIN ===")


if __name__ == "__main__":
    main()

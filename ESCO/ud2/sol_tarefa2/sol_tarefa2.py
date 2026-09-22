# ============================================================
# EJERCICIO FINAL - UD02
# Gestión de acceso y evaluación de usuarios
# ============================================================

# ------------------------------------------------------------
# 1. DATOS DE PARTIDA
# ------------------------------------------------------------

usuario = {
    "nombre": "Ana",
    "edad": 17,
    "rol": "alumno",
    "nota": 6.5,
    "activo": True
}


# ------------------------------------------------------------
# 2. VALIDACIÓN GENERAL DEL USUARIO
#    Condicional simple: if
# ------------------------------------------------------------

if not usuario["activo"]:
    print("Usuario inactivo. Acceso denegado.")

else:

    # --------------------------------------------------------
    # 3. IDENTIFICACIÓN DEL TIPO DE USUARIO
    #    Estructura match - case
    # --------------------------------------------------------

    match usuario["rol"]:

        # ----------------------------------------------------
        # CASO 1: ALUMNO
        # ----------------------------------------------------

        case "alumno":

            print(f"Acceso como alumno: {usuario['nombre']}")

            # ------------------------------------------------
            # 4. VALIDACIÓN Y EVALUACIÓN DE LA NOTA
            #    Condicionales anidados
            # ------------------------------------------------

            nota = usuario["nota"]

            # Comprobamos primero si la nota es válida
            if 0 <= nota <= 10:

                # --------------------------------------------
                # Clasificación de la nota
                # if - elif - else
                # --------------------------------------------

                if nota < 5:
                    print("Suspenso")

                elif nota < 7:
                    print("Aprobado")

                elif nota < 9:
                    print("Notable")

                else:
                    print("Sobresaliente")

                # --------------------------------------------
                # Operador ternario
                # --------------------------------------------

                estado_academico = "Promociona" if nota >= 5 else "No promociona"

                print(f"Estado académico: {estado_academico}")

            else:

                # La nota está fuera del intervalo 0-10
                print("Nota no válida.")

            # ------------------------------------------------
            # 5. CONTROL DE EDAD
            #    Condicional anidado dentro del alumno
            # ------------------------------------------------

            if usuario["edad"] < 18:
                print("Alumno menor de edad.")

            else:
                print("Alumno mayor de edad.")


        # ----------------------------------------------------
        # CASO 2: PROFESOR
        # ----------------------------------------------------

        case "profesor":

            print("Acceso como profesor. No se requiere evaluación.")


        # ----------------------------------------------------
        # CASO 3: INVITADO
        # ----------------------------------------------------

        case "invitado":

            print("Acceso limitado como invitado.")


        # ----------------------------------------------------
        # CUALQUIER OTRO ROL
        # ----------------------------------------------------

        case _:

            print("Rol no reconocido.")
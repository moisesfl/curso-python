def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print(f"***************************\n"
              f"Se va a llamar a la función:"
              )
        c = funcion(a, b)
        print("Se ha llamadoa la función")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

print (suma(5,8))

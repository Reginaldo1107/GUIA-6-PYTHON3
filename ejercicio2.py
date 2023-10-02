#1. problema_imprimir_saludo (in nombre: String) {
#requiere: { True }
#asegura: {imprime “Hola < nombre >”por pantalla}
#}

def imprimir_saludo (nombre : str) ->None:
    print("HOLA " + nombre)


imprimir_saludo("NALDO")

#2. raiz cuadrada de(numero) : 
# que devuelva la raı́z cuadrada del número.

def raiz_cuadrada_de(numero : int) -> float:
    return math.sqrt(numero)


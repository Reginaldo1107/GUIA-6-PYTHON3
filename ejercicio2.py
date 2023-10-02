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

# 3. fahrenheit a celsius(temp far) : que convierta una 
# temperatura en grados Fahrenheit a grados Celcius.
#problema fahrenheit a celsius (in t: R) : R {
#requiere: { True }
#asegura: {res = ((t − 32) × 5)/9}
#}
def fahrenheit_a_celsius(temperatura : float ) -> float :
    return ((temperatura -32)*5 )/9
    
# 4. imprimir dos veces(estribillo) : que imprima dos veces el 
#estribillo de una canción. Nota: Analizar el comporta-
# miento del operador (*) con strings.

def imprimir_dos_veces(estribillo :str) -> None :
    estribillo = estribillo + ' '
    print(estribillo*2)

imprimir_dos_veces("HOLA")

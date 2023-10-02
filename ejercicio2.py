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

#5. problema es multiplo de (in n: Z, in m:Z) : Bool {
#requiere: {m ̸ = 0}
#asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m × k)}
#}

def es_multiplo_de(n :int ,m :int) ->bool:
    return (n % m == 0)


#7. cantidad de pizzas(comensales, min cant de porciones) 
#que devuelva la cantidad de pizzas que necesitamos para
#que cada comensal coma como mı́nimo min cant de porciones 
#porciones de pizza. Considere que cada pizza tiene 8
#porciones y que se preere que sobren porciones.

def cantidadDePizzas (comensales :int , min_cantidad_de_porciones : int) -> int :
    
    totalPizzas :int = comensales * min_cantidad_de_porciones 
    return math.ceil(totalPizzas/8)
    

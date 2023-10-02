##########################################
##EJERCICIO3

#1. alguno es 0(numero1, numero2) : dados dos números racionales, 
# decide si alguno de los dos es igual a 0.
def alguno_es_0(numero1 : int ,numero2 :int) -> bool :
    return (numero1 == 0 or numero2 == 0)


#2. ambos son 0(numero1, numero2) : dados dos números racionales, 
# decide si ambos son iguales a 0.
 
def ambos_son_0(numero1 : int ,numero2 :int) -> bool :
    return (numero1 == 0 and numero2 == 0)

#3. problema es nombre largo (in nombre: String) : Bool {
#requiere: { True }
#asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
#}

def esNombreLargo(nombre : str) -> bool :
    return len(nombre) >= 3 and len(nombre) <= 8

#es_bisiesto(año): que indica si un año tiene 366 dı́as. Recordar 
# que un año es bisiesto si es múltiplo de 400, o bien
#4. es múltiplo de 4 pero no de 100.

def es_bisiesto(numero :int) -> bool :
    return (numero % 400 == 0) or (numero % 4  == 0 and ((numero % 100 != 0)))


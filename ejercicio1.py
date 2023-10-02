#1. problema imprimir hola mundo () {
#requiere: { T rue }
#asegura: { imprime “¡Hola mundo!”por consola}
#}
def imprimirEjercicio()->None:
    print("hola mundo ")

#2. imprimir un verso() : que imprima un verso de una canción que vos elijas,
#respetando los saltos de lı́nea mediante el
#caracter ‘\n´.
def imprimir_un_verso() -> None :
    verso = "Hola\nComo\nestas"
    print(verso)
#3. raizDe2() : 
# que devuelva la raı́z cuadrada de 2 con 4
#  #decimales. Ver función round
def raizDe2() -> float :
    return round(math.sqrt(2),4)

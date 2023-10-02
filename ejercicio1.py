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


#4. factorial_de_dos()
#problema factorial 2 () : Z {
#requiere: { True }
#asegura: {res = 2!}
#}

def factorial_de_dos() -> int:
    return 2

#5. perimetro : que devuelva el perı́metro de la circunferencia de 
#radio 1. Utilizar la biblioteca math mediante el comando
#import math y la constante math.pi
#problema perimetro () : R {
#requiere: { True }
#asegura: {res = 2 × π }
#}
def perimetro () ->float:
    return round(2 * math.pi,4)

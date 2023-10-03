############################################################################
#EJERCICIO 6 :
#6.1 
#1. Escribir una funcion que imprima los numeros del 1 al 10.

def del_1_al_10() -> None :
    numero :int = 1
    while (numero <= 10):
        print(numero)
        numero +=1
        

#6.2. Escribir una funcion que imprima los numeros 
# pares entre el 10 y el 40.

def del_10_al_40() -> None :
    numero :int = 10
    while (numero <= 40):
        print(numero)
        numero +=2


# 6.3 Escribir una funcion que imprima la palabra “eco” 10 veces.

def imprimir_eco_10_veces() -> None :
    numero :int = 0
    while (numero <10):
        print("ECO")
        numero +=1


#6.4. Escribir una funcion de cuenta regresiva para lanzar un cohete. 
# Dicha funcion ira imprimiendo desde el numero que
#me pasan por parametro (que sera positivo) hasta el 1, y por 
# ultimo “Despegue”.

def lanzar_un_cohete(numero : int )-> None :
 
    while (numero >= 1):
        print(numero)
        numero -= 1
    print ("DESPEGUE")



#6.5. Hacer una funcion que monitoree un viaje en el tiempo. 
#Dicha funcion recibe dos parametros, “el año de partida” y
#“algun año de llegada”, siendo este ultimo parametro siempre mas chico que el primero. 
#El viaje se realizara de a saltos de un año y la funcion debe mostrar el
#texto: “Viajo un año al pasado, estamos en el año: <año>” cada vez que se
#realice un salto de año
def maquinaDelTiempo(añoActual :int , añoPasado : int ) -> None:
    while (añoActual >= añoPasado):
        print ("Viajo un año al pasado, estamos en el año: " + str(añoActual))
        añoActual-=1


#6.6. Implementar de nuevo la funcion de monitoreo de viaje en el tiempo, 
# pero desde el año de partida hasta lo mas cercano
#al 384 a.C., donde conoceremos a Aristoteles.
#  Y para que sea mas rapido el viaje, ¡vamos a viajar de a 20 años en cada
#salto!

def maquinaDelTiempo_con_Aristoteles(añoActual :int  ) -> None:
    while (añoActual >= -384):
        print ("Viajo un año al pasado, estamos en el año: " + str(añoActual))
        añoActual-=20



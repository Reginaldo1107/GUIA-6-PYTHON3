##################################################
#Ejercicio  7 

# 7.1).Escribir una funcion que imprima los numeros del 1 al 10.
def del_1_al_10 () -> None :
    for i in range (1 , 11 ,1):
        print (i)



#7.2). Escribir una funcion que imprima los numeros pares entre el 10 y el 40

def del_10_al_40() -> None :
    for i in range (10 , 41 ,2):
        print (i)
        
        
 # 7.3)Escribir una funcion que imprima la palabra “eco” 10 veces
def imprime_eco() -> None :
    for i in range (0 ,10,1):
        print("ECO")
        
        
# 7.4) . Escribir una funcion de cuenta regresiva para lanzar 
# un cohete. Dicha funcion ira imprimiendo desde el numero que
#me pasan por parametro (que sera positivo) hasta el 1, y por 
# ultimo “Despegue”       

def cuenta_regresiva (numero : int ) -> None :
    for i in range (numero, 0, (-1)):
        print(numero)
    print("Despegue")    
    
    
# 7.5 ) Hacer una funcion que monitoree un viaje en el tiempo.
# Dicha funcion recibe dos parametros, “el año de partida” y
#“algun año de llegada”, siendo este ultimo parametro siempre
# mas chico que el primero. El viaje se realizara de a saltos
#de un año y la funcion debe mostrar el texto: 
# “Viajo un año al pasado, estamos en el año: <año>” cada vez que se
#realice un salto de año

def cuenta_regresiva(año_partida : int , año_llegada : int ) -> None :
    for i in range (año_partida , (año_llegada - 1), (-1)):
        print("Viajo un año al pasado estamos en el año : " + str(i))
                

# 7.6 ) . Implementar de nuevo la funcion de monitoreo de viaje en el tiempo, 
# pero desde el año de partida hasta lo mas cercano
# al 384 a.C., donde conoceremos a Aristoteles. Y para que sea mas rapido el viaje, 
# ¡vamos a viajar de a 20 años en cada salto

def aristoteles(año_de_partida : int ) -> None :
    for i in range (año_de_partida, -385, (-20) ):
        print (i)



aristoteles (-364)


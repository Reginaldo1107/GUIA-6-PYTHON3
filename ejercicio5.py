###########################################################
#EJERCICIO 5 
#1. devolver el doble si es par(numero) que devuelve el doble del 
# numero en caso de ser par y el mismo numero en
#caso contrario.

def devolver_el_doble_si_es_par (numero : int ) -> int :
    if(numero % 2 == 0):
        return numero *2 
    else :
        return numero 

#5.2 
#2. devolver_valor_si_es_par_sino_el_que_sigue(numero).
#que devuelve el mismo numero si es par y sino el siguiente.
#Analizar distintas formas de implementacion 
#(usando un if-then-else, y 2 if), ¿todas funcionan?

def devolver_valor_si_es_par_sino_el_que_sigue1(numero: int) -> int :
    if(numero % 2 == 0):
        return numero 
    
    else :
        return numero + 1  
#################################


def devolver_valor_si_es_par_sino_el_que_sigue2(numero: int) -> int :
    if(numero % 2 == 0):
        return numero 
    
    if(numero % 2 != 0):
        return numero + 1
    
####################################################################
#5.3
#3. devolver el doble si es multiplo3 el triple si es multiplo9(numero).
#En otro caso devolver el numero original. Analizar distintas formas de implementacion 
#(usando un if-then-else, y 2 if, usando alguna opcion de operacion
#logica), ¿todas funcionan?.

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9( numero : int ) -> int :

    if(numero % 9 == 0) :
        return numero *3 
    elif (numero % 3 == 0) :
        return numero *2 
    else :
        return numero 
    
############################################################################
#5.4
#4. lindo nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 
#devolver una frase que diga “Tu nombre tiene muchas letras!” y sino, “Tu nombre 
#tiene menos de 5 caracteres”

def lindo_nombre(nombre : str )->None :
    if(len(nombre)>= 5):
        print ("Tu nombre tiene muchas letras! ")
    else :
        print ("Tu nombre tiene menos de 5 letras")

############################################################################
#5.5
#5. elRango(numero) que imprime por pantalla “Menor a 5” si el numero 
# es menor a 5, “Entre 10 y 20” si el numero esta en ese rango y “Mayor a 20”
#  si el numero es mayor a 20.

def elRango(numero : int )->None :
    if(numero < 5):
        print ("MENOR A 5 ")
    elif(numero >= 10 and numero <= 20) :
        print ("ENTRE 10 Y 20 ")
    elif (numero > 20):
        print ("MAYOR A 20 ")

############################################################################
#5.6

#En Argentina una persona del sexo femenino se jubila a los 60 años, 
# mientras que aquellas del sexo masculino se jubilan
#a los 65 años. Quienes son menores de 18 años se deben ir de 
# vacaciones junto al grupo que se jubila. Al resto de
#las personas se les ordena ir a trabajar. Implemente una funcion que, 
# dados los parametros de sexo (F o M) y edad,
#imprima la frase que corresponda segun el caso: “Anda de vacaciones” 
# o “Te toca trabajar”
def que_te_toca ( sexo : str , edad: int) ->None :
    if(sexo == "F" and edad >= 60 ) :
        print(" Anda de vacaciones ")
    elif(sexo == "M" and edad >= 65 ):
        print(" Anda de vacaciones ")
    elif (edad < 18 ):
        print(" Anda de vacaciones ")
    else :
        print("TE TOCA TRABAJAR")

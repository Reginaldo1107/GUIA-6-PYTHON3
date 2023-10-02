import math
#####################################
#EJERCICIO 4.1 CON IF

def peso_pino( metros :int) -> int :
    if( metros <= 3 ):
        return (metros*300)
    else:
        return ((metros -3)*200)+ (900)
    



##################################################
#EJERCICIO 4.1 SIN IF
def peso_pino1( metros :int) -> int :
    metrospesados  = min(3,metros)
    metroslibianos = max(0,(metros-3))
    return metrospesados*300 + metroslibianos*200    
    


########################################

#4.2
#Definir la funcion es peso util,recibe un peso en kg y 
#responde si un pino de ese peso le sirve a la fabrica.

#Los pinos se usan para llevarlos a una fabrica de muebles, 
#a la que le sirven arboles de entre 400 y 1000 kilos, un pino
#fuera de este rango no le sirve a la fabrica
def es_peso_util (peso : int) -> bool :

    return ((peso >= 400) and (peso <= 1000))

##print(es_peso_util (400))
##print(es_peso_util (1400))

#####################################################
#4.3
#Definir la funcion sirve pino, recibe la altura de un pino y 
#responde si un pino de ese peso le sirve a la f´abrica.
def sirve_pino (metros : int ) -> bool :

    cambioMetrosAPesos = peso_pino(metros)
    
    return es_peso_util (cambioMetrosAPesos)

print(sirve_pino(2))
print(sirve_pino(3))
print(sirve_pino(4))
print(sirve_pino (5))

###########################################################
#4.4
def sirve_pino_composicion(metros : int ) -> bool :

    cambioMetrosAPesos = peso_pino(metros)
    
    return es_peso_util(cambioMetrosAPesos)

print(sirve_pino_composicion(2))
print(sirve_pino_composicion(3))
print(sirve_pino_composicion(4))
print(sirve_pino_composicion(5))



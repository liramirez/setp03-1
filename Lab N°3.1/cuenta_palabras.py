
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 13-Mayo-2013
#Actividad : 2 - Cuenta palbras Lab N°3
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de librerias
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

import re   # Expresiones regulares
import sys  # Aumenta la profundidad de la recursion

sys.setrecursionlimit(10000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Cuenta cuantas palabras en total tiene un texto
def cuenta_palabras(dic):
    if ( len(dic) > 0 ):

        # popitem elimina el elemento del diccionario
        palabra, cantidad = dic.popitem()
        return( cuenta_palabras(dic) + int(cantidad) )
    else:
        return( 0 )

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#


def main():

    dic ={}

    texto = open('funes.txt','r',encoding='utf-8')

    contenido=texto.read().lower()
    texto.close()
    palabras_texto = re.split('[^a-záéíóúñü]*',contenido)  # Busco palabras


    #Suma la cantidad de veces que existen las palabras
    #si las palabra no esta en diccionario, las agrega a este
    for palabra in palabras_texto:
        if (palabra in dic):
            dic[palabra]=dic[palabra]+1
        else:
            dic[palabra]=1

    print("La cantidad total de palabras en el texto es :", cuenta_palabras(dic))

    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

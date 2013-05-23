
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 13-Mayo-2013
#Actividad : 1 - Triangulo de Pascal Lab N°3
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def tri_pascal(n): 

    # Base triangulo 
    if n == -1: 
        return [] 
    if n == 0:
        return[[1]] 

    # Cuerpo del triangulo (cuando n > 1) 
    triangulo_final = tri_pascal(n-1) 
    triangulo_base = [1]
    
    for i in range(1, n): 
        triangulo_base.append(triangulo_final[n-1][i-1] + triangulo_final[n-1][i]) 

    triangulo_base.append(1)
    triangulo_final.append(triangulo_base)
    return triangulo_final

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():

    while True:
        print("Triangulo de Pascal")
        n =input("Ingrese el grado del binomio : ")

        #Valida la entrada para que sea NUMERO o que sea NUMERO mayor o igual a '0'
        if ( not n.isnumeric() or int(n) < 0):
             print()
             print("Error, ",n," NO es valido ")
             print()
             print("----INGRESE NUMERO MAYOR O IGUAL A '0'----")
             print()
        else:
            triangulos = tri_pascal(int(n))
            i = 0

            #Impresion en pantalla 
            for fila in triangulos:
                print("n =",i,":",end="")
                i = i + 1
                for coef in fila:
                    print(coef," ",end="")
                print()
            break


    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

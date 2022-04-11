import redis

 
redis = redis.Redis(host ='localhost', port = '6379')

my_dict = []
print('Sirve Redis!')

while True:

    print("\n Ingrese el numero del menu que desee acceder \n")

    menuOpt = int(input(" 1 Agregar una palabra nueva \n 2 Editar la palabra que ya existe \n 3 Eliminar la palabra que ya existe \n 4 Ver el listado de palabras \n 5 Buscar el significado de la palabra \n 6 Salir \n"))

    if(menuOpt == 1):
        palabra = input("Digite la palabra: ")
        definicion = input("digite la definicion: ")

        
        my_dict.append(palabra)

        print("Palabra Guardada")

    elif(menuOpt == 2):
        edita_palabra = input('Que palabra desea editar: ')
        if(palabra == edita_palabra):
            my_dict[palabra] = edita_palabra
            print('palabra editara')
            ni = redis.get(my_dict)
  
  
        print(ni)



    elif(menuOpt == 3):
        
        palabra_borrada = input("Dijite la palabra que desea borrar: ")
        if(palabra_borrada == palabra):
            test = redis.delete(palabra_borrada)
            print("se borro")
        else:
            print("No existe la palabra")

    elif(menuOpt == 4):
        print(my_dict)
        

    elif(menuOpt == 5):
        palabra_significado  = input("Digite la palabra que desea saber su significado: ")
        if(palabra_significado == palabra):
            thi = redis.get(palabra)
            print(thi)


    elif(menuOpt == 6):
        break

    else:
        print("\n Por favor ingrese una opcion valida \n")
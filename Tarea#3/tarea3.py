from pymongo import MongoClient
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]

mycol = mydb["Datos Personales"]

while True:

    print("\n Ingrese el numero del menu que desee acceder \n")

    menuOpt = int(input(" 1 Agregar una palabra nueva \n 2 Editar la palabra que ya existe \n 3 Eliminar la palabra que ya existe \n 4 Ver el listado de palabras \n 5 Buscar el significado de la palabra \n 6 Salir \n"))

    if(menuOpt == 1):
        # obtenemos la palabra y su definicion
        
        
        palabra_agregada = input("Ingrese la nueva palabra:")
        significado = input("Introduzca el significado:")    

        document = {'Palabra agregada': palabra_agregada,'Significado' : significado}

        _id = mycol['Datos Personales'].insert(document)
        print(_id)


    elif(menuOpt == 2):
        

        inputPalabra = input("\n Ingrese la palabra que desea modificar \n")

        nueva_palabra = input("Ingrese nueva palabra: \n")

        test = mycol['Datos Personales'].update_one({"palabra agregada": inputPalabra},{"$set":{"palabra agregada": "ni idea"}})        
        print("se actualizo")
        break

    elif(menuOpt == 3):
        inputPalabra = input("\n Ingrese la palabra que desea eliminar \n")
        test = mycol['Datos Personales'].delete_one({"palabra eliminada": inputPalabra})
        print("la palabra se elimino")
        break


    elif(menuOpt == 4):
        for r in mycol['Datos Personales'].find({}):
         print (r)
        break
      


    elif(menuOpt == 5):
         inputPalabra = input("\n Ingrese la palabra que desea saber su significado \n")
         for r in inputPalabra:
             print(significado)
            


      
    elif(menuOpt == 6):
       break

    else:
       print("\n Por favor ingrese una opcion valida \n")
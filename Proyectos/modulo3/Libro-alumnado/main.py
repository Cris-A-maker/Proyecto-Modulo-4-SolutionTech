from datos import *
from funciones import * #aqui aseguramos que se traigan los bloques de codigo

def main():

    if not login(USUARIO, PASSWORD):#asegurandose de que quien entre este logeado
        return


    while True:
        menu()

        option = input("Ingrese la opcion: ") #aqui elegimos del menu preparado

        if option == "1": #con esta opcion llamamos a la funcion inscribir
            inscribir(cursos, inscripciones, alumnos)
        elif option == "2": #con esta opcion llamamos a la funcion resumen
            resumen(inscripciones, alumnos)
        elif option =="3": #con esta opcion finalmente cerramos el programa
            print("\nCerrando inscripciones.")
            break
        else: #preparado por si el usuario usa una opcion que no sea 1,2,3 o escriba una letra
            print("\nOpcion no válida...")
            continue

if __name__ == "__main__": #si se ejecuta como script solo ejecuta esto
    main()
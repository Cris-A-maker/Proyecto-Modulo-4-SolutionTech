def login(usuario_correcto, contraseña_correcta): #Inicio de sesion
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos: #revisa que aun te queden intentos
        usuario = input("\nUsuario: ")
        contraseña = input("\nContraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("\nAccesso consedido")
            return True
        

        intentos +=1
        print(f"\nUsuario y/o contraseña incorrecto. intento {intentos} de {max_intentos}")
    print("\nSe a superado el maximo de intentos. Credenciales bloqueadas")
    return False

def mostrar_cursos(cursos): #mostrando los cursos disponibles y los cupos que tienen
    for codigo,curso in cursos.items():
        nombre, cupos = curso
        print(f"\n{codigo}.-{nombre} |Cupos: {cupos}")

def inscribir(cursos, inscripciones, alumnos): #inscribiendo a los alumnos
    mostrar_cursos(cursos)
    asignatura = input("\nSeleccione un curso (0 para salir): ")#seleccionando el curso el cual el alumno se va a inscribir

    if asignatura == "0":
        return
    
    if not asignatura.isdecimal(): #aqui nos aseguramos de que solo se ingresen numeros
        print("\nSolo se permiten digitos")
    
    asignatura = int(asignatura)

    if asignatura not in cursos:
        print("Curso no encontrado")
        return
    
    nombre_curso, cupos = cursos[asignatura]

    if cupos == 0:
        print("\nNo quedan cupos disponibles")
        return
    
    nombre = input ("Ingrese el nombre del alumno: ").capitalize()
    inscripciones.append((nombre, nombre_curso)) #aqui se esta agregando al alumno y el curso en el cual esta
    alumnos.add(nombre)

    cursos[asignatura] = (nombre_curso, cupos - 1)

    print(f"\n{nombre} Inscrito correctamente en {nombre_curso}")

def resumen(inscripciones, alumnos): #preparamos la funcion para mostrar toda la informacion de las inscripciones
    if len(inscripciones) == 0:
        print("No existen inscripciones")
        return
    
    print(f"\nCantidad de inscripciones: {len(inscripciones)}")
    for alumno,curso in inscripciones:
        print(f"\n{alumno} - {curso}")

    print(f"\nCantidad de alumnos inscritos: {len(alumnos)}")
    for alumno in alumnos:
        print(f"{alumno}")
        
def menu(): #un simple menu para la navegacion del usuario
    print(
        """
        ######################
        INSCRIPCION DE CURSOS
        ######################
        1.-Inscribir Alumnos
        2.-Resumen de inscripciones
        3.-Salir
        """
        )
listaUsuarios = ["Elian", "Mesu"] # Para validar o registrar
listaContrasenias = ["pipo", "tero"]

listaTareas = ["Revisar correos","Planificar proyecto","Escribir informe","Reunión de equipo","Llamar a cliente"]
listaPrioridad = [1,2,3,4,5] # Mientras mas alta mas importante
listaTiempoEstimado = [30,45,60,90,120] # En minutos
listaUsuarioAsignado = ["Elian", "Mesu"] 

def menuLogin(listaUsuarios, listaContrasenias): # Validar usuario, Crear usuario o salir del sistema
    ingresoSistema = 2 # Creamos una flag para saber si el usuario ingresa o no al sistema
    
    print("=========Menu Login=========")
    print("ingrese el numero correspondiente a la accion que quiera realizar")
    print("Validar Usuario 1")
    print("Registrar Usuario 2")
    print("Salir del sistema 0")
    
    # Validacion de la opcion
    opcion = int(input("Ingrese la opcion que quiere elegir: "))
    while (opcion < 1 or opcion > 2) and opcion != 0:
        opcion = int(input("ERROR-Ingrese una opcion valida que quiera elegir: "))
    
    while opcion != 0:
        if opcion == 1:
            print("eligio opcion 1")
            # Ingresa a funcion Validar Usuario
            ingreso = validarUsuario(listaUsuarios, listaContrasenias)
            if ingreso == True:
                ingresoSistema = 1
                print("")
                print("BIENVENIDO, YA ESTA LOGEADO, MARCA 0(cero) PARA SEGUIR AL SIGUIENTE MENU")
            else:
                print("========ERROR - CREDENCIALES INVALIDAS=======")
            
        if opcion == 2:
            print("eligio opcion 2")
            # Ingresa a funcion Registrar Usuario
            registro = registrarUsuario(listaUsuarios, listaContrasenias)
            if registro == True:
                print("EL USUARIO QUE INTENTO INGRESAR YA EXISTE INTENTE CON OTRO NOMBRE DE USUARIO")
            else:
                print("========El usuario fue creado con exito========")
                
        print("")        
        print("=========Menu Login=========")
        print("ingrese el numero correspondiente a la accion que quiera realizar")
        print("Validar Usuario 1")
        print("Registrar Usuario 2")
        print("Salir del sistema 0")
        
        opcion = int(input("Ingrese la opcion que quiere elegir: "))
        while (opcion < 1 or opcion > 2) and opcion != 0:
            opcion = int(input("ERROR-Ingrese una opcion valida que quiera elegir: "))
    
    return ingresoSistema

def validarUsuario(listaUsuarios, listaContrasenias): #VALIDACION DE USUARIO
    validacion = False
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i] == usuario and listaContrasenias[i] == contrasenia:
            validacion = True
    
    return validacion

def registrarUsuario(listaUsuarios, listaContrasenias): #REGISTRO DE USUARIO
    registracion = False
    nuevoUsuario = input("Ingrese nuevo nombre de usuario: ")
    nuevaContrasenia = input("Ingrese su nueva contraseña: ")
    
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i] == nuevoUsuario:
            registracion = True
            
    if registracion == False:
        listaUsuarios.append(nuevoUsuario)
        listaContrasenias.append(nuevaContrasenia)
        print(listaUsuarios)
        print(listaContrasenias)
        
    return registracion
        
#=================Programa Principal=====================
usuario = menuLogin(listaUsuarios, listaContrasenias)

while usuario > 0 and usuario <= 2: # Selecciona segun el valor de usuario a donde tiene que ir
    if usuario == 1: # Ingresa al sistema
        print("===============Has ingresado al sistema=================")
    elif usuario == 2: # Intenta ingresar al sistema pero no ah iniciado sesion
        print("INICIE SESION CON SU USUARIO PARA INGRESAR")
        usuario = menuLogin(listaUsuarios, listaContrasenias)
    else: 
        usuario = menuLogin(listaUsuarios, listaContrasenias)




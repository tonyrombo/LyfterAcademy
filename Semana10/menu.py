import actions, data

def menuSelection():
    menuOption = int(input("Seleccione una opcion: \n1. Ingresar estudiante.\n2. Ver información de todos los estudiantes.\n3. Ver Top 3 de estudiantes.\n4. Ver la nota promedio entre todos los estudiantes.\n5. Exportar datos actuales a un CSV.\n6. Importar datos desde un CSV.\n"))
    
    if menuOption > 6 :
        menuOption = int(input("Debe elegir una opcion del menu, intente de nuevo"))
    
    match menuOption:
        case 1:
            actions.ingresarEstudiante()
        case 2:
            actions.informacionEstudiantes()
        case 3:
            actions.topTresEstudiantes()
        case 4:
            actions.promedioTotal()
        case 5:
            data.exportData()
        case 6:
            data.importData()

def menu():
    print('¡Bienvenido al sistema de gestion de estudiantes!')
    menuSelection()

    wantContinue = input("¿Desea realizar otra accion? Y/N: ").lower()
    if not wantContinue == "y" and not wantContinue == "n":
        wantContinue = input("Respuesta inválida, ¿desea realizar otra accion? Y/N: ")

    if wantContinue == "y":
        menuSelection()
    else: return None

menu()
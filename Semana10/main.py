def studentsGrades():
    menuOption = int(input("Seleccione una opcion: \n1. Ingresar estudiante.\n2. Ver información de todos los estudiantes.\n3. Ver Top 3 de estudiantes.\n4. Ver la nota promedio entre todos los estudiantes.\n5. Exportar datos actuales a un CSV.\n6. Importar datos desde un CSV.\n"))
    
    try:
        if menuOption > 6 :
            raise ValueError
        
        match menuOption:
            case 1:
                print(f"Se ha elegido la opción: {menuOption}")
    except:
        print("Debe elegir una opcion del menu, intente de nuevo")
studentsGrades()
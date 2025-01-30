import actions

class Menu:
    def __init__(self):
        print("¡Bienvenido al sistema de gestión de estudiantes!")
        self.actions = actions.Actions()

    def menu_selection(self):
        menu_option = int(input(
            "Seleccione una opcion: \n1. Ingresar estudiante.\n2. Ver información de todos los estudiantes.\n3. Ver Top 3 de estudiantes.\n4. Ver la nota promedio entre todos los estudiantes.\n5. Exportar datos actuales a un CSV.\n6. Importar datos desde un CSV.\n7. Salir del programa.\n"))
        
        if menu_option > 7 :
            menu_option = int(input("Debe elegir una opcion del menu, intente de nuevo"))
        
        match menu_option:
            case 1:
                self.actions.add_student()
            case 2:
                self.actions.show_students()
            case 3:
                self.actions.top_three_students()
            case 4:
                self.actions.total_average()
            case 5:
                self.actions.export_data()
            case 6:
                self.actions.import_data()
            case 7:
                print("Hasta pronto!")
                return False
        
        return True

    def run_handler(self):
        while True:
            result = self.menu_selection()
            if not result:
                break

            want_continue = input("\n¿Desea realizar otra acción? (Y/N): ")
            if want_continue.lower() != 'y':
                print("¡Hasta pronto!")
                break


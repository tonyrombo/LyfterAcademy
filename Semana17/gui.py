import FreeSimpleGUI as sg
from logic import show_errors, validate_transaction, validate_category

# Ventana para ingresar una nueva categoría
def show_add_category_window():
    layout = [
        [sg.Text("Nombre de la categoría:"), sg.Input(key="category")],
        [sg.Text('Debes agregar una categoria', key='category-name-error-text', visible=False, text_color="red")],
        [sg.Button("Agregar", key="ADD_CAT_BTN"), sg.Button("Cancelar")]
    ]
    
    window = sg.Window("Agregar Categoría", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"): #Se comprueba si se da click a Cancelar o se cierra la ventana con la X
            break
        if event == "ADD_CAT_BTN":
            error = validate_category(values["category"])
            window["category-name-error-text"].update(visible=error)

            if not error: #Si antes no hubo error, se cierra la ventana y se actualiza la categoria
                window.close()
                return values["category"]
            
    window.close()
    return None

# Ventana para ingresar un nuevo gasto o ingreso
def show_add_transaction_window(categories, transaction_type):
    layout = [
        [sg.Text("Título:"), sg.Input(key="transaction-title")],
        [sg.Text('Debes agregar un título', key='transaction-title-error-text', visible=False, text_color="red")],

        [sg.Text("Monto:"), sg.Input(key="amount")],
        [sg.Text('Debes agregar un monto válido', key='amount-error-text', visible=False, text_color="red")],

        [sg.Text("Categoría:"), sg.Combo(categories, key="category", readonly=True)], #El combo se usa para generar dropdowns y recibe un list para generar las opciones
        [sg.Text('Debes seleccionar una categoría', key='category-error-text', visible=False, text_color="red")],

        [sg.Button("Agregar", key="ADD_TRANS_BTN"), sg.Button("Cancelar")]
    ]

    window = sg.Window(f"Agregar {transaction_type}", layout, finalize=True)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "ADD_TRANS_BTN":
            errores = validate_transaction(values) #Funciones para validar input y mostrar errores si se dejan vacios o se pone un tipo de dato que no corresponde
            show_errors(window, errores)
            
            if not any(errores.values()): #Si no hay errores se cierra la ventana y retorna el dict con los valores ingresados.
                window.close()
                return {
                    "title": values["transaction-title"].strip(),
                    "amount": float(values["amount"]),
                    "category": values["category"],
                    "type": transaction_type
                }

    window.close()
    return None


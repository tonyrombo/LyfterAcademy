# main.py
import FreeSimpleGUI as sg
from logic import load_data, add_category, add_transaction
from gui import show_add_category_window, show_add_transaction_window

def main():
    data = load_data() #Se cargan los datos del archivo json para tenerlos disponibles en memoria

    layout = [
        [sg.Table(
            values=[[data_value["title"], data_value["amount"], data_value["category"], data_value["type"]] for data_value in data["transactions"]],
            headings=["Título", "Monto", "Categoría", "Tipo"],
            key="TABLE",
            auto_size_columns=False,
            justification="left",
            expand_x=True,
            expand_y=True
        )],
        [sg.Button("Agregar Categoría"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso"), sg.Button("Salir")]
    ]

    window = sg.Window("Gestor de Finanzas Personales", layout, size=(600, 400), resizable=True)

    while True:
        event, _ = window.read() #Se usa el guión bajo como manera de prescindir de la variable values ya que en esta parte no se le dio uso#

        if event == sg.WINDOW_CLOSED or event == "Salir":
            break

        elif event == "Agregar Categoría":
            nueva_categoria = show_add_category_window() #Se llama a la función con la ventana para agregar categoria y el dato devuelto se guarda en variable
            if nueva_categoria: #Si el proceso fue exitoso y hay una categoria nueva, se agrega a la lista que se usa para el dropdown
                add_category(data, nueva_categoria)

        elif event in ("Agregar Gasto", "Agregar Ingreso"): #Click a Agregar Gasto o Ingreso

            tipo = "Gasto" if event == "Agregar Gasto" else "Ingreso" #Se actualiza el tipo dependiendo del tipo de transaccion a ejecutar
            nueva_transaccion = show_add_transaction_window(data["categories"], tipo) #Se abre la ventana de agregar transaccion y lo devuelto se guarda en variable
            if nueva_transaccion: # Si el proceso fue exitoso, se agrega al json de datos
                add_transaction(data, nueva_transaccion)

        # Actualizar tabla con los nuevos datos
        window["TABLE"].update(values=[[data_value["title"], data_value["amount"], data_value["category"], data_value["type"]] for data_value in data["transactions"]])

    window.close()

if __name__ == "__main__":
    main()

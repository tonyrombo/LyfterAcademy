# logic.py
import FreeSimpleGUI as sg
import json
import os

DATA_FILE = "finanzas_data.json"

# Se cargan los datos si hay un archivo qu ya existe
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"categories": [], "transactions": []}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Guardar los datos en el archivo
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Agregar una categoría si no existe ya
def add_category(data, category):
    if category not in data["categories"]:
        data["categories"].append(category)
        save_data(data)

# Agregar un gasto o ingreso
def add_transaction(data, transaction):
    data["transactions"].append(transaction)
    save_data(data)

#Validar categoria y valores en la transaccion antes de agregarlas
def validate_category(category_name):
    return not category_name.strip()


def validate_transaction(transaction_values):
    errors = {
        "transaction-title-error": not transaction_values["transaction-title"].strip(), #Si no se le puede aplicar un metodo para string, hay error
        "amount-error": False,
        "category-error": not transaction_values["category"] #Si la categoria no existe, hay error
    }

    try:
        float(transaction_values["amount"]) #Si el monto no es un numero se devuelve error
    except:
        errors["amount-error"] = True

    return errors

#Mostrar errores
def show_errors(window, errors): #Se recorre el diccionario de errores por su key, value y se actualizan los valores segun lo retornado en las validaciones
    for item, show in errors.items():
        window[f"{item}-text"].update(visible=show) 
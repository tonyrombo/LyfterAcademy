import FreeSimpleGUI as sg
from logic import LogicManager

class AppGui:
    def __init__(self):
        self.manager = LogicManager()
    # Window to add a new category
    def show_add_category_window(self):
        layout = [
            [sg.Text("Name of the category:"), sg.Input(key="category")],
            [sg.Text('You need to add a category', key='category-name-error-text', visible=False, text_color="red")],
            [sg.Button("Add", key="ADD_CAT_BTN"), sg.Button("Cancel")]
        ]
        
        window = sg.Window("Add Category", layout)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"): #If Cancel button or X is clicked
                break
            if event == "ADD_CAT_BTN":
                error = self.manager.validate_category(values["category"])
                window["category-name-error-text"].update(visible=error)

                if not error: #If there is not error before, it closes the window and return the category value
                    window.close()
                    return values["category"]
                
        window.close()
        return None

    # Window to add a new Expense or Income
    def show_add_transaction_window(self, categories, transaction_type):
        layout = [
            [sg.Text("Title:"), sg.Input(key="transaction-title")],
            [sg.Text('You need to add a title', key='transaction-title-error-text', visible=False, text_color="red")],

            [sg.Text("Amount:"), sg.Input(key="amount")],
            [sg.Text('You need to add a valid amount', key='amount-error-text', visible=False, text_color="red")],

            [sg.Text("Category:"), sg.Combo(categories, key="category", readonly=True)], #Combo is used to generate dropdowns, receives a list as input value
            [sg.Text('Debes seleccionar una categoría', key='category-error-text', visible=False, text_color="red")],

            [sg.Button("Add", key="ADD_TRANS_BTN"), sg.Button("Cancel")]
        ]

        window = sg.Window(f"Add {transaction_type}", layout, finalize=True)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancel"):
                break

            if event == "ADD_TRANS_BTN":
                errors = self.manager.validate_transaction(values) #Inputs validation
                self.manager.show_errors(window, errors) #Show errors if existing
                
                if not any(errors.values()): #If there is not errors, it closes the window and return the new data for the transaction
                    window.close()
                    return {
                        "title": values["transaction-title"].strip(),
                        "amount": float(values["amount"]),
                        "category": values["category"],
                        "type": transaction_type
                    }

        window.close()
        return None


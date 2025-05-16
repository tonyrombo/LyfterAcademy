# logic.py
import FreeSimpleGUI as sg
import json
import os

DATA_FILE = "finance_data.json"
class LogicManager:
    def __init__(self, filepath=DATA_FILE):
        self.filepath = filepath
        self.data = self.load_data()

    # Loading data if there is an existing file
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return {"categories": [], "transactions": []}
        with open(self.filepath, "r") as file:
            return json.load(file)

    # Saving data into the file
    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    # Add a category if it does not exist
    def add_category(self, category):
        if category not in self.data["categories"]:
            self.data["categories"].append(category)
            self.save_data()

    # Add an expense or income
    def add_transaction(self, transaction):
        self.data["transactions"].append(transaction)
        self.save_data()

    #Validate category and values before adding
    @staticmethod
    def validate_category(category_name):
        return not category_name.strip()

    @staticmethod 
    def validate_transaction(transaction_values):
        errors = {
            "transaction-title-error": not transaction_values["transaction-title"].strip(), #If the string method is not possible, returns error
            "amount-error": False,
            "category-error": not transaction_values["category"] #If category exists
        }

        try:
            amount = float(transaction_values["amount"]) #If amount is not a number
            if amount <= 0: #If amount is negative, returns error
                errors["amount-error"] = True  # monto debe ser mayor a cero
        except:
            errors["amount-error"] = True

        return errors

    #Show errors
    def show_errors(self, window, errors): #Loops dictionary by key, value and updates values depending onvalidations
        for item, show in errors.items():
            window[f"{item}-text"].update(visible=show) 
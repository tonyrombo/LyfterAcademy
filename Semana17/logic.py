import FreeSimpleGUI as sg
import json
import os

DATA_FILE = "finance_data.json"

class Category:
    def __init__(self, name):
        self.name = name.strip()

    def is_valid(self):
        return bool(self.name)

    def to_str(self):
        return self.name

    def __eq__(self, other): #Python Object comparator
        if isinstance(other, Category): #Confirm if is instance of Category
            return self.name.lower() == other.name.lower()
        elif isinstance(other, str): #Confirm if is a string
            return self.name.lower() == other.strip().lower()
        return False
    
class Transaction:
    def __init__(self, title, amount, category, type):
        self.title = title.strip()
        self.amount = float(amount)
        self.category = category
        self.type = type

    def convert_to_dictionary(self): #Structure to use data as dictionary
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type
        }
    
    #Validate transaction
    @staticmethod
    def validate_transaction(values):
        errors = {
            "transaction-title-error": not values["transaction-title"].strip(), #If the string method is not possible, returns error
            "amount-error": False,
            "category-error": not values["category"] #If category exists
        }

        try:
            amount = float(values["amount"]) #If amount is not a number
            if amount <= 0: #If amount is negative, returns error
                errors["amount-error"] = True 
        except:
            errors["amount-error"] = True

        return errors

class LogicManager:
    def __init__(self, filepath=DATA_FILE):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self): # Loading data if there is an existing file
        if not os.path.exists(self.filepath):
            return {"categories": [], "transactions": []}
        with open(self.filepath, "r") as file:
            return json.load(file)

    def save_data(self): # Saving data into the file
        with open(self.filepath, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_category(self, category_obj: Category): # Add a category if it does not exist
        name = category_obj.to_str()
        if name and name not in self.data["categories"]:
            self.data["categories"].append(name)
            self.save_data()

    def add_transaction(self, transaction_obj: Transaction): # Add an expense or income
        self.data["transactions"].append(transaction_obj.convert_to_dictionary())
        self.save_data()

    #Validate category and values before adding
    @staticmethod
    def validate_category(name):
        return not name.strip()

    def show_errors(self, window, errors):
        for item, show in errors.items():
            window[f"{item}-text"].update(visible=show)
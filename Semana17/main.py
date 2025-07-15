import FreeSimpleGUI as sg
from logic import LogicManager, Category, Transaction
from gui import AppGui

def main():
    manager = LogicManager()
    gui = AppGui()

    data = manager.data #Data is loaded from json file to have it available on memory

    layout = [
        [sg.Table(
            values=[[t["title"], t["amount"], t["category"], t["type"]] for t in data["transactions"]],
            headings=["Title", "Amount", "Category", "Type"],
            key="TABLE",
            auto_size_columns=False,
            justification="left",
            expand_x=True,
            expand_y=True
        )],
        [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income"), sg.Button("Exit")]
    ]

    window = sg.Window("Personal Finance Manager", layout, size=(600, 400), resizable=True)

    while True:
        event, _ = window.read() #Underscore is used to dispense with Values variable as it is not being used here
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        elif event == "Add Category":
            new_category = gui.show_add_category_window() #Calling Add Category window and saving returned data in a variable
            if new_category: #If the process is successful it saves the new category in the list for the dropdown
                manager.add_category(new_category)

        elif event in ("Add Expense", "Add Income"): #Click to Add Expense or Income
            transaction_type = "Expense" if event == "Add Expense" else "Income" #The Type is updated depending on the event received
            new_transaction = gui.show_add_transaction_window(data["categories"], transaction_type) #Open Add Transaction window and saves the data in a variable
            if new_transaction: # If the process is sucessful it saves it to the data jason
                manager.add_transaction(new_transaction)

        # Update table with latest data
        window["TABLE"].update(
            values=[[t["title"], t["amount"], t["category"], t["type"]] for t in data["transactions"]]
        )

    window.close()

if __name__ == "__main__":
    main()

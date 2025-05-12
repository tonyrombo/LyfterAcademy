import unittest
import os
import json
from logic import (
    load_data,
    save_data,
    add_category,
    add_transaction,
    validate_category,
    validate_transaction
)

class TestLogic(unittest.TestCase):

    def setUp(self): #Funcion que se ejecuta antes de cada prueba
        # Se crea un archivo de prueba para no afectar los datos reales
        self.test_file = "finanzas_data.json"
        self.sample_data = {"categories": [], "transactions": []}
        save_data(self.sample_data)

    def tearDown(self): #Funcion que se ejecuta al final de las pruebas
        # Se limpia el archivo
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_data_creates_structure_if_file_not_found(self):
        # Arrange
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        # Act
        data = load_data()

        # Assert
        self.assertEqual(data, {"categories": [], "transactions": []})

    def test_save_and_load_data_consistency(self):
        # Arrange
        data = {"categories": ["Transporte"], "transactions": []}
        save_data(data)

        # Act
        loaded = load_data()

        # Assert
        self.assertEqual(loaded, data)

    def test_add_category_adds_only_if_not_duplicate(self):
        # Arrange
        data = load_data()
        add_category(data, "Comida")

        # Act
        data_after = load_data()
        add_category(data_after, "Comida")  # Intentamos agregar duplicado

        # Assert
        self.assertEqual(data_after["categories"].count("Comida"), 1) #Se comprueba que solo existe una categoria con el nombre

    def test_add_transaction_appends_transaction(self):
        # Arrange
        data = load_data()
        transaction = {"title": "Sueldo", "amount": 1000, "category": "Trabajo", "type": "Ingreso"}
        add_transaction(data, transaction)

        # Act
        updated_data = load_data()

        # Assert
        self.assertIn(transaction, updated_data["transactions"])

    def test_validar_categoria_detects_empty_name(self):
        self.assertTrue(validate_category(""))
        self.assertTrue(validate_category("   "))
        self.assertFalse(validate_category("Casa"))

    def test_validar_transaccion_returns_expected_errors(self):
        # Caso válido
        values = {"transaction-title": "Renta", "amount": "500", "category": "Casa"}
        errors = validate_transaction(values)
        self.assertFalse(any(errors.values()))

        # Caso con errores
        values2 = {"transaction-title": "", "amount": "abc", "category": ""}
        errors2 = validate_transaction(values2)
        self.assertTrue(errors2["transaction-title-error"])
        self.assertTrue(errors2["amount-error"])
        self.assertTrue(errors2["category-error"])

if __name__ == '__main__':
    unittest.main()
import unittest
import os
from logic import LogicManager, Transaction, Category

class TestLogicManager(unittest.TestCase):

    def setUp(self):#SetUp is used for being executed before the tests
        # A test file is created to not interfere in the existing app data
        self.test_file = "test_finance_data.json"
        self.manager = LogicManager(filepath=self.test_file)
        self.manager.data = {"categories": [], "transactions": []}
        self.manager.save_data()

    def tearDown(self):#TearDown is used for being executed at the end of the tests
        # Cleaning file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_data_creates_structure_if_file_not_found(self):
        # Arrange
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        manager = LogicManager(filepath=self.test_file)
        # Assert
        self.assertEqual(manager.data, {"categories": [], "transactions": []})

    def test_save_and_load_data_consistency(self):
        # Arrange
        self.manager.data = {"categories": ["Health"], "transactions": []}
        self.manager.save_data()
        # Act
        loaded_manager = LogicManager(filepath=self.test_file)
        # Assert
        self.assertEqual(loaded_manager.data, {"categories": ["Health"], "transactions": []})

    def test_add_category_adds_only_if_not_duplicate(self):
        # Arrange
        cat = Category("Food")
        # Act
        self.manager.add_category(cat)
        self.manager.add_category(cat)  # Try duplicates
        # Assert
        self.assertEqual(self.manager.data["categories"].count("Food"), 1)

    def test_add_transaction_appends_transaction(self):
        # Arrange
        transaction = Transaction("Salary", 1500, "Work", "Income")
        # Act
        self.manager.add_transaction(transaction)
        # Assert
        self.assertIn(transaction.convert_to_dictionary(), self.manager.data["transactions"])

    def test_validate_category_detects_empty_and_valid(self):
        # Assert
        self.assertTrue(LogicManager.validate_category(""))         # Empty
        self.assertTrue(LogicManager.validate_category("   "))      # Spaces
        self.assertFalse(LogicManager.validate_category("House"))   # Valid

    def test_validate_transaction_returns_expected_errors(self):
        # Valid Input
        valid = {
            "transaction-title": "Payment",
            "amount": "500",
            "category": "Services"
        }
        valid_result = Transaction.validate_transaction(valid)
        self.assertFalse(any(valid_result.values()))

        # Invalid input
        invalid = {
            "transaction-title": "",
            "amount": "abc",
            "category": ""
        }
        invalid_result = Transaction.validate_transaction(invalid)
        self.assertTrue(invalid_result["transaction-title-error"])
        self.assertTrue(invalid_result["amount-error"])
        self.assertTrue(invalid_result["category-error"])

        # Negative amount
        invalid_negative = {
            "transaction-title": "Pago",
            "amount": "-100",
            "category": "Otros"
        }
        result = Transaction.validate_transaction(invalid_negative)
        self.assertTrue(result["amount-error"])

        # Zero amount
        invalid_zero = {
            "transaction-title": "Pago",
            "amount": "0",
            "category": "Otros"
        }
        result = Transaction.validate_transaction(invalid_zero)
        self.assertTrue(result["amount-error"])

if __name__ == '__main__':
    unittest.main()

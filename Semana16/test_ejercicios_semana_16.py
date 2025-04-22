import unittest
from Semana15.ejercicios_semana_15 import bubble_sort
from Semana6.ejercicios_semana_6 import list_sum, reversed_string, get_upper_and_lower, words_order, is_prime, find_primes


class TestSemana16(unittest.TestCase):
    def test_bubble_sort_with_small_list(self):
        # Arrange
        my_list = [3, 1, 2]
        expected_result = [1, 2, 3]
        # Act
        result = bubble_sort(my_list)
        # Assert
        self.assertEqual(result, expected_result)

    def test_bubble_sort_with_big_list(self):
        # Arrange
        my_list = list(range(100, 0, -1))
        expected_result = list(range(1, 101))
        # Act
        result = bubble_sort(my_list)
        # Assert
        self.assertEqual(result, expected_result)

    def test_bubble_sort_with_empty_list(self):
        # Arrange
        my_list = []
        expected_result = []
        # Act
        result = bubble_sort(my_list)
        # Assert
        self.assertEqual(result, expected_result)

    def test_bubble_sort_with_invalid_input(self):
        # Arrange
        wrong_input = "no soy una lista"
        # Act & Assert
        with self.assertRaises(TypeError):
            bubble_sort(wrong_input)

    def test_list_with_no_numeric_elements(self):
        # Arrange
        my_list = [1, 2, "tres"]
        # Act & Assert
        with self.assertRaises(TypeError):
            bubble_sort(my_list)

    def test_list_sum_with_positive_numbers(self):
        # Arrange
        numbers = [4, 6, 2, 29]
        expected = 41
        # Act
        result = list_sum(numbers)
        # Assert
        self.assertEqual(result, expected)

    def test_list_sum_with_empty_list(self):
        # Arrange
        numbers = []
        expected = 0
        # Act
        result = list_sum(numbers)
        # Assert
        self.assertEqual(result, expected)

    def test_list_sum_with_negative_numbers(self):
        # Arrange
        numbers = [-1, -2, -3]
        expected = -6
        # Act
        result = list_sum(numbers)
        # Assert
        self.assertEqual(result, expected)

    def test_reversed_string(self):
        # Arrange
        text = "Hola Mundo"
        expected = "odnuM aloH"
        # Act
        result = reversed_string(text)
        # Assert
        self.assertEqual(result, expected)

    def test_get_upper_and_lower(self):
        # Arrange
        text = "I love Nación Sushi"
        expected = "There`s 3 upper cases and 13 lower cases"
        # Act
        result = get_upper_and_lower(text)
        # Assert
        self.assertEqual(result, expected)

    def test_get_upper_and_lower_with_empty_string(self):
        # Arrange
        text = ""
        expected = "There`s 0 upper cases and 0 lower cases"
        # Act
        result = get_upper_and_lower(text)
        # Assert
        self.assertEqual(result, expected)

    def test_words_order(self):
        # Arrange
        text = "python-variable-funcion-computadora-monitor"
        expected = "computadora-funcion-monitor-python-variable"
        # Act
        result = words_order(text)
        self.assertEqual(result, expected)

    def test_words_order_with_single_word(self):
        # Arrange
        text = "python"
        expected = "python"
        # Act
        result = words_order(text)
        # Assert
        self.assertEqual(result, expected)

    def test_find_primes(self):
        # Arrange
        numbers = [1, 4, 6, 7, 13, 9, 67]
        expected = [7, 13, 67]
        # Act
        result = find_primes(numbers)
        # Assert
        self.assertEqual(result, expected)

    def test_find_primes_with_no_primes(self):
        # Arrange
        numbers = [1, 4, 6, 8, 9, 10]
        expected = []
        # Act
        result = find_primes(numbers)
        # Assert
        self.assertEqual(result, expected)

    def test_find_primes_with_empty_list(self):
        # Arrange
        numbers = []
        expected = []
        # Act
        result = find_primes(numbers)
        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
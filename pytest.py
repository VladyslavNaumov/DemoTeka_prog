import unittest
import json
from block_vvod import ParameterEntry
from block_priem import DataComparator

class TestParameterEntry(unittest.TestCase):
    def test_save_to_json(self):
        # Створюємо об'єкт ParameterEntry
        parameter_entry = ParameterEntry()
        
        # Встановлюємо тестові дані
        test_data = {"param1": "test_value1", "param2": "test_value2", "param3": "test_value3"}
        for i, entry in enumerate(parameter_entry.entries):
            entry.setText(test_data[f"param{i + 1}"])
        
        # Викликаємо метод save_to_json
        parameter_entry.save_to_json()

        # Перевіряємо, чи створено файл і чи його вміст відповідає тестовим даним
        with open("data.json", "r") as json_file:
            saved_data = json.load(json_file)

        self.assertEqual(saved_data, test_data)

class TestDataComparator(unittest.TestCase):
    def test_process_data(self):
        # Створюємо об'єкт DataComparator
        data_comparator = DataComparator("data_tab_1.json", "matching_data_dictionary.json")

        # Запускаємо обробку даних
        data_comparator.process_data()

        # Перевіряємо, чи створено файл і чи його вміст має правильні ключі
        with open("matching_data_dictionary.json", "r") as json_file:
            matching_data = json.load(json_file)

        expected_result = {"param1": "test_value1", "param2": "test_value2", "param3": "test_value3"}
        self.assertEqual(matching_data, expected_result)

if __name__ == "__main__":
    unittest.main()
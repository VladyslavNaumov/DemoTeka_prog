import json

class ParameterEncoder:
    def __init__(self, parameters_ranges):
        self.parameters_ranges = parameters_ranges

    def encode_value(self, parameter, value):
        for code, range_or_value in self.parameters_ranges[parameter].items():
            if isinstance(range_or_value, range):
                if value in range_or_value:
                    return code
            else:
                if value == range_or_value:
                    return code
        return None

    def encode_parameters(self, parameters_data):
        encoded_parameters = {}
        for category, params in parameters_data.items():
            encoded_parameters[category] = {}
            for param, value in params.items():
                try:
                    value = int(value)
                except ValueError:
                    pass
                encoded_code = self.encode_value(param, value)
                if encoded_code is not None:
                    encoded_parameters[category][param] = encoded_code
                else:
                    encoded_parameters[category][param] = value
        return encoded_parameters

def load_parameters_from_json(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            parameters_data = json.load(file)
        return parameters_data
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except json.JSONDecodeError:
        print("Помилка розкодування JSON.")
        return None

def load_database(database_file_path):
    try:
        # Ваша логіка для завантаження даних з бази даних
        # Наприклад, можна використати SQLite:
        import sqlite3
        conn = sqlite3.connect(database_file_path)
        cursor = conn.cursor()
        # Виконати запит до бази даних і отримати результат
        # Наприклад:
        cursor.execute("SELECT * FROM your_table")
        data = cursor.fetchall()
        # Повернути отримані дані
        return data
    except Exception as e:
        print("Помилка завантаження бази даних:", e)
        return None

# Приклад використання
json_file_path = 'parameters.json'
input_parameters = load_parameters_from_json(json_file_path)

database_file_path = 'your_database.db'
database_data = load_database(database_file_path)

if input_parameters and database_data:
    print("Дані успішно завантажено.")
else:
    print("Не вдалося завантажити дані.")

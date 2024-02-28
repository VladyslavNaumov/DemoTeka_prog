import json

class ParameterEncoder:
    def __init__(self, parameters_ranges):
        self.parameters_ranges = parameters_ranges

    def encode_value(self, parameter, value):
        try:
            if parameter not in self.parameters_ranges:
                raise KeyError(f"Parameter '{parameter}' is not present in the parameter ranges dictionary.")
            for code, range_or_value in self.parameters_ranges[parameter].items():
                if isinstance(range_or_value, range):
                    if value in range_or_value:
                        return code
                else:
                    if value == range_or_value:
                        return code
        except Exception as e:
            print(f"Error encoding parameter '{parameter}': {e}")
        return None

    def encode_parameters(self, parameters_data):
        encoded_parameters = {}
        for category, params in parameters_data.items():
            encoded_parameters[category] = {}
            for param, value in params.items():
                try:
                    value = int(value) if value.strip() else None
                except ValueError:
                    pass
                encoded_code = self.encode_value(param, value)
                if encoded_code is not None:
                    encoded_parameters[category][param] = encoded_code
                else:
                    encoded_parameters[category][param] = value
        return encoded_parameters

# Assuming 'parameters.json' and 'parameters_ranges' are already loaded
# Initialize the object and encode parameters
parameters_ranges = {
    "Geometric Parameters":{
    "1.Number of Floors": {
        1: range(1, 3),
        2: range(3, 6),
        3: range(6, 10),
        4: range(10, 15),
        5: range(15, 25)  # для представлення "більше 15"
    },
    "2.Building Height": {
        1: range(1, 11),
        2: range(11, 16),
        3: range(16, 31),
        4: range(31, 61),
        5: range(61, 100)  # для представлення "більше 60"
    },
    # Для параметра "Форма будівлі" будемо використовувати список, оскільки це не числові значення
    "3.Building Shape": {
        1: "1)Rectangular",
        2: "2)Square",
        3: "3)Circular",
        4: "4)Complex"
    },
    "4.Building Footprint Area": {
    1: range(1, 101),
    2: range(300, 501),
    3: range(600, 1201),
    4: range(1300, 2001),
    5: range(2001, 999999)  # Використовуємо велике число для представлення "більше 2000"
},
    "5.Height to Crane Rail": {
    1: "1)немає(Цивільна)",
    2: "2)До 5м",
    3: "3)5-10м",
    4: "4)10-15м",
    5: "5)більше 15м" # Використовуємо велике число для представлення "более 15"
},
    "6.Span Width (Average)": {
    1: "Немає",
    2: range(1, 10),
    3: range(9, 16),
    4: range(18, 31),
    5: range(30, 42)
}
    },
    "Parameters by Types": {
        "7.Building Type":{
    1: "1)Residential",
    2: "2)Administrative",
    3: "3)Public",
    4: "4)Industrial",
    5: "5)Other"
    },
    "8.Structural Scheme":{
    1: "1)Frameless",
    2: "2)Framed",
    3: "3)Partial Frame"
    },
    "9.Building Solidity":{
    1: "1)I",
    2: "2)II",
    3: "3)III",
    4: "4)IV",
    5: "5)V-VI"
    },
    "10.Type of Flooring":{
    1: "1)Monolithic",
    2: "2)Assembled (ribbed)",
    3: "3)Assembled (hollow-core)",
    4: "4)Metal",
    5: "5)Composite"
     },
    "11.Material of Load-Bearing Structures": {
    1: "1)Concrete",
    2: "2)Reinforced concrete",
    3: "3)Metal",
    4: "4)Stone",
    5: "5)Composite"
},
    "12.Method of Manufacturing Reinforced Concrete Structures": {
    1: "1)Monolithic",
    2: "2)Prefabricated",
    3: "3)None"
},
    "13.Year of Construction": {
    1: range(1900, 1919),
    2: range(1920, 1949),
    3: range(1950, 1979),
    4: range(1980, 2000),
    5: range(2001, 2020)
},
    "14.Consequence Class":{
    1: "1)СС1",
    2: "2)СС2",
    3: "3)СС3",
},
},
    "Site`s Parameters": {
    "15.Soil Type of the Object's Foundation": {
    1: "1)Rocky",
    2: "2)Clayey",
    3: "3)Silty",
    4: "4)Sandy",
    5: "5)Sandy/Fill"
},
    "16.Need for Additional Ground Reinforcemen": {
    1: "1)Sheet Pile Driving",
    2: "2)Vibrosubmersion",
    3: "3)Reinforced Concrete Piles (Retaining Wall)",
    4: "4)None"
},
    "17.Distance from Power Transmission Lines": {
    1: "1)None",
    2: "2)1-5m",
    3: "3)5-15m",
    4: "4)15-40m"
},
    "18.Distance from Railroad Tracks": {
    1: "1)None",
    2: "2)1-2m",
    3: "3)3-5m",
    4: "4)5-10m"
},
    "19.Presence of Radiation Exposure Exceedance": {
    1: 1,
    2: 2
},
    "20.Requirement for Project Approval from Special Services": {
    1: "1)None",
    2: "2)Yes(Water Supply)",
    3: "3)Yes(Gas Service)",
    4: "4)Yes(Electrical Networks)",
    5: "5)Yes(Environmental)"
},
    "21.Use of Specialized Production Standards": {
    1: "1)Blast Furnace, Converter",
    2: "2)Gas, Coke",
    3: "3)Sheet Rolling / Pipe Rolling",
    4: "4)Ore Enrichment",
    5: "5)None"
},
"22.Need for Utility Relocation": {
    1: 1,
    2: 2
},
}
}
# Припускаємо, що файл parameters.json містить валідний JSON
with open('parameters.json', 'r', encoding='utf-8') as file:
    parameters_data = json.load(file)

# Ініціалізація об'єкту класу та кодування параметрів
encoder = ParameterEncoder(parameters_ranges)
encoded_parameters = encoder.encode_parameters(parameters_data)

# Виведення результату
#print(encoded_parameters)
print("Keys in parameters_data:", parameters_data.keys())

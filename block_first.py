import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QVBoxLayout, QComboBox, QCheckBox
    )
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Вкладка "Геометричні параметри"
class GeometricParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        validator = QRegExpValidator(QRegExp("[0-9.]*"))

        self.image_label = QLabel(self)
        pixmap = QPixmap('1Dementions_of_building.png')
        scaled_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignHCenter)  # Центрування зображення по горизонталі
        layout.addWidget(self.image_label, 0, 0, 1, 3)

        # Кількість поверхів
        layout.addWidget(QLabel("Number of Floors:"), 1, 0)
        self.floors_input = QLineEdit()
        self.floors_input.setValidator(validator)
        layout.addWidget(self.floors_input, 1, 1)
        layout.addWidget(QLabel("floors"), 1, 2)

        # Висота будівлі
        layout.addWidget(QLabel("Building Height:"), 2, 0)
        self.building_height_input = QLineEdit()
        self.building_height_input.setValidator(validator)
        layout.addWidget(self.building_height_input, 2, 1)
        layout.addWidget(QLabel("m"), 2, 2)

        # Форма будівлі
        layout.addWidget(QLabel("Building Shape:"), 3, 0)
        self.building_shape = QComboBox()
        self.building_shape.addItems(["1)Rectangular", "2)Square", "3)Circular", "4)Complex"])
        layout.addWidget(self.building_shape, 3, 1)

        # Площа забудови
        layout.addWidget(QLabel("Building Footprint Area:"), 4, 0)
        self.area_input = QLineEdit()
        self.area_input.setValidator(validator)
        layout.addWidget(self.area_input, 4, 1)
        layout.addWidget(QLabel("m2"), 4, 2)

        # Висота до підкранового шляху
        layout.addWidget(QLabel("Height to Crane Rail:"), 5, 0)
        self.crane_height = QComboBox()
        self.crane_height.addItems(["None (Civil)", "2)Up to 5m", "3)5-10m", "4)10-15m","5)Over 15m" ])
        layout.addWidget(self.crane_height, 5, 1)

        # Ширина прольоту (середня)
        layout.addWidget(QLabel("Span Width (Average):"), 6, 0)
        self.span_width_input = QLineEdit()
        self.span_width_input.setValidator(validator)
        layout.addWidget(self.span_width_input, 6, 1)
        layout.addWidget(QLabel("m"), 6, 2)

    def get_data(self):
        return {
            "1.Number of Floors": self.floors_input.text(),
            "2.Building Height": self.building_height_input.text(),
            "3.Building Shape": self.building_shape.currentText(),
            "4.Building Footprint Area": self.area_input.text(),
            "5.Height to Crane Rail": self.crane_height.currentText(),
            "6.Span Width (Average)": self.span_width_input.text()
        }

# Вкладка "Параметри по типам"
class TypeParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        validator = QRegExpValidator(QRegExp("[0-9.]*"))
        
        self.image_label = QLabel(self)
        pixmap2 = QPixmap('2.Type_of_building.png')
        scaled_pixmap2 = pixmap2.scaled(600, 400, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap2)
        self.image_label.setAlignment(Qt.AlignHCenter)  # Центрування зображення по горизонталі
        layout.addWidget(self.image_label, 0, 0, 1, 3)

        # Тип будівлі
        layout.addWidget(QLabel("Building Type:"), 1, 0)
        self.building_type = QComboBox()
        self.building_type.addItems(["1)Residential", "2)Administrative", "3)Public", "4)Industrial", "5)Other"])
        layout.addWidget(self.building_type, 1, 1)

        # Конструктивна схема
        layout.addWidget(QLabel("Structural Scheme"), 2, 0)
        self.structural_scheme = QComboBox()
        self.structural_scheme.addItems(["1)Frameless", "2)Framed", "3)Partial Frame"])
        layout.addWidget(self.structural_scheme, 2, 1)

        # Капітальність будівлі
        layout.addWidget(QLabel("Building Solidity"), 3, 0)
        self.capital_structure = QComboBox()
        self.capital_structure.addItems(["1)І", "2)ІІ", "3)ІІІ", "4)ІV", "5)V-VI"])
        layout.addWidget(self.capital_structure, 3, 1)

        # Тип перекриття
        layout.addWidget(QLabel("Type of Flooring"), 4, 0)
        self.ceiling_type = QComboBox()
        self.ceiling_type.addItems(["1)Monolithic", "2)Assembled (ribbed)", "3)Assembled (hollow-core)", "4)Metal", "5)Composite"])
        layout.addWidget(self.ceiling_type, 4, 1)

        # Матеріал несучих конструкцій
        layout.addWidget(QLabel("Material of Load-Bearing Structures"), 5, 0)
        self.load_bearing_material = QComboBox()
        self.load_bearing_material.addItems(["1)Concrete", "2)Reinforced concrete", "3)Metal", "4)Stone", "5)Composite"])
        layout.addWidget(self.load_bearing_material, 5, 1)

        # Метод виготовлення ЗБ конструкцій
        layout.addWidget(QLabel("Method of Manufacturing Reinforced Concrete Structures"), 6, 0)
        self.prep_rein_conc_str = QComboBox()
        self.prep_rein_conc_str.addItems(["1)Monolithic", "2)Prefabricated", "3)None"])
        layout.addWidget(self.prep_rein_conc_str, 6, 1)

        # Рік побудови
        layout.addWidget(QLabel("Year of Construction"), 7, 0)
        self.build_year_input = QLineEdit()
        self.build_year_input.setValidator(validator)
        layout.addWidget(self.build_year_input, 7, 1)
        layout.addWidget(QLabel("рік"), 7, 2)

        # Клас наслідків
        layout.addWidget(QLabel("Consequence Class:"), 8, 0)
        self.clas_nasl = QComboBox()
        self.clas_nasl.addItems(["1)СС1", "2)СС2", "3)СС3"])
        layout.addWidget(self.clas_nasl, 8, 1)

    def get_data(self):
        return {
            "7.Building Type": self.building_type.currentText(),
            "8.Structural Scheme": self.structural_scheme.currentText(),
            "9.Building Solidity": self.capital_structure.currentText(),
            "10.Type of Flooring": self.ceiling_type.currentText(),
            "11.Material of Load-Bearing Structures": self.load_bearing_material.currentText(),
            "12.Method of Manufacturing Reinforced Concrete Structures": self.prep_rein_conc_str.currentText(),
            "13.Year of Construction": self.build_year_input.text(),
            "14.Consequence Class":self.clas_nasl.currentText()
        }
# Вкладка "Параметри майданчика"
class SiteParametersTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        
        self.image_label = QLabel(self)
        pixmap3 = QPixmap('3_Building site.png')
        scaled_pixmap3 = pixmap3.scaled(600, 400, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap3)
        self.image_label.setAlignment(Qt.AlignHCenter)  # Центрування зображення по горизонталі
        layout.addWidget(self.image_label, 0, 0, 1, 3)
        

        # Грунти на яких побудований об'єкт
        layout.addWidget(QLabel("Soil Type of the Object's Foundation:"), 1, 0)
        self.soil_type = QComboBox()
        self.soil_type.addItems(["1)Rocky", "2)Clayey", "3)Silty", "4)Sandy", "5)Sandy/Fill"])
        layout.addWidget(self.soil_type, 1, 1)

        # Необхідність додаткового закріплення грунту
        layout.addWidget(QLabel("Need for Additional Ground Reinforcemen:"), 2, 0)
        self.additional_soil_reinforcement = QComboBox()
        self.additional_soil_reinforcement.addItems(["1)Sheet Pile Driving", "2)Vibrosubmersion", "3)Reinforced Concrete Piles (Retaining Wall)","4)None"])
        layout.addWidget(self.additional_soil_reinforcement, 2, 1)

        # Відстань від дротів ЛЕП
        layout.addWidget(QLabel("Distance from Power Transmission Lines:"), 3, 0)
        self.distance_from_power_lines = QComboBox()
        self.distance_from_power_lines.addItems(["1)None", "2)1-5m", "3)5-15m","4)15-40m"])
        layout.addWidget(self.distance_from_power_lines, 3, 1)

        # Відстань від залізничних рельсів
        layout.addWidget(QLabel("Distance from Railroad Tracks:"), 4, 0)
        self.distance_from_railway = QLineEdit()
        self.distance_from_railway = QComboBox()
        self.distance_from_railway.addItems(["1)None", "2)1-2m", "3)3-5m","4)5-10m"])
        layout.addWidget(self.distance_from_railway, 4, 1)

        # Наявність перевищення норм радіації
        layout.addWidget(QLabel("Presence of Radiation Exposure Exceedance:"), 5, 0)
        self.radiation_norm_exceeded = QCheckBox("Yes!")
        layout.addWidget(self.radiation_norm_exceeded, 5, 1)

        # Необхідність погодження проекту зі спец. службами
        layout.addWidget(QLabel("Requirement for Project Approval from Special Services:"), 6, 0)
        self.special_services_approval = QComboBox()
        self.special_services_approval.addItems(["1)None", "2)Yes(Water Supply)", "3)Yes(Gas Service)","4)Yes(Electrical Networks)","5)Yes(Environmental)"])
        layout.addWidget(self.special_services_approval, 6, 1)

        # Використання спеціалізованих норм на виробництві
        layout.addWidget(QLabel("Use of Specialized Production Standards:"), 7, 0)
        self.specialized_standards_usage = QComboBox()
        self.specialized_standards_usage.addItems(["1)Blast Furnace, Converter", "2)Gas, Coke", "3)Sheet Rolling / Pipe Rolling", "4)Ore Enrichment","5)None"])
        layout.addWidget(self.specialized_standards_usage, 7, 1)

        # Необхідність перенесення комунікацій
        layout.addWidget(QLabel("Need for Utility Relocation:"), 8, 0)
        self.communication_relocation_need = QCheckBox("Yes!")
        layout.addWidget(self.communication_relocation_need, 8, 1)

    def get_data(self):
        return {
            "15.Soil Type of the Object's Foundation": self.soil_type.currentText(),
            "16.Need for Additional Ground Reinforcemen": self.additional_soil_reinforcement.currentText(),
            "17.Distance from Power Transmission Lines": self.distance_from_power_lines.currentText(),
            "18.Distance from Railroad Tracks": self.distance_from_railway.currentText(),
            "19.Presence of Radiation Exposure Exceedance": self.radiation_norm_exceeded.isChecked(),
            "20.Requirement for Project Approval from Special Services": self.special_services_approval.currentText(),
            "21.Use of Specialized Production Standards": self.specialized_standards_usage.currentText(),
            "22.Need for Utility Relocation": self.communication_relocation_need.isChecked()
        }

# Головне вікно програми
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DemoTeka")
        self.setWindowIcon(QIcon('Logo_prog.PNG'))
        self.resize(800, 600)
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Додаємо вкладки
        self.tab_widget.addTab(GeometricParametersTab(), "Geometric Parameters")
        self.tab_widget.addTab(TypeParametersTab(), "Parameters by Types")
        self.tab_widget.addTab(SiteParametersTab(), "Site`s Parameters")

        # Кнопка збереження
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        main_layout.addWidget(self.save_button)

    def save_data(self):
        data = {
            "Geometric Parameters": self.tab_widget.widget(0).get_data(),
            "Parameters by Types": self.tab_widget.widget(1).get_data(),
            "Site`s Parameters": self.tab_widget.widget(2).get_data()
        }

        with open("parameters.json", "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Дані збережено у файлі 'parameters.json'")

# Створення та запуск програми
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
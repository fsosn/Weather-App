from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QTextEdit,
    QCompleter,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from viewmodel import ViewModel
import forecast_options
import cities


class View(QMainWindow):
    def __init__(self, view_model: ViewModel):
        super().__init__()
        self.view_model = view_model
        self.initUI()
        self.view_model.data_updated.connect(self.update_weather_info)

    def initUI(self):
        self.setWindowTitle("Weather Forecast App")
        self.setWindowIcon(QIcon("images/app_icon.png"))
        self.resize(600, 400)

        main_frame = QFrame()
        main_layout = QVBoxLayout()
        main_frame.setLayout(main_layout)

        city_container = QHBoxLayout()
        city_label = QLabel("Enter the city:")
        self.city_entry = QLineEdit()
        city_container.addWidget(city_label)
        city_container.addWidget(self.city_entry)

        main_layout.addLayout(city_container)

        city_names = cities.load_city_names()
        completer = QCompleter(city_names, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.city_entry.setCompleter(completer)

        button_container = QHBoxLayout()
        buttons = [
            ("Current conditions", forecast_options.CURRENT_CONDITIONS),
            ("12 hours", forecast_options.HOURLY_FORECAST),
            ("Tomorrow", forecast_options.ONE_DAY_FORECAST),
            ("5-day", forecast_options.FIVE_DAY_FORECAST),
        ]
        for text, forecast_option in buttons:
            button = QPushButton(text)
            button.clicked.connect(
                lambda _, option=forecast_option: self.fetch_conditions(option)
            )
            button_container.addWidget(button)

        main_layout.addLayout(button_container)

        self.weather_display = QTextEdit()
        self.weather_display.setReadOnly(True)
        main_layout.addWidget(self.weather_display)

        self.setCentralWidget(main_frame)

    def fetch_conditions(self, forecast_type):
        city = self.city_entry.text()
        try:
            self.view_model.fetch_weather_conditions(city, forecast_type)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")

    def update_weather_info(self, weather_info):
        self.weather_display.setPlainText(weather_info)

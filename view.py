from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QTextEdit,
)
from PyQt5.QtGui import QIcon
from viewmodel import ViewModel
import forecast_options


class View(QMainWindow):
    def __init__(self, view_model: ViewModel):
        super().__init__()
        self.view_model = view_model
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather Forecast App")
        self.setWindowIcon(QIcon("images/app_icon.png"))

        self.resize(600, 400)

        left_frame = QFrame()
        left_layout = QVBoxLayout()
        left_frame.setLayout(left_layout)

        city_label = QLabel("Enter the city:")
        self.city_entry = QLineEdit()
        left_layout.addWidget(city_label)
        left_layout.addWidget(self.city_entry)

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
            left_layout.addWidget(button)

        left_layout.addStretch()

        right_frame = QFrame()
        right_layout = QVBoxLayout()
        right_frame.setLayout(right_layout)

        weather_display_label = QLabel("Weather Information:")
        self.weather_display = QTextEdit()
        self.weather_display.setReadOnly(True)

        right_layout.addWidget(weather_display_label)
        right_layout.addWidget(self.weather_display)

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def fetch_conditions(self, forecast_type):
        city = self.city_entry.text()
        weather_info = self.view_model.fetch_weather_conditions(city, forecast_type)
        self.update_weather_info(weather_info)

    def update_weather_info(self, weather_info):
        self.weather_display.setPlainText(weather_info)

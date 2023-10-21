import sys
from PyQt5.QtWidgets import QApplication
from view import View

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
        print("Usage: python main.py api_key")
        sys.exit(1)

    api_key = sys.argv[1]

    app = QApplication(sys.argv)
    weather_app = View(api_key)
    weather_app.show()
    sys.exit(app.exec_())

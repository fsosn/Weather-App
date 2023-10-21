import sys
from PyQt5.QtWidgets import QApplication
from view import View
from model import Model
from viewmodel import ViewModel

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
        print("Usage: python main.py api_key")
        sys.exit(1)

    api_key = sys.argv[1]

    app = QApplication(sys.argv)
    model = Model(api_key)
    view_model = ViewModel(model)
    view = View(view_model)
    view.show()

    sys.exit(app.exec_())

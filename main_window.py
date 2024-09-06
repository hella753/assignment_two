import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app import login_page
from app import app_page
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget() # Stacked Widget შექმნა
        self.setMinimumSize(800, 600) # ფანჯრის ზომა
        self.setWindowTitle("Currency Converter App")
        self.setWindowIcon(QIcon(self.resource_path("image/app_logo.ico"))) # წყარო: https://www.flaticon.com/free-icon/country-currencies_65714
        self.setStyleSheet("background-color: #7C93C3") # უკანა ფონი
        self.setCentralWidget(self.stacked_widget) # ცენტრალურ ვიჯეტად ვაყენებთ სტეკს
        self.login_page = login_page.LoginPage(self) # ვქმნით გვერდების ინსტანციებს, გადავცემთ ამ ფანჯარას რომ წვდომა ქონდეს მის მეთოდებზე
        self.app_page = app_page.App(self)
        self.stacked_widget.addWidget(self.login_page) # ვამატებთ სტეკში ამ ფეიჯებს
        self.stacked_widget.addWidget(self.app_page)
        self.stacked_widget.setCurrentWidget(self.login_page) # ავტორიზაციის ფეიჯს ვსვამთ დეფოლტად სტეკში
    def switch_to_app(self):
        self.stacked_widget.setCurrentWidget(self.app_page) #ფუნქციები ფეიჯების გადასართავად
    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_page)

    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
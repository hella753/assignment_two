import os.path
import sys

from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QComboBox, QPushButton
from PyQt5 import uic

class App(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        uic.loadUi(self.resource_path('ui/loaduiapp.ui'), self) # აპის ui ვაიმპორტებთ
        self.from_value_input = self.findChild(QLineEdit, 'from_value_input') # ელემენტების ინიციალიზაცია
        self.result_label = self.findChild(QLabel, 'result_label')
        self.from_curr_combobox = self.findChild(QComboBox, 'from_curr_combobox')
        self.to_curr_combobox = self.findChild(QComboBox, 'to_curr_combobox')
        self.convert_button = self.findChild(QPushButton, 'convert_button')
        self.clear_button = self.findChild(QPushButton, 'clear_button')
        self.logout_button = self.findChild(QPushButton, 'logout_button')

        self.currency_list = ["USD", "GEL", "EUR", "GBP"]
        self.currency_dict = {
            "GEL_TO_USD": 0.3717, "GEL_TO_EUR": 0.3359, "GEL_TO_GBP": 0.2827, "USD_TO_GBP": 0.7624,
            "USD_TO_EUR": 0.9062, "USD_TO_GEL": 2.6900, "EUR_TO_GBP": 0.8414, "EUR_TO_GEL": 2.9775,
            "EUR_TO_USD": 1.1036, "GBP_TO_USD": 1.3116, "GBP_TO_EUR": 1.1885, "GBP_TO_GEL": 3.5383
        } # წინა დავალების დაჰარდკოდებული მონაცემები

        self.init_ui()

    def init_ui(self):
        self.from_curr_combobox.setCurrentIndex(-1) # კომბობოქსის მნიშვნელობა წაიშალოს
        self.to_curr_combobox.setCurrentIndex(-1)
        self.convert_button.clicked.connect(self.convert_button_clicked) # ღილაკების ფუნქციები
        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.logout_button.clicked.connect(self.logout_button_clicked)

    def convert_button_clicked(self):
        # კონვერტაცია წინა დავალების ლოგიკით
        value_to_convert = float(self.from_value_input.text())
        get_curr = self.from_curr_combobox.currentText()
        to_curr = self.to_curr_combobox.currentText()
        if get_curr != to_curr and get_curr in self.currency_list and to_curr in self.currency_list:
            converted_value = self.currency_dict[f'{get_curr}_TO_{to_curr}'] * value_to_convert
            self.result_label.setText(f"{converted_value:.2f}")
        else:
            self.result_label.setText('აირჩიეთ ვალუტა')

    def clear_button_clicked(self):
        # საწყისი მდგომარეობის დაბრუნება
        self.from_curr_combobox.setCurrentIndex(-1)
        self.to_curr_combobox.setCurrentIndex(-1)
        self.from_value_input.clear()
        self.result_label.setText("შედეგი")

    def logout_button_clicked(self):
        # დაბრუნება ავტორიზაციის გვერდზე
        self.main_window.switch_to_login()
        self.clear_button_clicked()

    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)




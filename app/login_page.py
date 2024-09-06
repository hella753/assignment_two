from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic

class LoginPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        uic.loadUi('../ui/loaduiauth.ui', self) # ავტორიზაციის ui-ს ვტვირთავთ
        self.user = "admin" # ეს იქნება იუზერი და პაროლი
        self.password = "admin"
        self.user_input = self.findChild(QLineEdit, 'user_input') # ელემენტების ინიციალიზაცია
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.login_button = self.findChild(QPushButton, 'login_button')

        self.init_ui()

    def init_ui(self):
        self.user_input.returnPressed.connect(lambda: self.login()) # როცა იუზერზე ან პაროლის ინფუთზე ვიდგებით
        # ენთერითაც რომ დალოგინდეს
        self.password_input.setEchoMode(QLineEdit.Password) # პაროლი რომ არ იყოს ტექსტური ტიპის
        self.password_input.returnPressed.connect(lambda: self.login())
        self.login_button.clicked.connect(self.login)

    def login(self):
        if self.user_input.text() == self.user and self.password_input.text() == self.password:
            # ვალიდაცია
            self.main_window.switch_to_app()
            self.user_input.clear()
            self.password_input.clear() # გავწმინდოთ ინფუთები
        else:
            self.show_error_message() # გამოიტანოს შეცდომის მესიჯბოქსი
            self.user_input.clear()
            self.password_input.clear()

    @staticmethod
    def show_error_message():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("შეცდომა!")
        msg_box.setInformativeText("მომხმარებლის სახელი ან პაროლი არასწორია. თავიდან სცადეთ.")
        msg_box.setWindowTitle("შეცდომა")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()


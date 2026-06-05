import os

from PySide6.QtWidgets import QWidget
from ui.ui_settings import Ui_Settings
import wk_api as wk
import json

class SettingsWindow(QWidget, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Buttons
        self.btn_test.clicked.connect(self.test_api)
        self.btn_save.clicked.connect(self.save_settings)
        self.btn_quit.clicked.connect(self.quit_settings)

        # Start function on start
        self.check_config()
        self.test_api()

    def check_config(self):
        if os.path.exists("config.json"):
            with open ("config.json", "r") as file:
                data = json.load(file)

            if str(data["wk_api_key"]) == "":
                self.text_api.setText("Enter WaniKani API key")
            else:
                self.text_api.setText(f"{data["wk_api_key"]}")
        else:
            self.text_api.setText("Enter WaniKani API key")

    def test_api(self):
        self.save_settings()
        wk.get_headers()
        try:
            user_level = wk.get_user_level()
            self.label_info.setText(f"API key is valid. Your user level is {user_level}.")
        except Exception as e:
            self.label_info.setText(f"Error {e}.")

    def save_settings(self):
        with open("config.json", "w") as file:
            file.write(f'{{"wk_api_key": "{self.text_api.text()}"}}')

        self.label_info.setText(f"Settings saved.")

    def quit_settings(self):
        self.close()
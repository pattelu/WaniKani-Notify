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

    def check_config(self):
        if os.path.exists("config.json"):
            with open ("config.json", "r") as file:
                data = json.load(file)

            if str(data["wk_api_key"]) == "":
                self.text_api.setText("Enter WaniKani API key")
            else:
                self.text_api.setText(f"{data["wk_api_key"]}")

            self.check_user_level.setChecked(data["only_user_level"])
            self.combo_srs.setCurrentIndex(data["max_srs"] - 1)

            self.check_l_radicals.setChecked(data["lessons"]["radical"])
            self.check_l_kanji.setChecked(data["lessons"]["kanji"])
            self.check_l_vocabulary.setChecked(data["lessons"]["vocabulary"])

            self.check_r_radicals.setChecked(data["reviews"]["radical"])
            self.check_r_kanji.setChecked(data["reviews"]["kanji"])
            self.check_r_vocabulary.setChecked(data["reviews"]["vocabulary"])

        else:
            self.text_api.setText("Enter WaniKani API key")

    def test_api(self):
        self.save_settings()
        wk.get_headers()
        try:
            user_level = wk.get_user_level()
            self.label_test_api.setText(f"Your user level is {user_level}. API key is valid. ")
        except Exception as e:
            self.label_test_api.setText(f"Error {e}.")

    def save_settings(self):
        configuration = {
            "wk_api_key": f'{self.text_api.text()}',
            "only_user_level": self.check_user_level.isChecked(),
            "max_srs": (self.combo_srs.currentIndex() + 1),
            "lessons": {
                "radical": self.check_l_radicals.isChecked(),
                "kanji": self.check_l_kanji.isChecked(),
                "vocabulary": self.check_l_vocabulary.isChecked(),
                "kana_vocabulary": self.check_l_vocabulary.isChecked()
            },
            "reviews": {
                "radical": self.check_r_radicals.isChecked(),
                "kanji": self.check_r_kanji.isChecked(),
                "vocabulary": self.check_r_vocabulary.isChecked(),
                "kana_vocabulary": self.check_r_vocabulary.isChecked()
            }
        }

        with open("config.json", "w") as file:
            json.dump(configuration, file, indent=4)

        self.label_info.setText(f"Settings saved")

    def quit_settings(self):
        self.label_test_api.setText(f"")
        self.label_info.setText(f"")
        self.close()
import os
from PySide6.QtWidgets import QWidget
from apscheduler.schedulers.qt import QTimer

from ui.ui_settings import Ui_Settings
import wk_api as wk
import json


def gen_srs_stages(buttons):
    srs_stages = ""
    for number, stages in enumerate(buttons, start=1):
        if stages.isChecked():
            srs_stages += f"{number},"

    return srs_stages


class SettingsWindow(QWidget, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_info.setText("")

        # Buttons
        self.btn_test.clicked.connect(self.test_api)
        self.btn_save.clicked.connect(self.save_settings)
        self.btn_quit.clicked.connect(self.quit_settings)

        # Additional options visibility
        self.check_r_radicals.toggled.connect(self.widget_radicals_srs.setVisible)
        self.check_r_kanji.toggled.connect(self.widget_kanji_srs.setVisible)
        self.check_r_vocabulary.toggled.connect(self.widget_vocabulary_srs.setVisible)

        if not self.check_r_radicals.isChecked():
            self.widget_radicals_srs.setVisible(False)
        if not self.check_r_kanji.isChecked():
            self.widget_kanji_srs.setVisible(False)
        if not self.check_r_vocabulary.isChecked():
            self.widget_vocabulary_srs.setVisible(False)

        # SRS buttons lists
        self.check_srs_radicals_buttons = [
            self.check_srs_radicals_1,
            self.check_srs_radicals_2,
            self.check_srs_radicals_3,
            self.check_srs_radicals_4,
            self.check_srs_radicals_5,
            self.check_srs_radicals_6,
            self.check_srs_radicals_7,
            self.check_srs_radicals_8,
        ]
        self.check_srs_kanji_buttons = [
            self.check_srs_kanji_1,
            self.check_srs_kanji_2,
            self.check_srs_kanji_3,
            self.check_srs_kanji_4,
            self.check_srs_kanji_5,
            self.check_srs_kanji_6,
            self.check_srs_kanji_7,
            self.check_srs_kanji_8,
        ]
        self.check_srs_vocabulary_buttons = [
            self.check_srs_vocabulary_1,
            self.check_srs_vocabulary_2,
            self.check_srs_vocabulary_3,
            self.check_srs_vocabulary_4,
            self.check_srs_vocabulary_5,
            self.check_srs_vocabulary_6,
            self.check_srs_vocabulary_7,
            self.check_srs_vocabulary_8,
        ]

        # Start function on start
        self.check_config()

    def test_api(self):
        self.save_settings()
        wk.get_headers()
        try:
            user_level = wk.get_user_level()
            self.label_test_api.setText(
                f"Your user level is {user_level}. API key is valid. "
            )
        except Exception as e:
            self.label_test_api.setText(f"Error {e}.")

    def check_config(self):
        if os.path.exists("config.json"):
            with open("config.json", "r") as file:
                data = json.load(file)

            if str(data["wk_api_key"]) == "":
                self.text_api.setText("Enter WaniKani API key")
            else:
                self.text_api.setText(f"{data["wk_api_key"]}")

            # Lessons
            self.check_l_radicals.setChecked(data["lessons"]["radical"])
            self.check_l_kanji.setChecked(data["lessons"]["kanji"])
            self.check_l_vocabulary.setChecked(data["lessons"]["vocabulary"])
            self.check_user_level_lesson.setChecked(data["lessons"]["only_user_level"])

            # Reviews
            self.check_r_radicals.setChecked(data["reviews"]["radical"]["is_checked"])
            self.check_user_level_review_radicals.setChecked(
                data["reviews"]["radical"]["only_user_level"]
            )
            for button in self.check_srs_radicals_buttons:
                getattr(self, button.objectName()).setChecked(False)
            if data["reviews"]["radical"]["srs_stages"] != "":
                for number in (
                    data["reviews"]["radical"]["srs_stages"].strip(",").split(",")
                ):
                    getattr(self, f"check_srs_radicals_{number}").setChecked(True)

            self.check_r_kanji.setChecked(data["reviews"]["kanji"]["is_checked"])
            self.check_user_level_review_kanji.setChecked(
                data["reviews"]["kanji"]["only_user_level"]
            )
            for button in self.check_srs_kanji_buttons:
                getattr(self, button.objectName()).setChecked(False)
            if data["reviews"]["kanji"]["srs_stages"] != "":
                for number in (
                    data["reviews"]["kanji"]["srs_stages"].strip(",").split(",")
                ):
                    getattr(self, f"check_srs_kanji_{number}").setChecked(True)

            self.check_r_vocabulary.setChecked(
                data["reviews"]["vocabulary"]["is_checked"]
            )
            self.check_user_level_review_vocabulary.setChecked(
                data["reviews"]["vocabulary"]["only_user_level"]
            )
            for button in self.check_srs_vocabulary_buttons:
                getattr(self, button.objectName()).setChecked(False)
            if data["reviews"]["vocabulary"]["srs_stages"] != "":
                for number in (
                    data["reviews"]["vocabulary"]["srs_stages"].strip(",").split(",")
                ):
                    getattr(self, f"check_srs_vocabulary_{number}").setChecked(True)

        else:
            self.text_api.setText("Enter WaniKani API key")

    def save_settings(self):
        configuration = {
            "wk_api_key": f"{self.text_api.text()}",
            "lessons": {
                "radical": self.check_l_radicals.isChecked(),
                "kanji": self.check_l_kanji.isChecked(),
                "vocabulary": self.check_l_vocabulary.isChecked(),
                "only_user_level": self.check_user_level_lesson.isChecked(),
            },
            "reviews": {
                "radical": {
                    "is_checked": self.check_r_radicals.isChecked(),
                    "only_user_level": self.check_user_level_review_radicals.isChecked(),
                    "srs_stages": gen_srs_stages(self.check_srs_radicals_buttons),
                },
                "kanji": {
                    "is_checked": self.check_r_kanji.isChecked(),
                    "only_user_level": self.check_user_level_review_kanji.isChecked(),
                    "srs_stages": gen_srs_stages(self.check_srs_kanji_buttons),
                },
                "vocabulary": {
                    "is_checked": self.check_r_vocabulary.isChecked(),
                    "only_user_level": self.check_user_level_review_vocabulary.isChecked(),
                    "srs_stages": gen_srs_stages(self.check_srs_vocabulary_buttons),
                },
            },
        }

        with open("config.json", "w") as file:
            json.dump(configuration, file, indent=4)

        self.label_info.setText(f"Settings saved")
        QTimer.singleShot(3000, lambda: self.label_info.setText(""))

    def quit_settings(self):
        self.label_test_api.setText(f"")
        self.label_info.setText(f"")
        self.check_config()
        self.close()

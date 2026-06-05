from PySide6.QtWidgets import QWidget
from ui.ui_settings import Ui_Settings

class SettingsWindow(QWidget, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def action(self):
        pass

import os.path
from PySide6.QtWidgets import (
    QApplication,
)
from apscheduler.schedulers.qt import QtScheduler, QTimer
import wk_notify as wkn
from widgets.settings_window import SettingsWindow
import widgets.tray as tr


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Scheduler
    scheduler = QtScheduler()
    wkn.start_scheduler(scheduler)

    # Settings Window
    settings_window = SettingsWindow()

    # Tray
    tray = tr.Tray(scheduler, settings_window)
    tray.show()

    # Open settings if config.json doesn't exist else run review check
    if not os.path.exists("config.json"):
        settings_window.show()
    else:
        tr.user_check("review")

    # App execution
    app.exec()


if __name__ == "__main__":
    main()

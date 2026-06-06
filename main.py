import os.path
from functools import partial

from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QPushButton, QLabel
from PySide6.QtGui import QIcon, QAction
from apscheduler.schedulers.qt import QtScheduler, QTimer

import wk_notify as wkn
from widgets.settings_window import SettingsWindow


def main():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Tray
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("img/icon.png"))
    tray.setVisible(True)

    menu = QMenu()
    check_lessons = QAction("Check lessons")
    menu.addAction(check_lessons)
    check_review = QAction("Check reviews")
    menu.addAction(check_review)
    menu.addSeparator()
    settings = QAction("Settings")
    menu.addAction(settings)
    menu.addSeparator()
    quit = QAction("Quit")
    menu.addAction(quit)

    tray.setContextMenu(menu)

    # Settings Window
    settings_window = SettingsWindow()

    # Open settings if config.json doesn't exist else run review check
    if not os.path.exists("config.json"):
        settings_window.show()
    else:
        QTimer.singleShot(10, partial(user_check, "review"))

    # Scheduler
    scheduler = QtScheduler()
    wkn.start_scheduler(scheduler)

    # Tray button functions
    check_lessons.triggered.connect(partial(user_check, "lesson"))
    check_review.triggered.connect(partial(user_check, "review"))
    settings.triggered.connect(settings_window.show)
    quit.triggered.connect(scheduler.shutdown)
    quit.triggered.connect(app.quit)

    # App execution
    app.exec()

def user_check(task_type):
    wkn.check_in_progress_notification()
    try:
        wkn.check_available_items(task_type,True)
    except Exception as e:
        wkn.error_notification(e)

if __name__ == "__main__":
    main()
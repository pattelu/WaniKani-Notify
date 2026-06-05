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
    settings = QAction("Settings")
    menu.addAction(settings)
    menu.addSeparator()
    quit = QAction("Quit")
    menu.addAction(quit)

    tray.setContextMenu(menu)

    # Notification on app start
    wkn.start_notification()

    # Check review with app start
    QTimer.singleShot(0, check_review_on_start)

    # Scheduler
    scheduler = QtScheduler()
    wkn.start_scheduler(scheduler)

    # Settings Window
    settings_window = SettingsWindow()

    # Tray button functions
    settings.triggered.connect(settings_window.show)
    quit.triggered.connect(scheduler.shutdown)
    quit.triggered.connect(app.quit)

    # App execution
    app.exec()


def check_review_on_start():
    try:
        wkn.review_notification()
    except Exception as e:
        wkn.error_notification(e)

if __name__ == "__main__":
    main()
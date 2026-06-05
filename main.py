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
    check_review = QAction("Check reviews")
    menu.addAction(check_review)
    settings = QAction("Settings")
    menu.addAction(settings)
    menu.addSeparator()
    quit = QAction("Quit")
    menu.addAction(quit)

    tray.setContextMenu(menu)

    # Notification on app start
    wkn.start_notification()

    # Check review with app start
    QTimer.singleShot(10, user_review_check)

    # Scheduler
    scheduler = QtScheduler()
    wkn.start_scheduler(scheduler)

    # Settings Window
    settings_window = SettingsWindow()

    # Tray button functions
    check_review.triggered.connect(user_review_check)
    settings.triggered.connect(settings_window.show)
    quit.triggered.connect(scheduler.shutdown)
    quit.triggered.connect(app.quit)

    # App execution
    app.exec()


def user_review_check():
    wkn.check_in_progress_notification()
    try:
        wkn.check_reviews(True)
    except Exception as e:
        wkn.error_notification(e)

if __name__ == "__main__":
    main()
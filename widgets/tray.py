from functools import partial
from threading import Thread
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QAction, QIcon
import sys
from pathlib import Path
import wk_notify as wkn


class Tray(QSystemTrayIcon):
    def __init__(self, scheduler, settings_window):
        super().__init__()

        self.settings_window = settings_window
        self.scheduler = scheduler

        self.icon_path = resource_path("img/icon.png")
        self.setIcon(QIcon(self.icon_path))
        self.setVisible(True)

        self.menu = QMenu()
        self.check_lessons = QAction("Check lessons")
        self.menu.addAction(self.check_lessons)
        self.check_review = QAction("Check reviews")
        self.menu.addAction(self.check_review)
        self.closest_review = QAction("Closest reviews")
        self.menu.addAction(self.closest_review)
        self.menu.addSeparator()
        self.settings = QAction("Settings")
        self.menu.addAction(self.settings)
        self.menu.addSeparator()
        self.quit = QAction("Quit")
        self.menu.addAction(self.quit)

        self.setContextMenu(self.menu)

        # Tray button functions
        self.check_lessons.triggered.connect(partial(user_check, "lesson"))
        self.check_review.triggered.connect(partial(user_check, "review"))
        self.closest_review.triggered.connect(check_closest_review)
        self.settings.triggered.connect(self.open_settings)
        self.quit.triggered.connect(self.quit_app)

    def quit_app(self):
        self.scheduler.shutdown()
        QApplication.quit()

    def open_settings(self):
        self.settings_window.show()


def user_check(task_type):
    wkn.check_in_progress_notification()
    try:
        Thread(
            target=wkn.check_available_items,
            args=(
                task_type,
                True,
            ),
            daemon=True,
        ).start()
    except Exception as e:
        wkn.error_notification(e)


def check_closest_review():
    wkn.check_in_progress_notification(10)
    try:
        Thread(
            target=wkn.check_closest_review,
            args=(),
            daemon=True,
        ).start()
    except Exception as e:
        wkn.error_notification(e)


def resource_path(relative_path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).resolve().parent.parent

    return str(base_path / relative_path)

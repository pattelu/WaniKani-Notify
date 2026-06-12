from unittest.mock import patch, MagicMock
import pytest
from widgets.tray import Tray


@pytest.fixture
def tray_check(qtbot):
    with patch("widgets.tray.user_check") as mock_user_check:
        tray = Tray(None, None)

        yield tray, mock_user_check


@pytest.fixture
def tray_basic(qtbot):
    tray = Tray(None, None)

    yield tray


def test_check_lessons(tray_check):
    tray_obj, mock_user_check = tray_check
    tray_obj.check_lessons.trigger()

    mock_user_check.assert_called_once_with("lesson")


def test_check_reviews(tray_check):
    tray_obj, mock_user_check = tray_check
    tray_obj.check_review.trigger()

    mock_user_check.assert_called_once_with("review")


def test_closest_review(qtbot):
    with patch("widgets.tray.check_closest_review") as mock_closest_review:
        tray = Tray(None, None)
        tray.closest_review.trigger()

    mock_closest_review.assert_called_once_with()


def test_open_settings(tray_basic):
    tray_basic.settings_window = MagicMock()
    tray_basic.settings.trigger()

    tray_basic.settings_window.show.assert_called_once()


def test_quit_app(tray_basic):
    tray_basic.scheduler = MagicMock()

    with patch("PySide6.QtWidgets.QApplication.quit") as mock_quit:
        tray_basic.quit_app()

        tray_basic.scheduler.shutdown.assert_called_once()
        mock_quit.assert_called_once()

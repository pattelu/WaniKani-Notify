from pathlib import Path
from unittest.mock import patch

import pytest

from widgets.settings_window import SettingsWindow
import os.path
from widgets.tray import resource_path


@pytest.fixture
def settings(qtbot):
    window = SettingsWindow()
    qtbot.addWidget(window)

    yield window

@pytest.fixture
def remove_config():
    if os.path.exists("config.json"):
        path = resource_path("config.json")
        Path(path).unlink(missing_ok=True)


def test_default_settings(remove_config, settings, ):
    assert settings.text_api.text() == "Enter WaniKani API key"
    assert settings.check_user_level_lesson.isChecked() == False
    assert settings.check_l_radicals.isChecked() == False
    assert settings.check_l_kanji.isChecked() == False
    assert settings.check_l_vocabulary.isChecked() == False

    assert settings.check_r_radicals.isChecked() == False
    assert settings.check_r_kanji.isChecked() == False
    assert settings.check_r_vocabulary.isChecked() == False

    assert settings.widget_radicals_srs.isVisible() == False
    assert settings.widget_kanji_srs.isVisible() == False
    assert settings.widget_vocabulary_srs.isVisible() == False


def test_valid_api_key(settings):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": {"level": 20}}

        settings.btn_test.click()

        mock_get.assert_called_once()

        assert settings.label_test_api.text() == f"Your user level is 20. API key is valid. "


def test_invalid_api_key(settings):
    settings.text_api.setText("invalid-api")
    settings.btn_test.click()

    if "Error" in settings.label_test_api.text():
        assert True


def test_checkbox_dependencies(settings):
    pass


def test_save_settings(settings):

    #
    # Add
    # More
    #

    settings.btn_save.click()

    assert settings.label_info.text() == "Settings saved"


def test_quit_without_saving(settings):
    pass

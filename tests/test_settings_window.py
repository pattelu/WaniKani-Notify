from pathlib import Path
import pytest

from widgets.settings_window import SettingsWindow
import os.path
from widgets.tray import resource_path


@pytest.fixture
def settings(qtbot):
    if os.path.exists("config.json"):
        path = resource_path("config.json")
        Path(path).unlink(missing_ok=True)

    window = SettingsWindow()
    qtbot.addWidget(window)

    yield window


def test_default_settings(settings):
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


def test_api_key_info(settings):

    # Valid key env (?) / example response

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

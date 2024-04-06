"""Tests the streamlit app"""
from streamlit.testing.v1 import AppTest
import os


def test_app():
    """validates the file path and tests teh app"""
    test_directory = os.path.dirname(os.path.abspath(__file__))
    app_script_path = os.path.join(test_directory, "..", "voice_app.py")
    assert os.path.isfile(app_script_path), f"File not found at {app_script_path}"

    at = AppTest.from_file(app_script_path).run()
    assert not at.exception

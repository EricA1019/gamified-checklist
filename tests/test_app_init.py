"""
Test the main application initialization.
"""
import pytest
from unittest.mock import patch
import sys
import os

# Add the project root to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import GamifiedChecklistApp
from gamified_checklist.utils.logger import log_info

def test_app_creation():
    """Test that the app can be created without errors."""
    app = GamifiedChecklistApp()
    assert app is not None
    assert hasattr(app, 'build')

def test_app_build():
    """Test that the app build method exists and is callable."""
    app = GamifiedChecklistApp()
    # Just test that the method exists and is callable
    assert hasattr(app, 'build')
    assert callable(getattr(app, 'build'))

def test_logger_functionality():
    """Test that our logging system works."""
    # This should not raise any exceptions
    log_info("Test message", "TestTag")
    assert True  # If we get here, logging worked

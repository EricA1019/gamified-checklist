"""
Logging utility for the Gamified Checklist app.
Provides tagged logging to help with debugging and tracking.
"""
import logging
import sys
from datetime import datetime

def setup_logger(name="GamifiedChecklist", level=logging.INFO):
    """
    Set up a tagged logger for the application.
    
    Args:
        name: The logger name
        level: The logging level
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:  # Avoid duplicate handlers
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(name)s] %(asctime)s - %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    
    return logger

# Create the main app logger
app_logger = setup_logger()

def log_info(message, tag="General"):
    """Log an info message with a tag."""
    app_logger.info(f"[{tag}] {message}")

def log_error(message, tag="General"):
    """Log an error message with a tag."""
    app_logger.error(f"[{tag}] {message}")

def log_debug(message, tag="General"):
    """Log a debug message with a tag."""
    app_logger.debug(f"[{tag}] {message}")

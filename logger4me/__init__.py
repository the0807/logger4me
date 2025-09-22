"""
logger4me - A simple and colorful Python logging utility

This package provides enhanced console output with ANSI color codes 
and flexible file logging options.
"""

from .logger import get_logger, ColorFormatter, LOG_COLORS

__version__ = "0.1.0"
__author__ = "the0807"
__email__ = "the0807.eom@gmail.com"
__description__ = "A simple and colorful Python logging utility"

__all__ = ["get_logger", "ColorFormatter", "LOG_COLORS"]

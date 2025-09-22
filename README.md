# logger4me

![img1](img/img1.png)

A simple and colorful Python logging utility that provides enhanced console output with ANSI color codes and flexible file logging options.

## Features

- **Colorful Console Output**: Different log levels are displayed in different colors for better readability
- **File Logging Support**: Optional file logging with customizable file paths
- **Color Control**: Choose whether to save colors in log files or keep them plain text
- **Flexible Log Levels**: Support for all standard Python logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Easy Integration**: Simple one-function setup for your logging needs

## Installation

Install logger4me using uv:

```bash
uv add logger4me
```

Install logger4me using pip:

```bash
pip install logger4me
```

## Usage

### Basic Usage

```python
from logger4me import get_logger

# Create a logger with default settings
logger = get_logger()

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Advanced Configuration

```python
from logger4me import get_logger
import logging

# Create a logger with custom settings
logger = get_logger(
    level = 10,        # Set minimum log level
    log_file = './logs/app.log',  # Save logs to file
    save_color = False            # Don't save ANSI colors to file
)
```

### Parameters

- **level** (int): Minimum logging level (default: `logging.INFO`)
  - `10`: Debug messages and above(`logging.DEBUG`)
  - `20`: Info messages and above(`logging.INFO`)
  - `30`: Warning messages and above(`logging.WARNING`)
  - `40`: Error messages and above(`logging.ERROR`)
  - `50`: Critical messages only(`logging.CRITICAL`)

- **log_file** (str, optional): Path to save log messages to a file (default: `None`)
  - If provided, creates the directory structure automatically
  - File is created in write mode, overwriting existing content

- **save_color** (bool): Whether to save ANSI color codes in the log file (default: `False`)
  - `True`: Colors are preserved in the file
  - `False`: Plain text without color codes (recommended for file logs)

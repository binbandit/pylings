"""
Concept: Logging

The `logging` module provides a flexible framework for emitting log messages.
It's much better than print() for production code.

Why use logging instead of print()?
- Control verbosity with log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Easily enable/disable output without removing code
- Add timestamps automatically
- Write to files, network, etc.
- Filter messages by severity

Log levels (in order of severity):
    DEBUG    - Detailed diagnostic information
    INFO     - Confirmation that things are working
    WARNING  - Something unexpected, but program still works
    ERROR    - A serious problem, some functionality failed
    CRITICAL - Program may not be able to continue

Basic usage:
    import logging

    # Configure the logging system
    logging.basicConfig(level=logging.INFO)

    # Create a logger
    logger = logging.getLogger(__name__)

    # Log messages at different levels
    logger.debug("Detailed debug info")    # Won't show if level=INFO
    logger.info("Program started")         # Will show
    logger.warning("Disk space low")       # Will show
    logger.error("Connection failed")      # Will show

Task:
1. In setup_logging(): Configure basicConfig with level=logging.INFO
2. In log_events(): Log three messages using the logger:
   - An INFO message: "Application started"
   - A WARNING message: "Disk space low"
   - An ERROR message: "Connection failed"
"""

import logging


def setup_logging():
    """Configure the logging system."""
    # TODO: Configure basic logging to capture INFO level and above
    # Hint: logging.basicConfig(level=logging.INFO)
    pass


def log_events():
    """Log several events at different levels."""
    setup_logging()

    # Create a logger for this module
    logger = logging.getLogger("exercise_logger")

    # TODO: Log an INFO message: "Application started"
    # Hint: logger.info("message")

    # TODO: Log a WARNING message: "Disk space low"
    # Hint: logger.warning("message")

    # TODO: Log an ERROR message: "Connection failed"
    # Hint: logger.error("message")

    pass  # TODO: Remove this pass after adding the log statements


def main():
    """Run the logging exercise."""
    print("=" * 50)
    print("Running logging exercise...")
    print("You should see log messages below:")
    print("=" * 50)

    log_events()

    print("=" * 50)
    print("If you saw INFO, WARNING, and ERROR messages above,")
    print("you've completed the exercise!")


if __name__ == "__main__":
    main()

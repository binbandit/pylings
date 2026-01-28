
# LOGGING
# =======
#
# What: The `logging` module tracks events that happen when some software runs.
#       Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
#
# Why:  `print()` is bad for production. Logging allows you to toggle output levels,
#       timestamp messages, and write to files without changing code.
#
# How:  import logging
#       logging.basicConfig(level=logging.INFO)
#       logger = logging.getLogger(__name__)
#       logger.info("Message")
#
# Task:
# 1. Configure basic logging to capture INFO level messages.
# 2. Create a logger.
# 3. Log a warning message "Watch out!".
# 4. (We can't easily assert stdout in this simple exercise, so just run it)

import logging

def setup_logging():
    # TODO: call logging.basicConfig with level=logging.INFO
    pass

def log_events():
    setup_logging()
    logger = logging.getLogger("exercise_logger")
    
    # TODO: Log an info message "Starting app"
    # TODO: Log a warning "Disk space low"
    # TODO: Log an error "Connection failed"
    pass

if __name__ == "__main__":
    log_events()
    print("Logging ran (observe output above).")

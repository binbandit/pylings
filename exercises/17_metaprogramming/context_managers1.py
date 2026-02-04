"""
Concept: Context Managers (Class-based)

Context managers control resource allocation and cleanup using the `with` statement.
They guarantee that cleanup code runs, even if an exception occurs.

Common uses:
- File handling: `with open('file.txt') as f:` (auto-closes file)
- Database connections: Auto-commit or rollback transactions
- Locks: `with threading.Lock():` (auto-releases lock)
- Timing: Measure how long a block of code takes

To create a class-based context manager, implement two methods:

1. `__enter__(self)`:
   - Called when entering the `with` block
   - Sets up the resource
   - Returns the resource (available as `as variable`)

2. `__exit__(self, exc_type, exc_val, exc_tb)`:
   - Called when exiting the `with` block (always, even on error!)
   - Cleans up the resource
   - Parameters contain exception info (all None if no exception)
   - Return True to suppress exceptions, False/None to propagate them

Example:
```python
class DatabaseConnection:
    def __enter__(self):
        self.conn = create_connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False  # Don't suppress exceptions

with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")
# Connection is automatically closed here
```

Task:
Implement the `Tracer` context manager that tracks when we enter and exit.
- `__enter__` should append "enter" to the `events` list and return self
- `__exit__` should append "exit" to the `events` list
"""

# This list tracks the sequence of events
events = []


class Tracer:
    """A context manager that traces entry and exit of a code block."""

    # TODO: Implement __enter__ method
    # - Append "enter" to the events list
    # - Return self

    # TODO: Implement __exit__ method
    # - Takes parameters: self, exc_type, exc_val, exc_tb
    # - Append "exit" to the events list
    # - Return False (or nothing) to not suppress exceptions

    pass  # Remove this when you add the methods


def main():
    events.clear()

    # Check that the methods exist
    tracer = Tracer()

    if not hasattr(tracer, "__enter__"):
        raise AssertionError(
            "Tracer is missing the __enter__ method!\n"
            "Add: def __enter__(self):\n"
            "         events.append('enter')\n"
            "         return self"
        )

    if not hasattr(tracer, "__exit__"):
        raise AssertionError(
            "Tracer is missing the __exit__ method!\n"
            "Add: def __exit__(self, exc_type, exc_val, exc_tb):\n"
            "         events.append('exit')"
        )

    # Test the context manager
    events.clear()

    with Tracer() as t:
        events.append("inside")

    expected = ["enter", "inside", "exit"]

    if events != expected:
        raise AssertionError(
            f"Expected events to be {expected}, but got {events}\n"
            "Make sure __enter__ appends 'enter' and __exit__ appends 'exit'"
        )

    # Test that cleanup happens even with exceptions
    events.clear()

    try:
        with Tracer():
            events.append("before error")
            raise ValueError("test error")
    except ValueError:
        pass  # Expected

    expected_with_error = ["enter", "before error", "exit"]

    if events != expected_with_error:
        raise AssertionError(
            f"With exception: expected {expected_with_error}, got {events}\n"
            "__exit__ should run even when an exception occurs!"
        )

    print("Context manager working correctly!")
    print("__exit__ runs even when exceptions occur - guaranteed cleanup!")


if __name__ == "__main__":
    main()

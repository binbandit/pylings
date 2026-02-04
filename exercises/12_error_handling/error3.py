"""
Concept: The Finally Block

The `finally` block contains code that ALWAYS runs, whether an exception
occurred or not. This makes it perfect for cleanup operations.

Syntax:
    try:
        risky_operation()
    except SomeError:
        handle_error()
    finally:
        cleanup()  # This ALWAYS runs!

Why use finally?
- Close files that were opened
- Release database connections
- Clean up temporary resources
- Reset state that needs to be restored

The finally block runs even if:
- The try block succeeds
- An exception is caught
- An exception is NOT caught (finally runs, then exception propagates)
- A return statement is executed in try or except

Example:
    file = open("data.txt")
    try:
        process(file)
    finally:
        file.close()  # File is ALWAYS closed, even if process() crashes

Task: The `run_with_cleanup` function should call `process()` and ensure
that `cleanup()` is ALWAYS called afterward, even if process() raises an error.
Use a try/finally block to guarantee the cleanup happens.
"""

# Global flag to track if cleanup was called
cleanup_was_called = False


def cleanup():
    """Mark that cleanup has been performed."""
    global cleanup_was_called
    cleanup_was_called = True


def process():
    """A function that always raises an error."""
    raise ValueError("Something went wrong during processing!")


def run_with_cleanup():
    """
    Run process() and ensure cleanup() is always called.

    Even though process() raises an exception, cleanup() must still be called.
    The exception should be allowed to propagate after cleanup.
    """
    # TODO: Wrap process() in a try/finally block
    # TODO: Call cleanup() in the finally block
    # TODO: Let the ValueError propagate (don't catch it, just ensure cleanup runs)
    process()


def main():
    global cleanup_was_called

    # Reset the flag
    cleanup_was_called = False

    # run_with_cleanup should raise ValueError, but cleanup should still happen
    try:
        run_with_cleanup()
        raise Exception(
            "Expected run_with_cleanup() to raise ValueError, but it didn't. "
            "Make sure you're not catching the exception - just use finally for cleanup."
        )
    except ValueError:
        # This is expected - process() raises ValueError
        pass

    # Check that cleanup was called despite the exception
    if not cleanup_was_called:
        raise Exception(
            "cleanup() was not called! "
            "Did you use a 'finally' block to ensure cleanup() runs?"
        )

    print("Cleanup was correctly called even when an exception occurred!")


if __name__ == "__main__":
    main()

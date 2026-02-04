"""
Concept: Working with Dates and Times (datetime module)

The `datetime` module is Python's standard library for handling dates and times.

Key classes:
- `datetime`: Represents a specific point in time (year, month, day, hour, etc.)
- `timedelta`: Represents a duration (e.g., 7 days, 3 hours, 30 minutes)

Common operations:
    from datetime import datetime, timedelta

    now = datetime.now()           # Current date and time
    today = datetime.today()       # Also current date and time

    one_week = timedelta(days=7)   # A duration of 7 days
    one_hour = timedelta(hours=1)  # A duration of 1 hour

    future = now + one_week        # Add a duration to a datetime
    past = now - timedelta(days=1) # Subtract a duration

Why use datetime instead of manual calculations?
- Handles leap years automatically
- Handles varying month lengths
- Handles timezone complexities
- Prevents off-by-one errors

Task:
1. Get the current date/time using datetime.now() and assign it to `now`
2. Create a timedelta representing 7 days and assign it to `one_week`
"""

from datetime import datetime, timedelta


def main():
    # TODO: Get the current date and time
    # Hint: Use datetime.now()
    now = None

    # TODO: Create a timedelta of 7 days
    # Hint: Use timedelta(days=7)
    one_week = None

    # Verification
    if now is None:
        raise AssertionError(
            "Variable 'now' is None.\nSet it to the current time using datetime.now()"
        )

    if one_week is None:
        raise AssertionError(
            "Variable 'one_week' is None.\n"
            "Set it to a timedelta of 7 days using timedelta(days=7)"
        )

    if not isinstance(now, datetime):
        raise AssertionError(
            f"'now' should be a datetime object, but got {type(now).__name__}"
        )

    if not isinstance(one_week, timedelta):
        raise AssertionError(
            f"'one_week' should be a timedelta object, but got {type(one_week).__name__}"
        )

    if one_week.days != 7:
        raise AssertionError(
            f"'one_week' should represent 7 days, but represents {one_week.days} days"
        )

    # Calculate future date
    next_week = now + one_week

    print(f"Current time: {now}")
    print(f"One week later: {next_week}")
    print(f"Difference: {one_week}")
    print("Successfully used datetime and timedelta!")


if __name__ == "__main__":
    main()

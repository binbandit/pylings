"""
Concept: Datetime

What:
The `datetime` module is Python's standard way of handling dates and times.
- `datetime`: Represents a specific moment (year, month, day, hour, minute, second).
- `timedelta`: Represents a **duration** or difference between two times (e.g., "7 days").

Why:
Never try to do date math (like "add 7 days") manually. You will get it wrong (leap years, varying month lengths). Use `datetime`!

How:
```python
from datetime import datetime, timedelta

now = datetime.now()             # Current time
one_week = timedelta(days=7)    # Duration of 7 days
next_week = now + one_week       # Add duration to a date
```

Task:
1. Get the current time using `datetime.now()` and assign to `now`.
2. Create a `timedelta` representing exactly 7 days and assign to `delta`.
"""

from datetime import datetime, timedelta

def main():
    # FIX ME: Get current time
    # now = ...
    now = None
    
    # FIX ME: Create a timedelta of 7 days
    # delta = ...
    delta = None
    
    if now is None or delta is None:
        print("Please set 'now' and 'delta'!")
        return
        
    future = now + delta
    
    if not isinstance(now, datetime):
        raise Exception("now should be a datetime object")
        
    if not isinstance(delta, timedelta):
        raise Exception("delta should be a timedelta object")
        
    if delta.days != 7:
        raise Exception("delta should be 7 days")
        
    # Check approximately (ignoring execution time micros)
    if (future - now).days != 7:
        raise Exception("Future time calculation seems off")

if __name__ == "__main__":
    main()

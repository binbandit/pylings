"""
Concept: Environment Variables

What:
Environment variables are values set outside the program (in the OS or shell).
In Python, we access them via `os.environ`, which acts like a dictionary.

Why:
**Security and Configuration.**
Never hardcode passwords or API keys in your code! 
Read them from environment variables so your code can be public (open source) while your secrets stay private.

How:
```python
import os

# Get a variable (returns None if missing, won't crash)
api_key = os.getenv("API_KEY") 

# Get a variable (crashes if missing)
# user = os.environ["USER"] 

# Set a variable (only for this process)
os.environ["MY_VAR"] = "value"
```

Task:
1. Set an environment variable named `APP_MODE` to "production".
2. Retrieve it using `os.getenv` and assign it to `current_mode`.
"""

import os

def main():
    # FIX ME: Set APP_MODE to "production"
    # os.environ["APP_MODE"] = "production"
    
    # FIX ME: Get APP_MODE
    # current_mode = ...
    current_mode = None
    
    if current_mode != "production":
        raise Exception(f"Expected 'production', got '{current_mode}'")
        
    # Verify it is actually in environ
    if os.environ.get("APP_MODE") != "production":
        raise Exception("APP_MODE not found in os.environ")

if __name__ == "__main__":
    main()

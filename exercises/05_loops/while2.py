"""
Concept: Infinite Loops and Break

What:
- An "Infinite Loop" is a loop where the condition never becomes False (`while True`).
- The `break` keyword immediately exits the nearest enclosing loop.

Why:
Sometimes you *want* to loop forever (e.g., a game loop or a server listening for requests)
until a specific event happens inside the loop (e.g., specific input or an error).

How:
```python
while True:
    command = input("> ")
    if command == "quit":
        break  # Exit the loop immediately
    print("You typed:", command)
```

Task:
The loop below runs forever (`while True`).
Add a check inside the loop: if `counter` equals 10, stop the loop using `break`.
"""

def main():
    counter = 0
    
    while True:
        counter += 1
        
        # FIX ME: Check if counter is 10, then break
        if counter > 20: # Safety break to prevent actual infinite loop during test
            raise Exception("Loop ran too long! Did you forget to break?")
            
    if counter != 10:
        raise Exception(f"Counter should be 10, got {counter}")

if __name__ == "__main__":
    main()

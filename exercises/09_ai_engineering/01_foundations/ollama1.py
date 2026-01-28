"""
Concept: Local AI (Ollama)
Ollama allows you to run models locally. API clients usually point to `localhost:11434`.

Task: Specify a model name (e.g., 'llama3') to generate a response.
"""

import ollama

def main():
    # FIX ME: We want to chat with "llama3" (or "tinyllama").
    # For this exercise, we just want to construct the call.
    model = ""
    
    if not model:
        raise Exception("Define a model name!")
    
    # We won't actually call it to avoid hanging/errors if not installed.
    # Just checking the variable.
    print(f"Ready to call {model}")

if __name__ == "__main__":
    main()

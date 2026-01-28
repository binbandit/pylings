"""
Concept: AI Engineering (OpenAI Client)
The `openai` library is the standard client for interacting with GPT models. You must initialize it with an API key.

Task: Initialize the `OpenAI` client with a dummy API key for testing.
"""

import os
from openai import OpenAI

def main():
    # FIX ME: Set a dummy API key to make the client init work (for this exercise)
    # os.environ["OPENAI_API_KEY"] = "sk-dummy"
    
    try:
        client = OpenAI()
        print("OpenAI client initialized!")
    except Exception as e:
        print(f"Failed to init client: {e}")
        raise

if __name__ == "__main__":
    main()

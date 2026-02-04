"""
Concept: OpenAI Client Initialization

The `openai` Python library is the official client for interacting with OpenAI's
GPT models (ChatGPT, GPT-4, etc.). Before making any API calls, you must
initialize the client with your API key.

The OpenAI client looks for the API key in this order:
1. The `api_key` parameter passed directly to `OpenAI()`
2. The `OPENAI_API_KEY` environment variable

For production code, you should use environment variables to keep your API key
secure and out of your source code. You can set it like this:

    import os
    os.environ["OPENAI_API_KEY"] = "your-api-key"

Or in your shell before running your script:

    export OPENAI_API_KEY="your-api-key"

Task: Set the OPENAI_API_KEY environment variable before initializing the client.
      For this exercise, use "sk-test-key-12345" as a dummy API key.
"""

import os
from openai import OpenAI


def create_openai_client():
    """Initialize and return an OpenAI client.

    The client needs an API key to be set in the environment.
    """
    # TODO: Set the OPENAI_API_KEY environment variable
    # Hint: Use os.environ to set environment variables
    # os.environ[???] = ???

    client = OpenAI()
    return client


def main():
    # This will fail if the API key is not set
    client = create_openai_client()

    # Verify the client was created successfully
    if client is None:
        raise Exception("Failed to create OpenAI client!")

    # Check that the API key was set correctly
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key.startswith("sk-"):
        raise Exception(
            "API key not set correctly!\n"
            "Hint: Set os.environ['OPENAI_API_KEY'] to a key starting with 'sk-'"
        )

    print("OpenAI client initialized successfully!")
    print(f"API key configured: {api_key[:10]}...")


if __name__ == "__main__":
    main()

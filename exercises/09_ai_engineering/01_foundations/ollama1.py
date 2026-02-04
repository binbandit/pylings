"""
Concept: Local LLMs with Ollama

Ollama is a tool that lets you run large language models locally on your machine.
This is useful for:
- Privacy: Your data never leaves your computer
- Cost: No API fees for inference
- Offline use: Works without internet
- Experimentation: Try different models easily

Ollama runs as a local server (default: http://localhost:11434) and provides
an API similar to OpenAI's. Popular models include:
- "llama3" or "llama3.2" - Meta's open LLaMA models
- "mistral" - Mistral AI's efficient model
- "codellama" - Optimized for code generation
- "tinyllama" - Small, fast model for testing

To use Ollama:
1. Install from https://ollama.ai
2. Pull a model: `ollama pull llama3`
3. Use the Python client to interact with it

The basic chat structure looks like:
    ollama.chat(model="model_name", messages=[...])

Task: Configure the model name and create a properly formatted message for Ollama.
"""


def configure_ollama_chat():
    """Configure an Ollama chat request.

    Returns a tuple of (model_name, messages) that can be used with ollama.chat()
    """
    # TODO: Set the model name to "llama3" (or another model you have installed)
    model = ""  # FIX ME: Replace with a valid model name

    # TODO: Create a messages list with a single user message
    # Messages should be a list of dicts with "role" and "content" keys
    # Example: [{"role": "user", "content": "Hello!"}]
    messages = []  # FIX ME: Add a user message asking "What is Python?"

    return model, messages


def validate_chat_config(model, messages):
    """Validate that the chat configuration is correct."""
    # Check model name
    if not model:
        raise Exception(
            "Model name is empty!\n"
            "Hint: Set model to a valid Ollama model like 'llama3' or 'mistral'"
        )

    # Check messages structure
    if not messages:
        raise Exception(
            "Messages list is empty!\n"
            "Hint: Add at least one message dict with 'role' and 'content' keys"
        )

    if not isinstance(messages, list):
        raise Exception("Messages must be a list!")

    for i, msg in enumerate(messages):
        if not isinstance(msg, dict):
            raise Exception(f"Message {i} must be a dictionary!")
        if "role" not in msg:
            raise Exception(
                f"Message {i} missing 'role' key!\n"
                "Hint: Role should be 'user', 'assistant', or 'system'"
            )
        if "content" not in msg:
            raise Exception(
                f"Message {i} missing 'content' key!\n"
                "Hint: Content is the actual text of the message"
            )

    # Check for user message
    user_messages = [m for m in messages if m.get("role") == "user"]
    if not user_messages:
        raise Exception("No user message found!\nHint: Add a message with role='user'")


def main():
    model, messages = configure_ollama_chat()

    # Validate the configuration
    validate_chat_config(model, messages)

    print(f"Ollama configured successfully!")
    print(f"Model: {model}")
    print(f"Messages: {messages}")
    print("\nNote: This exercise doesn't actually call Ollama.")
    print("To test with a real model, install Ollama and run: ollama pull llama3")


if __name__ == "__main__":
    main()

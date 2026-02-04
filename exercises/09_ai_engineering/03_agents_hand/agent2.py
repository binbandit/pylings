"""
Concept: Parsing Agent Output (ReAct Format)

Agents often produce semi-structured text output that needs to be parsed.
A common format is the ReAct pattern:

    Thought: I need to search for information about Python.
    Action: search("Python programming")

Or with more structure:

    Thought: The user wants weather information.
    Action: get_weather
    Action Input: {"location": "Paris"}

Your parsing code must:
1. Handle multi-line output
2. Extract specific fields (Thought, Action, etc.)
3. Be robust to variations in formatting

Regular expressions are perfect for this! Key patterns:
- `r"Thought: (.*)"` - Capture everything after "Thought: "
- `r"Action: (.*)"` - Capture the action
- `re.DOTALL` flag - Make `.` match newlines too
- `re.MULTILINE` flag - Make `^` and `$` match line boundaries

Task: Use regex to extract the Action from agent output.
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedOutput:
    """Structured representation of parsed agent output."""

    thought: Optional[str] = None
    action: Optional[str] = None
    action_input: Optional[str] = None


def parse_agent_output(llm_output: str) -> ParsedOutput:
    """Parse ReAct-style agent output to extract thought and action.

    Expected format:
        Thought: <reasoning>
        Action: <action_name>(<arguments>)

    Args:
        llm_output: Raw text output from the LLM

    Returns:
        ParsedOutput with extracted fields
    """
    result = ParsedOutput()

    # Extract the Thought (everything after "Thought: " until newline)
    thought_match = re.search(r"Thought: (.*)", llm_output)
    if thought_match:
        result.thought = thought_match.group(1).strip()

    # TODO: Extract the Action using regex
    # The action comes after "Action: " and continues to end of line
    # Example: "Action: search('query')" should extract "search('query')"
    #
    # FIX ME: Use re.search() with a pattern similar to the thought extraction
    # Hint: r"Action: (.*)" will match "Action: " followed by anything
    action_match = None  # FIX ME: Replace with re.search(...)

    if action_match:
        result.action = action_match.group(1).strip()

    return result


def parse_action_with_input(llm_output: str) -> ParsedOutput:
    """Parse agent output with separate Action and Action Input lines.

    Expected format:
        Thought: <reasoning>
        Action: <action_name>
        Action Input: <input_value>

    Args:
        llm_output: Raw text output from the LLM

    Returns:
        ParsedOutput with extracted fields
    """
    result = ParsedOutput()

    # Extract Thought
    thought_match = re.search(r"Thought: (.*)", llm_output)
    if thought_match:
        result.thought = thought_match.group(1).strip()

    # TODO: Extract Action (just the action name, no input)
    # FIX ME: Similar to above
    action_match = None  # FIX ME
    if action_match:
        result.action = action_match.group(1).strip()

    # TODO: Extract Action Input
    # Pattern: r"Action Input: (.*)"
    # FIX ME: Extract the action input
    input_match = None  # FIX ME
    if input_match:
        result.action_input = input_match.group(1).strip()

    return result


def main():
    # Test 1: Basic ReAct format
    print("Test 1: Basic ReAct format")
    print("-" * 40)

    output1 = """Thought: I should look up information about Python.
Action: google_search('python programming language')"""

    parsed = parse_agent_output(output1)

    if parsed.thought != "I should look up information about Python.":
        raise Exception(f"Thought parsing failed! Got: {parsed.thought}")

    expected_action = "google_search('python programming language')"
    if parsed.action != expected_action:
        raise Exception(
            f"Action parsing failed!\n"
            f"Expected: {expected_action}\n"
            f"Got: {parsed.action}\n\n"
            f"Hint: Use re.search(r'Action: (.*)', llm_output) to match the action"
        )

    print(f"Thought: {parsed.thought}")
    print(f"Action: {parsed.action}")
    print("PASSED!\n")

    # Test 2: Action with separate input
    print("Test 2: Action with separate input")
    print("-" * 40)

    output2 = """Thought: I need to check the weather in Tokyo.
Action: get_weather
Action Input: Tokyo, Japan"""

    parsed2 = parse_action_with_input(output2)

    if parsed2.action != "get_weather":
        raise Exception(
            f"Action parsing failed!\nExpected: get_weather\nGot: {parsed2.action}"
        )

    if parsed2.action_input != "Tokyo, Japan":
        raise Exception(
            f"Action Input parsing failed!\n"
            f"Expected: Tokyo, Japan\n"
            f"Got: {parsed2.action_input}\n\n"
            f"Hint: Use re.search(r'Action Input: (.*)', llm_output)"
        )

    print(f"Thought: {parsed2.thought}")
    print(f"Action: {parsed2.action}")
    print(f"Action Input: {parsed2.action_input}")
    print("PASSED!\n")

    # Test 3: Handling edge cases
    print("Test 3: Output with no action")
    print("-" * 40)

    output3 = """Thought: I now have all the information I need.
Final Answer: Python is a programming language."""

    parsed3 = parse_agent_output(output3)

    if parsed3.action is not None:
        raise Exception(f"Should return None for missing action, got: {parsed3.action}")

    print(f"Thought: {parsed3.thought}")
    print(f"Action: {parsed3.action} (correctly None)")
    print("PASSED!\n")

    print("=" * 40)
    print("All parsing tests passed!")
    print("You can now extract structured data from agent outputs.")


if __name__ == "__main__":
    main()

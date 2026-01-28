"""
Concept: Agents (Parsing)
Agents often output unstructured text. You need to parse their output to detect actions.

Task: Use regex to extract the content after "Action: " from the agent's response.
"""

import re

def parse_thought_action(llm_output):
    # Output format: 
    # Thought: I need to search
    # Action: search("query")
    
    # FIX ME: Use regex to extract the Action.
    # match = re.search(r"Action: (.*)", llm_output)
    match = None
    
    if match:
        return match.group(1)
    return None

def main():
    output = "Thought: I should look this up.\nAction: google_search('python')"
    action = parse_thought_action(output)
    
    if action != "google_search('python')":
        raise Exception(f"Failed to parse action. Got: {action}")
        
    print("Action parsed!")

if __name__ == "__main__":
    main()

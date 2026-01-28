"""
Concept: Agents (ReAct Loop)
Agents operate in a loop: Thought -> Action -> Observation -> Repeat.

Task: Implement the `while` loop to allow the agent to keep acting until it is finished.
"""

def run_agent_loop(max_steps=5):
    step = 0
    # FIX ME: Implement a loop that runs until max_steps
    # while step < max_steps:
    #     print(f"Step {step}")
    #     step += 1
    
    if step != max_steps:
        raise Exception("Agent did not run for enough steps!")

if __name__ == "__main__":
    run_agent_loop()

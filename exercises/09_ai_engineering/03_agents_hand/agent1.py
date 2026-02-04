"""
Concept: The Agent Loop (ReAct Pattern)

An AI agent is more than just a single LLM call - it's a system that can:
1. Reason about what to do next (Thought)
2. Take an action using tools (Action)
3. Observe the results (Observation)
4. Repeat until the task is complete

This is called the ReAct (Reasoning + Acting) pattern. The basic structure:

    while not done:
        thought = llm.think(context)      # "I need to search for X"
        action = llm.decide_action()      # "search('X')"
        observation = execute(action)      # Result from search
        context.append(observation)        # Add to history
        done = llm.check_if_done()         # Did we achieve the goal?

Key considerations:
- Max steps: Prevent infinite loops with a step limit
- Stop conditions: Know when the task is complete
- Error handling: What if a tool fails?
- Context management: Keep track of the conversation history

Task: Implement the agent loop that runs until completion or max_steps is reached.
"""

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class AgentState:
    """Tracks the current state of the agent."""

    step: int = 0
    status: Literal["running", "completed", "error"] = "running"
    history: list[str] = field(default_factory=list)


def think(state: AgentState) -> str:
    """Simulate the agent's reasoning step."""
    thoughts = [
        "I need to gather information first.",
        "Let me search for relevant data.",
        "I should verify this information.",
        "Now I can formulate my response.",
        "I have enough information to complete the task.",
    ]
    idx = min(state.step, len(thoughts) - 1)
    return thoughts[idx]


def act(state: AgentState) -> str:
    """Simulate the agent taking an action."""
    actions = [
        "search('initial query')",
        "search('detailed query')",
        "verify('data')",
        "compile_results()",
        "finish()",
    ]
    idx = min(state.step, len(actions) - 1)
    return actions[idx]


def observe(action: str) -> str:
    """Simulate getting a result from an action."""
    return f"Result of {action}: Success"


def is_task_complete(state: AgentState, max_steps: int) -> bool:
    """Check if the agent should stop."""
    # Stop if we've reached max steps
    if state.step >= max_steps:
        return True
    # Stop if the last action was finish()
    if state.history and "finish()" in state.history[-1]:
        state.status = "completed"
        return True
    return False


def run_agent(max_steps: int = 5) -> AgentState:
    """Run the agent loop until completion or max_steps.

    Args:
        max_steps: Maximum number of steps before stopping

    Returns:
        AgentState: Final state of the agent
    """
    state = AgentState()

    # TODO: Implement the agent loop
    # The loop should:
    # 1. Continue while the task is not complete
    # 2. Call think() to get the agent's reasoning
    # 3. Call act() to get the action to take
    # 4. Call observe() to get the result
    # 5. Add the observation to state.history
    # 6. Increment state.step
    # 7. Check is_task_complete() for the loop condition

    # FIX ME: Replace 'pass' with a while loop
    # Hint: while not is_task_complete(state, max_steps):
    #           thought = think(state)
    #           action = act(state)
    #           ...
    pass

    return state


def main():
    print("Running agent loop...")
    print("=" * 50)

    state = run_agent(max_steps=5)

    # Verify the agent ran correctly
    if state.step == 0:
        raise Exception(
            "Agent didn't run any steps!\n"
            "Hint: Implement a while loop that:\n"
            "  - Checks is_task_complete() for the condition\n"
            "  - Calls think(), act(), observe() each iteration\n"
            "  - Increments state.step"
        )

    if state.step < 5:
        raise Exception(
            f"Agent only ran {state.step} steps, expected 5\n"
            "Hint: The loop should continue until is_task_complete() returns True"
        )

    if len(state.history) != 5:
        raise Exception(
            f"Agent history has {len(state.history)} entries, expected 5\n"
            "Hint: Append the observation to state.history each step"
        )

    print(f"\nAgent completed in {state.step} steps")
    print(f"Final status: {state.status}")
    print(f"\nHistory:")
    for i, entry in enumerate(state.history):
        print(f"  Step {i + 1}: {entry}")

    print("\nAgent loop implemented correctly!")


if __name__ == "__main__":
    main()

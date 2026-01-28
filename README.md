# Pylings 🐍

**Pylings** is a hands-on, interactive Python curriculum designed to take you from "Hello World" to "Algorithm Expert". It is inspired by *Rustlings* but expanded to cover deep Computer Science concepts, System Design, and Technical Interview prep.

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- `uv` (recommended) or `pip`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/brayden/pylings.git
   cd pylings
   ```

2. **Install dependencies**:
   ```bash
   # Using uv (fastest)
   uv venv
   source .venv/bin/activate
   uv pip install -e .

   # OR using standard pip
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

## 🎮 How to Play

Pylings works by running small exercises that are initially broken (or incomplete). Your goal is to fix code, implement functions, or pass tests to proceed.

### Exercises (The Learning Path)
Exercises guide you through Python syntax, StdLib, and OOP.

- **List all exercises**:
  ```bash
  pylings list
  ```

- **Run the current/next failing exercise**:
  ```bash
  pylings watch
  ```
  *This will automatically rerun as you save files!*

- **Run a specific exercise**:
  ```bash
  pylings run <exercise_name>
  # Example: pylings run intro1
  ```

### Challenges (HackerRank/LeetCode Style)
Challenges are larger, self-contained algorithmic problems with randomized test suites.

- **List all challenges**:
  ```bash
  pylings challenge list
  ```

- **Run a challenge**:
  ```bash
  pylings challenge run <challenge_name>
  # Example: pylings challenge run two_sum
  ```

## 📚 Curriculum Overview

The curriculum is divided into **15 Phases**, covering over **100 steps**:

### Fundamentals
- **Basics**: Variables, Control Flow, Functions.
- **Data Structures**: Lists, Dicts, Sets, Tuples.
- **OOP**: Classes, Inheritance, Properties, Magic Methods.

### Advanced Python
- **Functional**: Lambdas, Generators, Decorators, Iterators.
- **Metaprogramming**: Context Managers, Decorator Factories.
- **Concurrency**: `asyncio`, `gather`.
- **System**: `pathlib`, `logging`, `argparse`, `os`.

### Computer Science & Algorithms (Challenges)
- **Arrays & Hashing**: Two Sum, Top K Frequent, Group Anagrams.
- **Two Pointers**: Trapping Rain Water, 3Sum.
- **Sliding Window**: Longest Substring which non-repeating chars.
- **Trees**: Invert Tree, Serialize/Deserialize, Tries.
- **Graphs**: Number of Islands, Rotting Oranges, Course Schedule.
- **Dynamic Programming**: Climbing Stairs.
- **Backtracking**: Permutations, Word Search.
- **System Design**: LRU Cache.
- **Greedy & Intervals**: Merge Intervals, Best Time to Buy Stock.

## 🛠 Project Structure

```
pylings/
├── exercises/          # The learning path (broken into topics)
│   ├── 01_intro/
│   ├── ...
│   └── 19_recursion/
├── challenges/         # The algorithmic challenges
│   ├── two_sum/
│   ├── lru_cache/
│   └── ...
├── src/pylings/        # The CLI tool source code
└── info.toml           # Configuration file for exercises
```

## 🧪 Testing

Every challenge includes a `tests.py` file with **Dynamic Randomized Testing**.
- Run 30+ random inputs every time you check your solution.
- Benchmarks performance (e.g., ensures O(n) vs O(n^2)).

---
*Happy Coding!*

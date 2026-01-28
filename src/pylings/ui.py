from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from .model import Exercise
from .checker import CheckResult

console = Console()

def show_exercise_header(exercise: Exercise):
    console.print(Panel(f"[bold blue]Running {exercise.name}[/bold blue]", expand=False))

def show_success(exercise: Exercise, output: str):
    console.print(f"[bold green]✓ {exercise.name} passed![/bold green]")
    if output:
        console.print(Panel(output, title="Output", border_style="green"))

def show_failure(exercise: Exercise, result: CheckResult):
    console.print(f"[bold red]✗ {exercise.name} failed[/bold red]")
    if result.output:
        console.print(Panel(result.output, title="Output", border_style="red"))
    if result.error:
        console.print(Panel(result.error, title="Error", border_style="red"))
    
    console.print("\n[bold yellow]Hint:[/bold yellow]")
    console.print(exercise.hint or "No hint available.")

def show_list(exercises):
    for ex in exercises:
        console.print(f"- {ex.name} ({ex.path})")

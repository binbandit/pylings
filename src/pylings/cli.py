import typer
from typing import Optional
from pathlib import Path
from .config import Config
from .checker import Checker
from .ui import show_exercise_header, show_success, show_failure, show_list, console
from .watcher import Watcher

app = typer.Typer(name="pylings", help="Python exercises runner")
challenge_app = typer.Typer(name="challenge", help="coding challenges")
app.add_typer(challenge_app, name="challenge")

from .challenge_runner import ChallengeRunner

@challenge_app.command("list")
def list_challenges():
    """List available challenges"""
    challenges_dir = Path("challenges")
    if not challenges_dir.exists():
        console.print("[yellow]No challenges directory found.[/yellow]")
        return
        
    for item in challenges_dir.iterdir():
        if item.is_dir():
            console.print(f"[bold cyan]{item.name}[/bold cyan]")

@challenge_app.command("run")
def run_challenge(name: str):
    """Run a specific challenge"""
    challenge_dir = Path("challenges") / name
    if not challenge_dir.exists():
        console.print(f"[red]Challenge '{name}' not found[/red]")
        raise typer.Exit(code=1)
        
    runner = ChallengeRunner(challenge_dir)
    console.print(f"[bold]Running Challenge: {name}[/bold]")
    
    results = runner.run()
    
    all_passed = True
    for res in results:
        status = "[green]PASS[/green]" if res.passed else "[red]FAIL[/red]"
        console.print(f"{status} {res.name}: {res.message} [dim]({res.duration:.4f}s)[/dim]")
        if not res.passed:
            all_passed = False
            
    if all_passed:
        console.print("\n[bold green]ALL TESTS PASSED! \u2728[/bold green]")
    else:
        console.print("\n[bold red]SOME TESTS FAILED[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def list():
    """List all exercises"""
    config = Config.load()
    show_list(config.exercises)

@app.command()
def verify(name: Optional[str] = typer.Argument(None)):
    """Verify all exercises or a specific one"""
    config = Config.load()
    
    if name:
        exercises = [ex for ex in config.exercises if ex.name == name]
        if not exercises:
            console.print(f"[red]Exercise '{name}' not found[/red]")
            raise typer.Exit(code=1)
    else:
        exercises = config.exercises

    for exercise in exercises:
        show_exercise_header(exercise)
        result = Checker.run_exercise(exercise)
        if result.success:
            show_success(exercise, result.output)
        else:
            show_failure(exercise, result)
            raise typer.Exit(code=1)

@app.command()
def hint(name: str):
    """Show hint for a specific exercise"""
    config = Config.load()
    exercise = next((ex for ex in config.exercises if ex.name == name), None)
    
    if exercise:
        console.print(f"[bold yellow]Hint for {name}:[/bold yellow]")
        console.print(exercise.hint)
    else:
        console.print(f"[red]Exercise '{name}' not found[/red]")

def on_file_change(path):
    # Ideally, we would find which exercise this file belongs to and run it.
    # For now, let's just re-run verify for everything or smarter logic.
    # To keep it simple for MVP, we clear screen and run verify all.
    console.clear()
    console.print(f"[dim]File changed: {path}[/dim]")
    try:
        verify()
    except typer.Exit:
        pass # verify raises Exit on failure, we want to keep watching

@app.command()
def watch():
    """Watch for file changes and run exercises"""
    console.print("[bold green]Starting Pylings Watcher...[/bold green]")
    verify() # Run once initially
    
    # Watch the exercises directory
    # Assuming exercises are in the root 'exercises' folder relative to CWD
    exercises_path = "exercises" 
    watcher = Watcher(exercises_path, on_file_change)
    watcher.start()

if __name__ == "__main__":
    app()

import typer
from typing import Optional, Tuple
from pathlib import Path
from .config import Config
from .checker import Checker, CheckResult
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
        console.print(
            f"{status} {res.name}: {res.message} [dim]({res.duration:.4f}s)[/dim]"
        )
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

    for i, exercise in enumerate(exercises):
        result = Checker.run_exercise(exercise)
        if result.success:
            # Exercise passed, continue to next
            continue
        else:
            # Found failing exercise - show it and stop
            show_exercise_header(exercise)
            show_failure(exercise, result)
            console.print(
                f"\n[dim]Progress: {i}/{len(exercises)} exercises completed[/dim]"
            )
            raise typer.Exit(code=1)

    # All exercises passed!
    console.print(
        f"\n[bold green]All {len(exercises)} exercises completed![/bold green]"
    )
    console.print("[bold]You've finished all the exercises. Great job![/bold]")


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


def find_current_exercise(config: Config) -> Tuple[int, Optional[CheckResult]]:
    """Find the first failing exercise and return its index and result.

    Returns (index, result) where:
    - If all pass: (len(exercises), None)
    - If one fails: (failing_index, CheckResult)
    """
    for i, exercise in enumerate(config.exercises):
        result = Checker.run_exercise(exercise)
        if not result.success:
            return i, result
    return len(config.exercises), None  # All done


def run_watch_cycle():
    """Run a single watch cycle - find and display current exercise status."""
    config = Config.load()
    idx, result = find_current_exercise(config)

    if result is None:
        # All exercises completed!
        console.print(
            f"\n[bold green]All {len(config.exercises)} exercises completed![/bold green]"
        )
        console.print("[bold]You've finished all the exercises. Great job![/bold]")
        return True  # All done

    # Show the current failing exercise
    exercise = config.exercises[idx]
    show_exercise_header(exercise)
    show_failure(exercise, result)
    console.print(
        f"\n[dim]Progress: {idx}/{len(config.exercises)} exercises completed[/dim]"
    )
    return False  # More to do


def on_file_change(path):
    """Handle file changes - recheck exercises and show progress."""
    console.clear()
    console.print(f"[dim]File changed: {path}[/dim]\n")

    # Check if the previously failing exercise now passes
    config = Config.load()
    old_idx, _ = find_current_exercise(config)

    # Re-run to get current state
    config = Config.load()  # Reload in case file changed
    new_idx, result = find_current_exercise(config)

    if new_idx > old_idx:
        # Made progress! Show success for completed exercises
        for i in range(old_idx, new_idx):
            completed = config.exercises[i]
            show_success(completed, "")

    if result is None:
        # All done!
        console.print(
            f"\n[bold green]All {len(config.exercises)} exercises completed![/bold green]"
        )
        console.print("[bold]You've finished all the exercises. Great job![/bold]")
    else:
        # Show the current failing exercise
        exercise = config.exercises[new_idx]
        show_exercise_header(exercise)
        show_failure(exercise, result)
        console.print(
            f"\n[dim]Progress: {new_idx}/{len(config.exercises)} exercises completed[/dim]"
        )


@app.command()
def watch():
    """Watch for file changes and run exercises"""
    console.print("[bold green]Starting Pylings Watcher...[/bold green]")
    console.print("[dim]Watching for file changes... (Ctrl+C to exit)[/dim]\n")

    # Run initial check
    all_done = run_watch_cycle()
    if all_done:
        return

    # Watch the exercises directory
    exercises_path = "exercises"
    watcher = Watcher(exercises_path, on_file_change)
    watcher.start()


if __name__ == "__main__":
    app()

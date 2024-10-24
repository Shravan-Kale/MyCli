import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print
from rich.text import Text

console = Console()

def get_test(input_str: str, display_str: str, end_str: str) -> str:
    # Get the test string
    return str(Text.assemble((input_str, "bold underline green"), (display_str, "bold blue"), (end_str, "bold red")))

def display_app_name():
    # Display the app name in a panel

    app_name = "My Awesome CLI App"
    console.print(Panel(Text(app_name,justify="center"), title="[bold magenta]Welcome[/bold magenta]", title_align="center", border_style="green", style="bold cyan"))


def get_user_details():
    # Ask for user details with fancy prompts
    name = Prompt.ask("[bold green]What's your [underline]name[/underline]?[/bold green]", default="Guest")
    age = Prompt.ask("[bold blue]How [underline]old[/underline] are you?[/bold blue]", default="25")
    dis = Prompt.ask(get_test("What is the test string?", "What is the display string? 🏃 ", "What is the end string?"), default="My Default String")
    typer.prompt(get_test("What is the test string?", "What is the display string? 🏃 ", "What is the end string?"), default="My Default String")
    # Choices for favorite color
    favorite_color = Prompt.ask(
        "[bold magenta]Pick your [underline]favorite color[/underline]:[/bold magenta]",
        choices=["Red", "Green", "Blue", "Yellow"],
        default="Blue"
    )

    # Display a summary of user inputs
    console.print(f"\n[bold yellow]Hello, [green]{name}[/green]![/bold yellow] :wave:")
    console.print(
        f"[bold yellow]You are [blue]{age}[/blue] years old and your favorite color is [magenta]{favorite_color}[/magenta].[/bold yellow] :star_struck:")


def main():
    display_app_name()
    get_user_details()


if __name__ == "__main__":
    main()

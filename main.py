import os
import time
from llama_cpp import Llama
from rich.console import Console
from rich.prompt import Prompt

# UI Setup
console = Console()

def list_models(directory="models"):
    """Lists available GGUF models in the models directory."""
    models = [f for f in os.listdir(directory) if f.endswith(".gguf")]
    return models

def select_model():
    """Allows the user to select a model from the available GGUF files."""
    models = list_models()
    
    if not models:
        console.print("[bold red]No GGUF models found in the 'models/' folder![/bold red]")
        exit(1)

    console.print("\n[bold cyan]Available Models:[/bold cyan]\n")
    for idx, model in enumerate(models, 1):
        console.print(f"[bold yellow]{idx}.[/bold yellow] {model}")

    while True:
        try:
            choice = int(Prompt.ask("\n[bold cyan]Select a model (1-{0})[/bold cyan]".format(len(models))))
            if 1 <= choice <= len(models):
                return os.path.join("models", models[choice - 1])
            else:
                console.print("[bold red]Invalid selection! Please choose a valid number.[/bold red]")
        except ValueError:
            console.print("[bold red]Please enter a valid number.[/bold red]")

# Model Selection
console.print("[bold cyan]Scanning for models...[/bold cyan]")
model_path = select_model()
console.print(f"[bold green]Selected Model: {model_path}[/bold green]")

# Load the selected model
console.print("[bold cyan]Loading model... This may take a while.[/bold cyan]")
llm = Llama(
    model_path=model_path, 
    n_ctx=4096,
    n_threads=12,  # Adjust based on your CPU
    n_batch=512,  # Process multiple tokens at once
    top_p=0.9,
    verbose=False # Suppress unnecessary logging
)
console.print("[bold green]Model loaded successfully![/bold green]\n")

def chat():
    """Interactive chat loop with token statistics summary after generation."""
    console.print("[bold yellow]Welcome! Type 'exit' to quit.[/bold yellow]")

    while True:
        user_input = Prompt.ask("\n[bold cyan]You[/bold cyan]")
        if user_input.lower() in ["exit", "quit"]:
            console.print("\n[bold red]Exiting chat. Goodbye![/bold red]")
            break
        
        console.print("[bold magenta]Thinking...[/bold magenta]")

        response = []
        token_count = 0
        start_time = time.time()  # Start timing

        # Streamed generation
        for token in llm(
            user_input,
            max_tokens=4096,  # Allow for longer responses
            temperature=0.7,
            top_p=0.9,
            stream=True
        ):
            text = token["choices"][0]["text"]
            response.append(text)
            console.print(text, end="", style="bold green", highlight=False)
            token_count += 1

        end_time = time.time()  # Stop timing
        elapsed_time = end_time - start_time

        # Calculate tokens per second
        tokens_per_second = token_count / elapsed_time if elapsed_time > 0 else 0

        # Print the summary after full response generation
        console.print(f"\n\n[white]Total Tokens Generated:[/white] [bold cyan]{token_count}[/bold cyan]")
        console.print(f"[white]Average Tokens per Second:[/white] [bold cyan]{tokens_per_second:.2f}[/bold cyan]\n")

# Start Chat
chat()

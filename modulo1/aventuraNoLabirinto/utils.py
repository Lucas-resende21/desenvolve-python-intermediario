"""Utilitários de interface e formatação Rich."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def imprime_menu():
    """Exibe o menu inicial estilizado."""
    table = Table(title="Aventura no Labirinto")
    table.add_column("Opção", justify="center", style="cyan")
    table.add_column("Ação", style="magenta")
    table.add_row("1", "Jogar Manualmente")
    table.add_row("2", "Assistir Solução (Recursiva)")
    table.add_row("3", "Instruções")
    table.add_row("4", "Sair")
    console.print(table)

def vitoria_recursiva(n=3):
    """Função Recursiva: Animação de vitória simples."""
    if n == 0:
        return
    console.print("[bold yellow]!!! VOCÊ VENCEU !!![/bold yellow]")
    vitoria_recursiva(n-1)
import argparse
import time
from rich.live import Live
from aventura_pkg import labirinto, jogador, utils
from pynput import keyboard

def jogar(args, modo_auto=False):
    lab = labirinto.criar_labirinto(10, 10)
    player = jogador.Jogador(args.nome, args.color)
    
    if modo_auto:
        solucao = labirinto.encontrar_caminho_recursivo(lab, 0, 0, (9, 9), [])
        for passo in solucao:
            player.pos = list(passo)
            # Lógica de renderização aqui com Live do Rich...
            time.sleep(0.2)
    else:
        # Loop com pynput.keyboard.Listener...
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Labirinto CLI")
    parser.add_argument("nome", help="Nome do herói")
    parser.add_argument("--color", default="blue", help="Cor do jogador")
    parser.add_argument("--dificuldade", type=int, choices=[1, 2, 3], default=1)
    parser.add_argument("--mute", action="store_true", help="Desativa sons")
    args = parser.parse_args()

    utils.imprime_menu()
    escolha = input("Selecione: ")
    
    match escolha:
        case "1": jogar(args)
        case "2": jogar(args, modo_auto=True)
        case "3": console.print(Panel("Use as setas para mover!"))
        case "4": exit()
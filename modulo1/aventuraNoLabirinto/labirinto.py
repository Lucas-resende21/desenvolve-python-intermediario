"""Módulo responsável pela geração e exibição do cenário do labirinto."""
import random

def criar_labirinto(largura=10, altura=10):
    """
    Gera um labirinto aleatório como uma lista de listas.
    0 = Caminho, 1 = Parede, 2 = Item.
    """
    lab = [[1 if random.random() < 0.25 else 0 for _ in range(largura)] for _ in range(altura)]
    # Garantir entrada e saída livres
    lab[0][0] = 0
    lab[altura-1][largura-1] = 0
    # Adicionar itens aleatórios
    for _ in range(3):
        ry, rx = random.randint(0, altura-1), random.randint(0, largura-1)
        if lab[ry][rx] == 0: lab[ry][rx] = 2
    return lab

def encontrar_caminho_recursivo(lab, y, x, destino, caminho_atual):
    """
    Função Recursiva: Resolve o labirinto usando Backtracking.
    Retorna a lista de coordenadas do caminho até o destino.
    """
    if (y, x) == destino:
        return caminho_atual + [(y, x)]
    
    if not (0 <= y < len(lab) and 0 <= x < len(lab[0])) or lab[y][x] == 1 or (y, x) in caminho_atual:
        return None

    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        res = encontrar_caminho_recursivo(lab, y + dy, x + dx, destino, caminho_atual + [(y, x)])
        if res: return res
    return None
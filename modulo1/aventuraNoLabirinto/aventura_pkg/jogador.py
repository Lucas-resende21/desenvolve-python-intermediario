"""Módulo de controle do jogador e mecânicas de movimento."""
from pynput import keyboard

class Jogador:
    def __init__(self, nome, cor="blue"):
        self.nome = nome
        self.cor = cor
        self.pos = [0, 0]
        self.pontos = 0

    def mover(self, tecla, lab):
        """Atualiza a posição baseada na entrada do teclado."""
        y, x = self.pos
        nova_pos = [y, x]
        
        match tecla:
            case keyboard.Key.up:    nova_pos[0] -= 1
            case keyboard.Key.down:  nova_pos[0] += 1
            case keyboard.Key.left:  nova_pos[1] -= 1
            case keyboard.Key.right: nova_pos[1] += 1
            
        ny, nx = nova_pos
        if 0 <= ny < len(lab) and 0 <= nx < len(lab[0]) and lab[ny][nx] != 1:
            if lab[ny][nx] == 2: # Coletou item
                self.pontos += 10
                lab[ny][nx] = 0
            self.pos = nova_pos
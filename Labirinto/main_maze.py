# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

def resolver_labirinto(maze: Maze) -> bool:
    """Resolve o labirinto usando backtracking com pilha explícita."""
    visitado = set()
    pilha = deque()

    pos_inicial = maze.get_init_pos_player()
    pilha.append(pos_inicial)

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pilha:
        x, y = pilha.pop()

        if (x, y) in visitado:
            continue
        visitado.add((x, y))

        if maze.find_prize((x, y)):
            maze.mov_player((x, y))
            return True

        maze.mov_player((x, y))
        time.sleep(0.05)

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if maze.is_free((nx, ny)) and (nx, ny) not in visitado:
                pilha.append((nx, ny))

    return False

# Execução principal
maze_csv_path = "labirinto1.txt"
maze = Maze()
maze.load_from_csv(maze_csv_path)
maze.run()
maze.init_player()

achou = resolver_labirinto(maze)
print("Tesouro encontrado!" if achou else "Tesouro não encontrado.")

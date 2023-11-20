# DFS
import time
from datetime import datetime
from queue import LifoQueue

from GameState import GameState
from constant.sound import *
from constant.image import *
from common import reconstruct_path, WIN
from GUI import draw


def DFS(board, start, end):
    GameState.start_time = time.time()
    stack = LifoQueue()
    came_from = {}
    stack.put(start)
    visited = {start}
    while not stack.empty():
        # pygame.time.wait(200)
        # pygame.mixer.Sound(swimmingSound).play()
        current = stack.get()
        if current == end:
            current.setImage(finishLineImg)
            GameState.last_time = time.time()
            reconstruct_path(came_from, start, end, board, "DFS")
            return True

        if current != start:
            current.make_closed()
        for neighbour in current.neighbour:
            if neighbour not in visited:
                stack.put(neighbour)
                visited.add(neighbour)
                came_from[neighbour] = current
                if neighbour != end:
                    neighbour.make_open()

        draw(WIN, board, ROWS, WIDTH)
    return False
# END DFS

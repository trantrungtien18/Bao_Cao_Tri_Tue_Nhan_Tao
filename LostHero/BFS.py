import time
from datetime import datetime
from queue import Queue

from GameState import GameState
from constant.sound import *
from constant.image import *
from common import reconstruct_path, WIN
from GUI import draw
# BFS
def BFS(board,start,end):
    GameState.start_time = time.time()
    queue = Queue()
    queue.put(start)
    visited = {start}
    came_from = {}
    while not queue.empty():
        # pygame.mixer.Sound(swimmingSound).play()
        current = queue.get()
        if current == end:
            current.setImage(finishLineImg)
            GameState.last_time = time.time()
            reconstruct_path(came_from,start,end,board, "BFS")
            return True

        if current != start:
            current.make_closed()
        for neighbour in current.neighbour:
            if neighbour not in visited:
                queue.put(neighbour)
                visited.add(neighbour)
                came_from[neighbour] = current
                if neighbour != end:
                    neighbour.make_open()
        draw(WIN,board,ROWS,WIDTH)
    return False
# END BFS
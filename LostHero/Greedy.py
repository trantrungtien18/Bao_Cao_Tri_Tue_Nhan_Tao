from queue import LifoQueue
from common import *


def Greedy(board, start, end):
    GameState.start_time = time.time()
    stack = LifoQueue()
    came_from = {}
    stack.put(start)
    visited = {start}
    while not stack.empty():
        current = stack.get()
        if current == end:
            current.setImage(finishLineImg)
            GameState.last_time = time.time()
            reconstruct_path(came_from, start, end, board, "Greedy")
            return True

        if current != start:
            current.make_closed()

        sorted_neighbour = sorted(current.neighbour, key=lambda x: get_score(x.get_pos(), end.get_pos()), reverse=True)

        print([get_score(x.get_pos(), end.get_pos()) for x in sorted_neighbour])

        for neighbour in sorted_neighbour:
            if neighbour not in visited:
                stack.put(neighbour)
                visited.add(neighbour)
                came_from[neighbour] = current
                if neighbour != end:
                    neighbour.make_open()

        draw(WIN, board, ROWS, WIDTH)
    return False


def get_score(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return ((r1 - r2) ** 2 + (c1 - c2) ** 2) ** 1 / 2

import pygame
from constant.sound import *
from GUI import draw
from common import reconstruct_path, WIN
from constant.dimension import *


# DIJKSTRA
def Dijkstra(board, start, end):
    if (not start) or (not end):
        return False
    came_from = {}
    start.distance = 0
    unvisited = {cell for row in board for cell in row}
    while len(unvisited) > 0:
        pygame.time.wait(200)
        pygame.mixer.Sound(swimmingSound).play()
        unvisited = sort_set_by_distance(unvisited)
        closestNode = next(iter(unvisited))
        unvisited.remove(closestNode)
        if closestNode != start and closestNode != end:
            closestNode.make_closed()
        if closestNode == end:
            reconstruct_path(came_from, start, end, board)
            return True
        for neighbour in closestNode.neighbour:
            alt = closestNode.distance + 1
            if alt < neighbour.distance:
                neighbour.distance = alt
                came_from[neighbour] = closestNode
                if neighbour != end:
                    neighbour.make_open()
        draw(WIN, board, ROWS, WIDTH)


def sort_set_by_distance(set):
    set = sorted(set, key=lambda x: x.distance)
    return set
# END DIJKSTRA

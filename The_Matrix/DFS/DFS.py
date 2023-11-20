from pyamaze import maze, agent, COLOR, textLabel
import random as rand
from pygame.locals import *
import time

x = rand.randint(10, 20)
y = rand.randint(10, 20)


def DFS(m, x, y):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}

    goal = (x, y)  # Goal node

    while goal != start:
        fwdPath[dfsPath[goal]] = goal
        goal = dfsPath[goal]
    return fwdPath


def runGame():
    if __name__ == '__main__':
        m = maze(x, y)
        x1 = rand.randint(x//10, x % 10)
        y1 = rand.randint(y//10, y % 10)

        m.CreateMaze(x1, y1, loopPercent=40)

        gameStart = time.time()
        path = DFS(m, x1, y1)
        gameEnd = time.time()

        runningGame = gameEnd - gameStart
        timeStamp = str(runningGame) + " millisecond"

        a = agent(m, footprints=True)
        m.tracePath({a: path})
        l = textLabel(m, 'Length of Shortest Path', len(path)+1)
        l2 = textLabel(m, 'Time Stamp', timeStamp)
        print(timeStamp)
        m.run()


runGame()

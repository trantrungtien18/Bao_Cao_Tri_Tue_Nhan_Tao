from pyamaze import maze, agent, COLOR, textLabel
import random as rand
from pygame.locals import *
import time

x = rand.randint(10, 20)
y = rand.randint(10, 20)


def BFS(m, y, x):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfsPath = {}
    while len(frontier) > 0:
        currGoal = frontier.pop(0)
        if currGoal == (1, 1):
            break
        for d in 'ESNW':
            # Kiem tra gia tri cua m.maze_map tai vi tri currGoal : loc du lieu ESNW lay ra gia tri nao = 1 trong dãy m.maze_map[currGoal][d]
            if m.maze_map[currGoal][d] == True:
                if d == 'E':
                    childgoal = (currGoal[0], currGoal[1]+1)
                elif d == 'W':
                    childgoal = (currGoal[0], currGoal[1]-1)
                elif d == 'N':
                    childgoal = (currGoal[0]-1, currGoal[1])
                elif d == 'S':
                    childgoal = (currGoal[0]+1, currGoal[1])
                if childgoal in explored:
                    continue
                frontier.append(childgoal)
                explored.append(childgoal)
                bfsPath[childgoal] = currGoal
    fwdPath = {}

    goal = (y, x)  # Goal node

    while goal != start:
        fwdPath[bfsPath[goal]] = goal
        goal = bfsPath[goal]
    return fwdPath


def runGame():
    if __name__ == '__main__':
        m = maze(x, y)
        y1 = rand.randint(0, m.cols-1)
        x1 = rand.randint(0, m.rows-1)

        m.CreateMaze(y1, x1, loopPercent=40)

        gameStart = time.time()
        path = BFS(m, y1, x1)
        gameEnd = time.time()

        runningTime = gameEnd - gameStart
        timeStamp = str(runningTime) + " millisecond"

        a = agent(m, footprints=True)
        m.tracePath({a: path})
        l = textLabel(m, 'Length of Shortest Path', len(path)+1)
        l2 = textLabel(m, 'Time Stamp', timeStamp)
        # print(timeStamp)
        m.run()


runGame()

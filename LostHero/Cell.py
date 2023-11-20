from constant.image import *
from constant.color import *


class Cell:
    def __init__(self, row, col, width, total_rows, image=None):
        self.is_player = False
        self.image = image;
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.color = None
        self.x = row * width
        self.y = col * width
        self.player_pos = (self.x - self.width // 2, self.y - self.width // 2)
        self.neighbour = []
        self.distance = float("inf")  # for dijkstra algorithm

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == LIGHTORANGE

    def is_player(self):
        return self.is_player

    def is_open(self):
        return self.color == LIGHTYELLOW

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == BLUE

    def is_end(self):
        return self.image == finishLineImg

    def is_path(self):
        return self.color == GREEN

    def reset(self):
        self.color = None
        self.image = waterImg
        self.is_player = False
        self.neighbour = []

    def setImage(self, image):
        self.image = image

    def make_start(self):
        self.image = startImg
        self.color = BLUE

    def make_closed(self):
        self.color = LIGHTORANGE

    def make_open(self):
        self.color = LIGHTYELLOW
        # self.image = flagImg

    def make_barrier(self):
        self.color = BLACK
        self.image = grassImg

    def make_end(self):
        self.color = BLUE
        self.image = finishLineImg

    def make_path(self):
        self.is_player = False
        self.color = GREEN
        self.image = landImg

    def make_player(self, value):
        self.is_player = value

    def draw(self, win):
        win.blit(waterImg, (self.x, self.y))
        if self.is_player:
            win.blit(self.image, self.player_pos)
            return
        if self.image:
            win.blit(self.image, (self.x, self.y))
            return

    def update_neighbor(self, board):
        if self.row < self.total_rows - 1 and not board[self.row + 1][self.col].is_barrier():
            self.neighbour.append(board[self.row + 1][self.col])
        if self.row > 0 and not board[self.row - 1][self.col].is_barrier():
            self.neighbour.append(board[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not board[self.row][self.col + 1].is_barrier():
            self.neighbour.append(board[self.row][self.col + 1])
        if self.col > 0 and not board[self.row][self.col - 1].is_barrier():
            self.neighbour.append(board[self.row][self.col - 1])

    def __lt__(self, other):
        return False

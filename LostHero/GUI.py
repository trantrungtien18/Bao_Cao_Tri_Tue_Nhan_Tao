import pygame

from GameState import GameState
from constant.color import *
from constant.dimension import *


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:  # Draw ouline
            pygame.draw.rect(win, outline, (self.x - 2, self.y -
                             2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y,
                         self.width, self.height), 0)
        if self.text != "":
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, True, BLACK)
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class Text:
    def __init__(self, text, x, y, size, color=BLACK):
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, win):
        font = pygame.font.SysFont('comicsans', self.size)
        text = font.render(self.text, True, self.color)
        win.blit(text, (self.x, self.y))


# MAKING BUTTONS:
y = 50
gap = 60
height = 40
High_Score = Text(
    f'High Score: {GameState.high_score} ({GameState.high_score_label})', WIDTH + 30, y, 20)
y += gap
Last_Time_Button = Button(GREEN, WIDTH + 40, y, 120, height, "Last Time: 0")
y += gap
Gold_Button = Button(GREEN, WIDTH + 40, y, 120, height, "Gold: 0")
y += gap
Heart_Button = Button(RED, WIDTH + 40, y, 120, height, "Heart: 0")
y += gap
Start_Button = Button(BLUE, WIDTH + 40, y, 120, height, "Start")
y += gap
End_Button = Button(BLUE, WIDTH + 40, y, 120, height, "End")
y += gap
A_Star_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "A*")
y += gap
Dijkstra_button = Button(YELLOW, WIDTH + 40, y, 120, height, "DIJKSTRA")
y += gap
Greedy_button = Button(YELLOW, WIDTH + 40, y, 120, height, "Greedy search")
y += gap
BFS_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "BFS")
y += gap
DFS_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "DFS")
y += gap
Clear_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Clear")
y += gap
Random_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Random")


# END MAKING BUTTONS


def draw_grid(win, rows, total_width):
    width = total_width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * width), (total_width, i * width))
        for j in range(rows + 1):
            pygame.draw.line(win, BLACK, (j * width, 0),
                             (j * width, total_width))


def draw_button(win, button: Button, outline_color=BLACK):
    button.draw(win, outline_color)


def draw(win, board, rows, total_width):
    win.fill(WHITE)
    # Draw menu
    pygame.draw.rect(win, WHITE, (WIDTH, 0, MENU_WIDTH, WIDTH), 0)

    High_Score.draw(win)
    draw_button(win, Last_Time_Button)
    draw_button(win, Gold_Button)
    draw_button(win, Heart_Button)
    draw_button(win, Start_Button)
    draw_button(win, End_Button)
    draw_button(win, A_Star_Button)
    draw_button(win, Greedy_button)
    draw_button(win, BFS_Button)
    draw_button(win, DFS_Button)
    draw_button(win, Clear_Button)
    draw_button(win, Random_Button)
    draw_button(win, Dijkstra_button)

    player_cell = None
    for row in board:
        for cell in row:
            if cell.is_player:
                player_cell = cell
            cell.draw(win)
    if player_cell:
        player_cell.draw(win)
    pygame.display.update()

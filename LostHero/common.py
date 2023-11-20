import datetime
import time

from GameState import GameState
from constant.sound import winSound
from GUI import draw
from constant.image import *

DELAY = 3
SPEED = 5


def move_to(start, dest, board):
    start.make_player(False)

    # Di chuyển theo trục x
    if start.x > dest.x:
        x = start.x
        while x > dest.x:
            for frame in range(15):
                dest.setImage(get_player_image(player_left, frame))
                pygame.time.delay(DELAY)
                x -= SPEED
                dest.player_pos = (x, dest.player_pos[1])
                draw(WIN, board, ROWS, WIDTH)

        dest.make_path()
    elif start.x < dest.x:
        x = start.x
        while x < dest.x:
            for frame in range(15):
                dest.setImage(get_player_image(player_right, frame))
                pygame.time.delay(DELAY)
                x += SPEED
                dest.player_pos = (x, dest.player_pos[1])
                draw(WIN, board, ROWS, WIDTH)
        dest.make_path()

    # Di chuyển theo trục y
    elif start.y > dest.y:
        y = start.y
        while y > dest.y:
            for frame in range(15):
                dest.setImage(get_player_image(player_back, frame))
                pygame.time.delay(DELAY)
                y -= SPEED
                dest.player_pos = (dest.player_pos[0], y - 20)
                draw(WIN, board, ROWS, WIDTH)
        dest.make_path()
    elif start.y < dest.y:
        y = start.y
        while y < dest.y:
            for frame in range(15):
                dest.setImage(get_player_image(player_front, frame))
                pygame.time.delay(DELAY)
                y += SPEED
                dest.player_pos = (dest.player_pos[0], y)
                draw(WIN, board, ROWS, WIDTH)
        dest.make_path()


def reconstruct_path(came_from, start, end, board, algo):
    current_time = time.time()

    GameState.last_time = round(
        (current_time - GameState.start_time) * 1000, 1)
    print(GameState.last_time)

    # Tạo danh sách để lưu giá trị các ô đã đi qua
    current = end
    stack = []

    end.make_player(False)  # Đặt trạng thái cho ô tại vị trí đích là ...

    # Xây dựng danh sách các vị trí để từ vị trí came_from đến start
    while came_from[current] != start:
        current = came_from[current]
        if current != end:
            stack.append(current)

    # Di chuyển đối tượng từ ô trước đó tới ô hiện tại trong danh sách và vẽ ra bảng
    prev = start
    while len(stack) > 0:
        current = stack.pop()
        current.make_player(True)
        move_to(prev, current, board)
        draw(WIN, board, ROWS, WIDTH)
        prev = current
        prev.make_player(False)
        prev.make_path()

    # Xóa hình ảnh của ô trước đó 
    prev.setImage(None)
    prev.make_path()
    prev.make_player(False)
    end.make_player(True)
    end.setImage(player_idle_image)
    draw(WIN, board, ROWS, WIDTH)

    pygame.mixer.Sound.play(winSound)
    new_score = 10000 // GameState.last_time

    if new_score > GameState.high_score:
        GameState.high_score = new_score
        GameState.high_score_label = algo

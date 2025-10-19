import os
import time
import random
import ctypes
from enum import StrEnum, IntEnum
from ctypes import wintypes

# Virtual key codes for snake movement
VK_UP = 0x26
VK_DOWN = 0x28
VK_LEFT = 0x25
VK_RIGHT = 0x27

# Initialize user32 library for Windows API interaction
user32 = ctypes.WinDLL("user32")
GetAsyncKeyState = user32.GetAsyncKeyState
GetAsyncKeyState.argtypes = [wintypes.INT]
GetAsyncKeyState.restype = wintypes.WORD


# Utility functions
def clear_console():
    os.system("cls")

def is_key_pressed(vk_code: int) -> bool:
    return GetAsyncKeyState(vk_code) & 0x8000 != 0


# Game data models
class SnakeEvent(IntEnum):
    SPACE = 0
    WALL = 1
    PLAYER_HEAD = 2
    PLAYER_BODY = 3
    FOOD = 4

class SnakeSymbol(StrEnum):
    SPACE = " "
    WALL = "#"
    PLAYER_HEAD = "●"
    PLAYER_BODY = "○"
    FOOD = "•"

class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    def __init__(self, size: int):
        self.size = size
        self.field = [[SnakeEvent.SPACE for _ in range(size)] for _ in range(size)]
        
        for i in range(size):
            self.field[0][i] = SnakeEvent.WALL
            self.field[size - 1][i] = SnakeEvent.WALL
            self.field[i][0] = SnakeEvent.WALL
            self.field[i][size - 1] = SnakeEvent.WALL
        
        self.snake = [(size // 2, size // 2)]
        self.field[size // 2][size // 2] = SnakeEvent.PLAYER_HEAD

        self.fps_loop   = 1/30 # 30 FPS
        self.fps_render = 1/6  # 6 FPS
        
        self.score = 0
        self.game_over = False
        self.direction = Direction.RIGHT

        self.last_input = time.perf_counter()
        self.last_render = time.perf_counter()
        
        self.spawn_food()
    

    def spawn_food(self):
        empty_cells = []
        for x in range(self.size):
            for y in range(self.size):
                if self.field[x][y] == SnakeEvent.SPACE:
                    empty_cells.append((x, y))
        
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.field[x][y] = SnakeEvent.FOOD
    

    def handle_input(self):
        if is_key_pressed(VK_UP) and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif is_key_pressed(VK_DOWN) and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif is_key_pressed(VK_LEFT) and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif is_key_pressed(VK_RIGHT) and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
    

    def update(self):
        head_x, head_y = self.snake[0]
        
        if self.direction == Direction.UP:
            new_head = (head_x - 1, head_y)
        elif self.direction == Direction.DOWN:
            new_head = (head_x + 1, head_y)
        elif self.direction == Direction.LEFT:
            new_head = (head_x, head_y - 1)
        else: # RIGHT
            new_head = (head_x, head_y + 1)
        
        new_head_x, new_head_y = new_head
        
        if (self.field[new_head_x][new_head_y] == SnakeEvent.WALL or 
            self.field[new_head_x][new_head_y] == SnakeEvent.PLAYER_BODY):
            self.game_over = True
            return
        
        eat_food = self.field[new_head_x][new_head_y] == SnakeEvent.FOOD
        
        self.snake.insert(0, new_head)

        self.field[head_x][head_y] = SnakeEvent.PLAYER_BODY
        self.field[new_head_x][new_head_y] = SnakeEvent.PLAYER_HEAD
        
        if not eat_food:
            tail_x, tail_y = self.snake.pop()
            self.field[tail_x][tail_y] = SnakeEvent.SPACE
        else:
            self.score += 1
            self.spawn_food()
    

    def render(self):
        clear_console()
        print(f"Score: {self.score}")
        
        for row in self.field:
            line = ""
            for cell in row:
                if cell == SnakeEvent.SPACE:
                    line += SnakeSymbol.SPACE
                elif cell == SnakeEvent.WALL:
                    line += SnakeSymbol.WALL
                elif cell == SnakeEvent.PLAYER_HEAD:
                    line += SnakeSymbol.PLAYER_HEAD
                elif cell == SnakeEvent.PLAYER_BODY:
                    line += SnakeSymbol.PLAYER_BODY
                elif cell == SnakeEvent.FOOD:
                    line += SnakeSymbol.FOOD
            print(line)
        
        if self.game_over:
            print(f"Game Over! Your score: {self.score}")
        

    def run(self):
        while not self.game_over:
            current_time = time.perf_counter()
            
            if current_time - self.last_input > self.fps_loop:
                self.handle_input()
                self.last_input = current_time
            
            if current_time - self.last_render > self.fps_render:
                self.update()
                self.render()
                self.last_render = current_time
            
            time.sleep(self.fps_loop)
        
        self.render()


def main():
    game = Snake(20)
    
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nGame was interrupted by the user")


if __name__ == "__main__":
    main()
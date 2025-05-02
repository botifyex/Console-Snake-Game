# 🐍 Console Snake Game

A classic Snake game implemented in Python, running in the console with real-time keyboard input using the Windows API (`ctypes`). Control the snake to eat food, grow longer, and avoid collisions with walls or yourself!

## 📖 Overview

This project is a simple yet engaging implementation of the Snake game, designed to run in a Windows console. The game uses ASCII characters to render the game field and leverages the `ctypes` library to handle low-level keyboard input for smooth controls. The snake moves continuously, and the player must navigate to collect food while avoiding obstacles.

## ✨ Features

- **Dynamic Gameplay**: Control the snake using arrow keys with real-time input detection.
- **Score Tracking**: Earn points for each food item collected.
- **Game Over Detection**: Ends the game on collision with walls or the snake's body.
- **Customizable Field**: Configurable game field size (default: 20x20).
- **ASCII Art**: Simple and clean visual representation using Unicode characters.
- **Error Handling**: Gracefully handles user interruptions (e.g., Ctrl+C).

## 🛠️ Requirements

- **Operating System**: Windows (due to `ctypes` and `user32` dependency)
- **Python**: Version 3.6 or higher
- **No external libraries required** (uses only standard Python libraries)

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/botifyex/console-snake-game.git
   cd snake-game
   ```

2. **Ensure Python is Installed**:
   Verify you have Python 3.6+ installed by running:
   ```bash
   python --version
   ```

3. **Run the Game**:
   Execute the main script:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. Launch the game by running `python main.py`.
2. Use the **arrow keys** to control the snake's direction:
   - **Up Arrow**: Move up
   - **Down Arrow**: Move down
   - **Left Arrow**: Move left
   - **Right Arrow**: Move right
3. Guide the snake (`●` head, `○` body) to eat food (`•`) and avoid hitting walls (`#`) or the snake's body.
4. Each food item increases your score by 1.
5. The game ends if the snake collides with a wall or itself. Your final score is displayed.
6. Press `Ctrl+C` to exit the game early.

## 📝 Code Structure

- **`main.py`**: Main game script containing all logic.
- **Key Components**:
  - `Snake` class: Manages game state, snake movement, food spawning, and rendering.
  - `SnakeEvent`: Enum-like class for field object types (e.g., wall, food, snake).
  - `SnakeSymbol`: Defines ASCII symbols for rendering.
  - `Direction`: Enum-like class for snake movement directions.
  - Utility functions for console clearing and keyboard input detection via `ctypes`.

## 🖥️ Example Output

```
Score: 2
####################
#                  #
#                  #
#         •        #
#                  #
#         ●        #
#         ○        #
#         ○        #
#                  #
####################
```

## ⚙️ Customization

To modify the game, adjust the following in `snake.py`:
- **Field Size**: Change the `size` parameter in `Snake(20)` (e.g., `Snake(30)` for a 30x30 field).
- **Game Speed**: Adjust the `time.sleep(0.15)` value in the `run` method (lower values increase speed, e.g., `0.01` for ~60 FPS).
- **Symbols**: Modify `SnakeSymbol` class to use different ASCII/Unicode characters.

## 🙌 Acknowledgments

- Inspired by the classic Snake game.
- Built with Python and the `ctypes` library for Windows API integration.

---

⭐ If you enjoy this project, give it a star on GitHub!
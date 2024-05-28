
# 2048 Game in Tkinter

Welcome to the 2048 game implemented using Python's Tkinter library. This project recreates the popular 2048 puzzle game, where the objective is to combine tiles with the same number to reach the 2048 tile.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- 4x4 grid for classic 2048 gameplay.
- Smooth tile merging animations.
- Intuitive keyboard controls (Arrow keys).
- Automatic saving and loading of game state.
- Simple and clean user interface.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/2048-tkinter.git
   cd 2048-tkinter
   ```

2. (Optional) Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the game:

   ```sh
   python game2048.py
   ```

2. Use the arrow keys to move the tiles:

   - **Up Arrow**: Move tiles up
   - **Down Arrow**: Move tiles down
   - **Left Arrow**: Move tiles left
   - **Right Arrow**: Move tiles right

## Game Rules

1. Combine tiles of the same number to create larger numbers.
2. Each move, a new tile of value 2 or 4 will appear in an empty spot on the board.
3. The game is won when a tile with a value of 2048 is created.
4. The game ends when there are no possible moves left.

## Code Overview

The game is implemented in a single file `game2048.py`. Below is a brief overview of the main components:

### Class: `Game2048`

#### `__init__(self, master)`
Initializes the game, sets up the grid, and starts a new game.

#### `create_widgets(self)`
Creates the grid of tiles using Tkinter Labels and binds keyboard events.

#### `new_game(self)`
Starts a new game by resetting the grid and adding two random tiles.

#### `add_random_tile(self)`
Adds a random tile (2 or 4) to an empty spot on the grid.

#### `update_ui(self)`
Updates the UI to reflect the current state of the grid.

#### `handle_key(self, event)`
Handles keypress events and moves the tiles accordingly.

#### `move(self, direction)`
Performs the logic for moving tiles in the specified direction and merges tiles as needed.

#### `transpose(self, field)`
Transposes the grid, used for simplifying the move logic.

#### `can_move(self, direction)`
Checks if a move in the specified direction is possible.

### Main Loop

The main loop initializes the Tkinter root window and starts the game.

```python
if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding style and include tests where appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing 2048 and happy coding! If you encounter any issues or have suggestions, feel free to open an issue on the repository.

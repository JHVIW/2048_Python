import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        # Initialize the game
        self.master = master
        self.master.title("2048")
        self.grid_size = 4  # Size of the game grid (4x4)
        self.tiles = [[0]*self.grid_size for _ in range(self.grid_size)]  # Initialize the game grid with zeros
        self.colors = {  # Define the colors for different tile values
            0: "#ccc0b3",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e"
        }
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Create the GUI elements
        self.frame = tk.Frame(self.master)
        self.frame.grid(sticky="nsew")

        self.grid = []
        for row in range(self.grid_size):
            row_tiles = []
            for col in range(self.grid_size):
                tile = tk.Label(self.frame, text="", bg=self.colors[0], font=("Helvetica", 24), width=4, height=2)
                tile.grid(row=row, column=col, padx=5, pady=5)
                row_tiles.append(tile)
            self.grid.append(row_tiles)

        self.master.bind("<Key>", self.handle_key)

    def new_game(self):
        # Start a new game
        self.tiles = [[0]*self.grid_size for _ in range(self.grid_size)]
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def add_random_tile(self):
        # Add a random tile (2 or 4) to an empty spot on the grid
        empty_tiles = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size) if self.tiles[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.tiles[r][c] = random.choice([2, 4])

    def update_ui(self):
        # Update the GUI to reflect the current state of the grid
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                value = self.tiles[r][c]
                self.grid[r][c].config(text=str(value) if value != 0 else "", bg=self.colors[value])

    def handle_key(self, event):
        # Handle key presses to move tiles
        key = event.keysym
        if key == "Up":
            self.move("Up")
        elif key == "Down":
            self.move("Down")
        elif key == "Left":
            self.move("Left")
        elif key == "Right":
            self.move("Right")
        self.update_ui()

    def move(self, direction):
        # Move tiles in the specified direction
        def move_row_left(row):
            # Helper function to move and merge a row to the left
            new_row = [i for i in row if i != 0]  # Remove all zeros
            new_row += [0] * (len(row) - len(new_row))  # Add zeros to the end to maintain length
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:  # Merge tiles if they are the same
                    new_row[i] *= 2
                    new_row[i + 1] = 0
            new_row = [i for i in new_row if i != 0]  # Remove zeros again after merging
            new_row += [0] * (len(row) - len(new_row))  # Add zeros to the end again
            return new_row

        moves = {
            "Left": lambda field: [move_row_left(row) for row in field],
            "Right": lambda field: [move_row_left(row[::-1])[::-1] for row in field],
            "Up": lambda field: self.transpose(moves["Left"](self.transpose(field))),
            "Down": lambda field: self.transpose(moves["Right"](self.transpose(field)))
        }

        if direction in moves:
            if self.can_move(direction):
                self.tiles = moves[direction](self.tiles)
                self.add_random_tile()

    def transpose(self, field):
        # Transpose the grid (rows become columns and vice versa)
        return [list(row) for row in zip(*field)]

    def can_move(self, direction):
        # Check if a move in the specified direction is possible
        def row_can_move(row):
            # Helper function to check if a single row can move
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i] == row[i + 1]:
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {
            "Left": lambda field: any(row_can_move(row) for row in field),
            "Right": lambda field: check["Left"]([row[::-1] for row in field]),
            "Up": lambda field: check["Left"](self.transpose(field)),
            "Down": lambda field: check["Right"](self.transpose(field))
        }

        if direction in check:
            return check[direction](self.tiles)
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()

import tkinter as tk
from grid.crossword_grid import CrosswordGrid
from dictionary.word_loader import load_word_dict_by_length
from csp.solver import build_and_solve

CELL_SIZE = 50

class CrosswordGUI:
    def __init__(self, master):
        self.master = master
        master.title("Crossword Puzzle Auto Generator")

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.generate_button = tk.Button(master, text="Generate Crossword", command=self.generate_crossword)
        self.generate_button.pack()

        self.grid_obj = None  # Will store the CrosswordGrid instance

    def generate_crossword(self):
        self.canvas.delete("all")

        self.grid_obj = CrosswordGrid("assets/sample_grid.txt")
        word_dict = load_word_dict_by_length(15)
        solution, slot_map = build_and_solve(self.grid_obj.slots, word_dict)

        if solution:
            self.grid_obj.fill_grid(solution, slot_map)
            self.draw_grid(self.grid_obj.grid)
        else:
            print("❌ Could not generate crossword.")

    def draw_grid(self, grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                if grid[r][c] == "#":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                    if grid[r][c] != "_":
                        self.canvas.create_text(x1 + 25, y1 + 25, text=grid[r][c].upper(), font=("Helvetica", 16))


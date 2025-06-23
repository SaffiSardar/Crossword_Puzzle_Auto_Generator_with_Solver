from grid.crossword_grid import CrosswordGrid
from dictionary.word_loader import load_word_dict_by_length
from csp.solver import build_and_solve

grid = CrosswordGrid("assets/sample_grid.txt")
word_dict = load_word_dict_by_length(15)

solution = build_and_solve(grid.slots, word_dict)

if solution:
    for k, v in solution.items():
        print(f"{k}: {v}")
else:
    print("No valid solution found.")

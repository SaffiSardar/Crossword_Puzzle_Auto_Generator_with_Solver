# main.py

from crossword import parse_grid, find_variables
from csp_solver import CrosswordCSP
from utils import load_dictionary, print_grid

if __name__ == "__main__":
    grid_layout = [
        "___",
        "___",
        "___"
    ]
    
    grid = parse_grid(grid_layout)
    variables = find_variables(grid)
    dictionary = load_dictionary()

    csp = CrosswordCSP(grid, variables, dictionary)
    assignment = csp.backtrack()

    if assignment:
        filled = csp.fill_grid(assignment)
        print("✅ Crossword Generated:\n")
        print_grid(filled)
    else:
        print("❌ No solution found.")

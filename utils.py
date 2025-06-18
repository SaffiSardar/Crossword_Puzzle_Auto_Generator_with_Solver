# utils.py

def load_dictionary(path="wordlist.txt"):
    with open(path, "r") as file:
        return [line.strip().upper() for line in file if line.strip().isalpha()]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

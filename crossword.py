# crossword.py

def parse_grid(grid_layout):
    return [list(row) for row in grid_layout]

def find_variables(grid):
    variables = []

    # Horizontal words
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j] == '_':
                start = j
                while j < len(row) and row[j] == '_':
                    j += 1
                if j - start > 1:
                    variables.append((i, start, 'H', j - start))
            else:
                j += 1

    # Vertical words
    for j in range(len(grid[0])):
        i = 0
        while i < len(grid):
            if grid[i][j] == '_':
                start = i
                while i < len(grid) and grid[i][j] == '_':
                    i += 1
                if i - start > 1:
                    variables.append((start, j, 'V', i - start))
            else:
                i += 1

    return variables

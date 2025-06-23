class CrosswordGrid:
    def __init__(self, file_path):
        self.grid = self.read_grid(file_path)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.slots = self.extract_slots()

    def read_grid(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return [line.strip().split() for line in lines]

    def extract_slots(self):
        slots = []
        # Horizontal
        for r in range(self.rows):
            c = 0
            while c < self.cols:
                start = c
                while c < self.cols and self.grid[r][c] == '_':
                    c += 1
                length = c - start
                if length >= 2:
                    slots.append({'start': (r, start), 'len': length, 'dir': 'across'})
                c += 1

        # Vertical
        for c in range(self.cols):
            r = 0
            while r < self.rows:
                start = r
                while r < self.rows and self.grid[r][c] == '_':
                    r += 1
                length = r - start
                if length >= 2:
                    slots.append({'start': (start, c), 'len': length, 'dir': 'down'})
                r += 1

        return slots
    
    def display_grid(self):
        for row in self.grid:
            print(" ".join(['■' if cell == '#' else '.' for cell in row]))



# grid = CrosswordGrid("assets/sample_grid.txt")
# print(grid.grid)


# if __name__ == "__main__":
#     grid = CrosswordGrid("assets/sample_grid.txt")
#     for slot in grid.slots:
#         print(slot)

# print(grid.display_grid())
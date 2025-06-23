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
            print(" ".join(['■' if cell == '#' else cell for cell in row]))

        
    def fill_grid(self, solution, slot_map):
        if not solution:
            print("❌ No solution given to fill the grid.")
            return
        if not slot_map:
            print("❌ No slot_map given to fill the grid.")
            return

        print(f"\n🧠 Filling {len(solution)} slots into the grid...\n")

        for slot_id, word in solution.items():
            print(f"Placing '{word}' in slot {slot_id}")

            # extra safety checks
            if slot_id not in slot_map:
                print(f"⚠️ Slot ID {slot_id} not found in slot_map.")
                continue

            slot = slot_map[slot_id]
            r, c = slot['start']
            direction = slot['dir']

            print(f" → Position: {slot['start']}, Direction: {direction}")

            for i in range(len(word)):
                try:
                    if direction == 'across':
                        self.grid[r][c + i] = word[i]
                    elif direction == 'down':
                        self.grid[r + i][c] = word[i]
                    else:
                        print(f"❌ Invalid direction '{direction}' for slot {slot_id}")
                except Exception as e:
                    print(f"❌ Error placing letter '{word[i]}' for slot {slot_id}: {e}")






# grid = CrosswordGrid("assets/sample_grid.txt")
# print(grid.grid)


# if __name__ == "__main__":
#     grid = CrosswordGrid("assets/sample_grid.txt")
#     for slot in grid.slots:
#         print(slot)

# print(grid.display_grid())
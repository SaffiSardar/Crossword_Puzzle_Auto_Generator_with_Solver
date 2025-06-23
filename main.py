from grid.crossword_grid import CrosswordGrid
from dictionary.word_loader import load_word_dict_by_length
from csp.solver import build_and_solve

# Load grid and dictionary
grid = CrosswordGrid("assets/sample_grid.txt")
word_dict = load_word_dict_by_length(15)

# Solve using CSP
solution, slot_map, solve_time = build_and_solve(grid.slots, word_dict)

print("########################################################################################################################################################")

# Print slot info
print("\nSLOT MAP:")
for k, v in slot_map.items():
    print(f"{k}: {v}")

# Fill and show grid
if solution:
    grid.fill_grid(solution, slot_map)
    print("\nFinal Filled Grid:\n")
    grid.display_grid()

    # 💡 NEW: Calculate and show metrics
    fill_rate = grid.calculate_fill_rate()
    print("\n📈 Metrics:")
    print(f"🕒 Solve Time: {solve_time} seconds")
    print(f"📦 Fill Rate: {fill_rate}%")
    print(f"✅ Slots Filled: {len(solution)} / {len(slot_map)}")
else:
    print("❌ No valid crossword could be generated.")

print("\nSOLUTION:", solution)

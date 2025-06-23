from grid.crossword_grid import CrosswordGrid
from dictionary.word_loader import load_word_dict_by_length
from csp.solver import build_and_solve

grid = CrosswordGrid("assets/sample_grid.txt")
word_dict = load_word_dict_by_length(15)

solution, slot_map = build_and_solve(grid.slots, word_dict)

print("########################################################################################################################################################")

solution, slot_map = build_and_solve(grid.slots, word_dict)
print("\nSLOT MAP:")
for k, v in slot_map.items():
    print(f"{k}: {v}")

grid.fill_grid(solution, slot_map)


print("########################################################################################################################################################")

if solution:
    grid.fill_grid(solution, slot_map)
    print("\nFinal Filled Grid:\n")
    grid.display_grid()
else:
    print("❌ No valid crossword could be generated.")

print("SOLUTION:", solution)




from constraint import Problem

def get_coords(slot):
    r, c = slot['start']
    direction = slot['dir']
    length = slot['len']
    return [(r + i, c) if direction == 'down' else (r, c + i) for i in range(length)]

def build_and_solve(slots, word_dict):
    problem = Problem()
    slot_map = {}

    # Step 1: Assign unique IDs to slots like S1, S2, ...
    for i, slot in enumerate(slots):
        slot_id = f"S{i}"
        slot_map[slot_id] = slot
        length = slot['len']
        domain = word_dict.get(length, [])
        problem.addVariable(slot_id, domain)

    # Step 2: Add intersection constraints
    slot_items = list(slot_map.items())
    for i in range(len(slot_items)):
        for j in range(i + 1, len(slot_items)):
            id1, slot1 = slot_items[i]
            id2, slot2 = slot_items[j]

            if slot1['dir'] == slot2['dir']:
                continue  # Only different directions intersect

            coords1 = get_coords(slot1)
            coords2 = get_coords(slot2)

            intersect = set(coords1) & set(coords2)
            if intersect:
                (r, c) = list(intersect)[0]
                index1 = coords1.index((r, c))
                index2 = coords2.index((r, c))

                def constraint_fn(w1, w2, i1=index1, i2=index2):
                    return w1[i1] == w2[i2]

                problem.addConstraint(constraint_fn, (id1, id2))

    # Step 3: Solve it
    solution = problem.getSolution()
    return solution, slot_map


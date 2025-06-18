# csp_solver.py

class CrosswordCSP:
    def __init__(self, grid, variables, dictionary):
        self.grid = grid
        self.variables = variables
        self.dictionary = dictionary
        self.domains = self.build_domains()
        self.overlaps = self.build_overlaps()

    def build_domains(self):
        domains = {}
        for var in self.variables:
            length = var[3]
            domains[var] = [word.upper() for word in self.dictionary if len(word) == length]
        return domains

    def build_overlaps(self):
        overlaps = {}
        for var1 in self.variables:
            for var2 in self.variables:
                if var1 == var2:
                    continue
                overlap = self.check_overlap(var1, var2)
                if overlap:
                    overlaps[(var1, var2)] = overlap
        return overlaps

    def check_overlap(self, var1, var2):
        (i1, j1, d1, l1) = var1
        (i2, j2, d2, l2) = var2
        for k1 in range(l1):
            x1 = i1 + (k1 if d1 == 'V' else 0)
            y1 = j1 + (k1 if d1 == 'H' else 0)
            for k2 in range(l2):
                x2 = i2 + (k2 if d2 == 'V' else 0)
                y2 = j2 + (k2 if d2 == 'H' else 0)
                if x1 == x2 and y1 == y2:
                    return (k1, k2)
        return None

    def is_consistent(self, var, word, assignment):
        for other_var in assignment:
            if (var, other_var) in self.overlaps:
                i, j = self.overlaps[(var, other_var)]
                if word[i] != assignment[other_var][j]:
                    return False
        return True

    def select_unassigned_var(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        return min(unassigned, key=lambda var: len(self.domains[var]))

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        var = self.select_unassigned_var(assignment)
        for word in self.domains[var]:
            if self.is_consistent(var, word, assignment):
                assignment[var] = word
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

    def fill_grid(self, assignment):
        new_grid = [row.copy() for row in self.grid]
        for var, word in assignment.items():
            i, j, d, l = var
            for k in range(l):
                x = i + (k if d == 'V' else 0)
                y = j + (k if d == 'H' else 0)
                new_grid[x][y] = word[k]
        return new_grid

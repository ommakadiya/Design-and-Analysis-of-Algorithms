# Sudoku solver using backtracking + MRV heuristic
# Grid format: 9x9 list of lists, 0 means empty.

def solve_sudoku(grid):
    """
    Solves the Sudoku in-place. Returns True if solved, False if unsolvable.
    """
    # Precompute sets for rows, cols, and boxes of used digits
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []

    # Initialize
    for r in range(9):
        for c in range(9):
            v = grid[r][c]
            if v != 0:
                rows[r].add(v)
                cols[c].add(v)
                boxes[(r//3)*3 + (c//3)].add(v)
            else:
                empties.append((r,c))

    def candidates(r, c):
        """Return a set of possible digits for cell (r,c)."""
        used = rows[r] | cols[c] | boxes[(r//3)*3 + (c//3)]
        return {d for d in range(1,10) if d not in used}

    # Backtracking with MRV: choose empty cell with fewest candidates
    def backtrack():
        if not empties:
            return True  # solved

        # MRV: find index of empty with fewest candidates
        best_idx = None
        best_opts = None
        best_len = 10
        for i, (r,c) in enumerate(empties):
            opts = candidates(r,c)
            L = len(opts)
            if L == 0:
                return False  # dead end
            if L < best_len:
                best_len = L
                best_opts = opts
                best_idx = i
                if L == 1:
                    break

        # Take that cell out of empties (swap-pop)
        r, c = empties.pop(best_idx)

        for val in sorted(best_opts):  # sorting not necessary but deterministic
            # place
            grid[r][c] = val
            rows[r].add(val)
            cols[c].add(val)
            boxes[(r//3)*3 + (c//3)].add(val)

            if backtrack():
                return True

            # undo
            grid[r][c] = 0
            rows[r].remove(val)
            cols[c].remove(val)
            boxes[(r//3)*3 + (c//3)].remove(val)

        # restore empties
        empties.insert(best_idx, (r,c))
        return False

    return backtrack()


def print_grid(g):
    for i, row in enumerate(g):
        print(' '.join(str(x) if x!=0 else '.' for x in row))
        if i % 3 == 2 and i != 8:
            print('-'*21)


# Example usage
if __name__ == "__main__":
    puzzle = [
        [0,0,0, 6,0,4, 7,0,0],
        [7,0,6, 0,0,0, 0,0,9],
        [0,0,0, 0,0,5, 0,8,0],

        [0,7,0, 0,2,0, 0,9,3],
        [8,0,0, 0,0,0, 0,0,5],
        [4,3,0, 0,1,0, 0,7,0],

        [0,5,0, 2,0,0, 0,0,0],
        [3,0,0, 0,0,0, 2,0,8],
        [0,0,2, 3,0,1, 0,0,0],
    ]

    print("Puzzle:")
    print_grid(puzzle)
    solved = solve_sudoku(puzzle)
    print("\nSolved:" if solved else "\nNo solution found.")
    print_grid(puzzle)

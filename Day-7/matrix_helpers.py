# ==============================================================================
# Course: Python Programming
# Session: Day 7 (Chapter 7 & 8: 1D Lists & Multi-Dimensional Lists)
# Module: matrix_helpers.py — Reusable Matrix & List Transformation Utilities
#
# Description:
#   A reusable helper library for matrix creation, pretty printing,
#   row/column aggregation, transpositions, and deep copy isolation.
# ==============================================================================

import copy

def create_grid(rows, cols, initial_value=0):
    """
    Create and return an independent rows x cols matrix initialized with initial_value.
    Uses list comprehension to prevent shallow row reference duplication.
    """
    return [[initial_value for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix, label="Matrix Grid"):
    """
    Display a formatted 2D matrix with column indices and neat column alignment.
    """
    if not matrix or not matrix[0]:
        print(f"{label}: [Empty Matrix]")
        return

    cols = len(matrix[0])
    print(f"\n--- {label} ({len(matrix)}x{cols}) ---")
    
    # Print header row with column numbers
    header = "     " + "".join(f"Col {c:<5}" for c in range(cols))
    print(header)
    print("    " + "-" * (len(header) - 4))
    
    for r_idx, row in enumerate(matrix):
        row_str = f"R{r_idx:<2} |"
        for val in row:
            if isinstance(val, float):
                row_str += f"{val:7.1f} "
            else:
                row_str += f"{str(val):>6} "
        print(row_str)


def calculate_row_totals(matrix):
    """
    Compute and return a 1D list containing the sum of elements for each row.
    """
    return [sum(row) for row in matrix]


def calculate_col_totals(matrix):
    """
    Compute and return a 1D list containing the sum of elements for each column.
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    col_totals = []
    
    for c in range(cols):
        col_sum = sum(matrix[r][c] for r in range(rows))
        col_totals.append(col_sum)
    return col_totals


def transpose_matrix(matrix):
    """
    Return a new matrix which is the transpose of the input matrix.
    Rows become columns and columns become rows.
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def clone_matrix(matrix):
    """
    Perform a true deep copy of a 2D matrix to prevent unwanted side-effects.
    """
    return copy.deepcopy(matrix)


# ==============================================================================
# SELF-TESTING GUARD (__name__ == '__main__')
# ==============================================================================
if __name__ == "__main__":
    print("=== Testing matrix_helpers.py directly ===")
    
    # Test grid creation
    sample_grid = create_grid(3, 4, 10)
    sample_grid[0][0] = 99
    print_matrix(sample_grid, "Sample 3x4 Grid")
    
    # Test row and col totals
    print(f"Row Totals: {calculate_row_totals(sample_grid)}")
    print(f"Col Totals: {calculate_col_totals(sample_grid)}")
    
    # Test transpose
    t_grid = transpose_matrix(sample_grid)
    print_matrix(t_grid, "Transposed Grid")
    
    print("\nAll matrix_helpers tests executed cleanly!")

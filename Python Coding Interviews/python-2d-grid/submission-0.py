from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    """
    2D grid named grid, 2 integers r and c, r = index of a row, c = index of a column
    return True if cell at row r and column c within the bounds of the grid, False otherwise
    Grid = [
            [0, 0, 0],
            [0, 0, 0],
    ]
    row = len(grid)         # 2 rows
    column = len(grid[0])   # 3 columns
    let r = 3
    let c = 2
    in this above use case.
    # cell would only be in the bounds if the number at grid[r][c]
    """
    max_row_index, max_column_index = len(grid) - 1, len(grid[0]) - 1
    
    if r > max_row_index or c > max_column_index:
        return False
    
    return True

    

# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))

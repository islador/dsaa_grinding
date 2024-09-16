class Solution:
    @classmethod
    # Computational complexity is R x C where R is row count and C is column count.
    def find_rotten_fruits(self, row_count, column_count, grid, rotten_fruits):
        current_row = 0
        current_column = 0
        while current_row < row_count:
            while current_column < column_count:
                if grid[current_row][current_column] == 0:
                    rotten_fruits.append([current_row, current_column])
                current_column+=1
            current_row+=1
            current_column = 0

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])
        rotten_fruits = []
        self.find_rotten_fruits(row_count, column_count, grid, rotten_fruits)
        
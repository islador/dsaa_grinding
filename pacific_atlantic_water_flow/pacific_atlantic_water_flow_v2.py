from typing import List
class Cell:
    def __init__(self, value, coordinates):
        self.value = value
        self.coordinates = coordinates

class Solution:

    @classmethod
    def stable_sort_matrix(self, row_count, column_count, matrix):
        # Load the matrix
        current_row = 0
        current_column = 0
        values_in_order = []
        # Convert the matrix into a flat array of sortable objects.
        while current_row < row_count:
            while current_column < column_count:
                values_in_order.append(Cell(matrix[current_row][current_column],[current_row, current_column]))
                current_column+=1
            current_row +=1
            current_column = 0
        for n in range(len(values_in_order)-1, 0, -1):
            for i in range(n):
                if values_in_order[i].value > values_in_order[i+1].value:
                    swapped = True
                    values_in_order[i], values_in_order[i+1] = values_in_order[i+1], values_in_order[i]
        return values_in_order


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Configuration Variables
        row_count = len(heights)
        column_count = len(heights[0])
        sorted_coordinates = self.stable_sort_matrix(row_count, column_count, heights)
        for cell in sorted_coordinates:
            print(f"{cell.coordinates}")
        return [[1]]

#input_array = [[2,2,2],[2,1,2],[2,2,2]]
#print(f"{Solution.pacificAtlantic(Solution, input_array)}")

input_array = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
print(f"{Solution.pacificAtlantic(Solution, input_array)}")
from typing import List
class Cell:
    def __init__(self, value, coordinates):
        self.value = value
        self.coordinates = coordinates

class Solution:

    @classmethod
    def stable_sort_matrix(self, row_count, column_count, matrix):
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

        # Bubble Sort the built array to achieve a stable lowest to highest value sort
        for n in range(len(values_in_order)-1, 0, -1):
            for i in range(n):
                if values_in_order[i].value > values_in_order[i+1].value:
                    swapped = True
                    values_in_order[i], values_in_order[i+1] = values_in_order[i+1], values_in_order[i]
        return values_in_order

    @classmethod
    def build_flow_destinations_matrix(self, row_count, column_count):
        current_row = 0
        current_column = 0
        flow_destinations = []
        # Expand the matrix and populate it with known flow destinations
        while current_row < row_count:
            flow_destinations.append([])
            while current_column < column_count:
                flow_destinations[current_row].append([])
                if (current_row == 0) and (current_column == column_count-1):
                    flow_destinations[current_row][current_column] = {"Pacific": True, "Atlantic": True}
                elif (current_row == row_count-1) and (current_column == 0):
                    flow_destinations[current_row][current_column] = {"Pacific": True, "Atlantic": True}
                else:
                    flow_destinations[current_row][current_column] = {}
                current_column+=1
            current_row +=1
            current_column = 0
        return flow_destinations

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Configuration Variables
        row_count = len(heights)
        column_count = len(heights[0])
        sorted_coordinates = self.stable_sort_matrix(row_count, column_count, heights)
        flow_destinations = self.build_flow_destinations_matrix(row_count, column_count)
        print(f"Flow Destinations")
        print(f"{flow_destinations}")
        #for cell in sorted_coordinates:
        #    print(f"{cell.coordinates}")
        return [[1]]

#input_array = [[2,2,2],[2,1,2],[2,2,2]]
#print(f"{Solution.pacificAtlantic(Solution, input_array)}")

input_array = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
print(f"{Solution.pacificAtlantic(Solution, input_array)}")
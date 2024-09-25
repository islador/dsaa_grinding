from typing import List
class Cell:
    def __init__(self, value, coordinates):
        self.value = value
        self.coordinates = coordinates

class Solution:

    @classmethod
    def assemble_new_flow_destination_for_cell(self, cell, flow_destinations, updated_destinations):
        current_flow_destinations = flow_destinations[cell.coordinates[0]][cell.coordinates[1]]
        safe_updates = current_flow_destinations

        if "Pacific" in updated_destinations:
            if updated_destinations["Pacific"] == True:
                safe_updates["Pacific"] = True
        if "Atlantic" in updated_destinations:
            if updated_destinations["Atlantic"] == True:
                safe_updates["Atlantic"] = True

        return safe_updates

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

    @classmethod
    def calculate_next_position_from_sequence(self, sequence, sequence_position, cell):
        row = cell.coordinates[0]+sequence[sequence_position][0]
        column = cell.coordinates[1]+sequence[sequence_position][1]
        return [row,column]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Configuration Variables
        row_count = len(heights)
        column_count = len(heights[0])
        flow_destinations = self.build_flow_destinations_matrix(row_count, column_count)
        sorted_coordinates = self.stable_sort_matrix(row_count, column_count, heights)
        sequence = [[0,-1],[-1,0],[0,1],[1,0]]
        
        # Traverse array
        sequence_position = 0
        for cell in sorted_coordinates:
            if flow_destinations[cell.coordinates[0]][cell.coordinates[1]] != {"Pacific": True, "Atlantic": True}:
                # Left
                next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, cell)
                print(f"cell_coordinates: {cell.coordinates}, next_position: {next_position}")
                sequence_position +=1
                # Up
                next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, cell)
                print(f"cell_coordinates: {cell.coordinates}, next_position: {next_position}")
                sequence_position +=1
                # Right
                next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, cell)
                print(f"cell_coordinates: {cell.coordinates}, next_position: {next_position}")
                sequence_position +=1
                # Down
                next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, cell)
                print(f"cell_coordinates: {cell.coordinates}, next_position: {next_position}")
                sequence_position = 0
            else:
                # Need recursive elements
                updated_destinations = {"Pacific": True}
            # This is in the wrong space, it needs to be moved once the rest of the functions are defined.
            updated_destinations = {"Pacific": True}
            flow_destinations[cell.coordinates[0]][cell.coordinates[1]] = self.assemble_new_flow_destination_for_cell(cell, flow_destinations, updated_destinations)
        print(f"flow_destinations: {flow_destinations}")
        return [[1]]

#input_array = [[2,2,2],[2,1,2],[2,2,2]]
#print(f"{Solution.pacificAtlantic(Solution, input_array)}")

input_array = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
print(f"{Solution.pacificAtlantic(Solution, input_array)}")
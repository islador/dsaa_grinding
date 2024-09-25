from typing import List
class Cell:
    def __init__(self, value, coordinates):
        self.value = value
        self.coordinates = coordinates

class Solution:

    @classmethod
    def assemble_safe_flow_destination_updates(self, current_flow_destinations, updated_destinations):
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
    def calculate_next_position_from_sequence(self, sequence, sequence_position, position):
        row = position[0]+sequence[sequence_position][0]
        column = position[1]+sequence[sequence_position][1]
        return [row,column]

    @classmethod
    def coordinates_are_in_matrix(self, row_count, column_count, coordinates):
        if coordinates[0] < 0:
            return False
        if coordinates[1] < 0:
            return False
        if coordinates[0] > row_count-1:
            return False
        if coordinates[1] > column_count-1:
            return False
        return True

    @classmethod
    def calculate_ocean_from_off_matrix_coordinates(self, row_count, column_count, coordinates):
        pacific = False
        atlantic = False
        
        if coordinates[0] < 0:
            pacific = True
        if coordinates[1] < 0:
            pacific = True
        if coordinates[0] > row_count-1:
            atlantic = True
        if coordinates[1] > column_count-1:
            atlantic = True

        return {"Pacific": pacific, "Atlantic": atlantic}
    
    @classmethod
    def inspect_cell(self, row_count, column_count, flow_destinations, heights, current_position, next_position, recursive_cell_stack):
        updated_destinations = {}
        if self.coordinates_are_in_matrix(row_count, column_count, next_position):
            # If the cell is lower
            if heights[next_position[0]][next_position[1]] < heights[current_position[0]][current_position[1]]:
                if flow_destinations[next_position[0]][next_position[1]] == {"Pacific": True, "Atlantic": True}:
                    return self.assemble_safe_flow_destination_updates(updated_destinations, flow_destinations[next_position[0]][next_position[1]])
                else:
                    updated_destinations = self.assemble_safe_flow_destination_updates(updated_destinations, flow_destinations[next_position[0]][next_position[1]])
            # If the next cell is the same as the current cell
            if heights[next_position[0]][next_position[1]] == heights[current_position[0]][current_position[1]]:
                if next_position not in recursive_cell_stack:
                    if flow_destinations[next_position[0]][next_position[1]] == {"Pacific": True, "Atlantic": True}:
                        return self.assemble_safe_flow_destination_updates(updated_destinations, flow_destinations[next_position[0]][next_position[1]])
                    else:
                        recursive_cell_stack.append(next_position)
                        updated_destinations = self.find_flow_destinations_for_cell(row_count, column_count, flow_destinations, heights, next_position, recursive_cell_stack)
        else:
            discovered_destinations = self.calculate_ocean_from_off_matrix_coordinates(row_count, column_count, next_position)
            updated_destinations = self.assemble_safe_flow_destination_updates(updated_destinations, discovered_destinations)
        return updated_destinations, recursive_cell_stack
    
    @classmethod
    def find_flow_destinations_for_cell(self, row_count, column_count, flow_destinations, heights, current_position, recursive_cell_stack):
        sequence = [[0,-1],[-1,0],[0,1],[1,0]]
        sequence_position = 0
        updated_destinations = {}
        if flow_destinations[current_position[0]][current_position[1]] != {"Pacific": True, "Atlantic": True}:
            # Left
            next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, current_position)
            sequence_position +=1
            updated_destinations, recursive_cell_stack = self.inspect_cell(row_count, column_count, flow_destinations, heights, current_position, next_position, recursive_cell_stack)
            # Up
            next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, current_position)
            sequence_position +=1
            updated_destinations, recursive_cell_stack = self.inspect_cell(row_count, column_count, flow_destinations, heights, current_position, next_position, recursive_cell_stack)
            # Right
            next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, current_position)
            sequence_position +=1
            updated_destinations, recursive_cell_stack = self.inspect_cell(row_count, column_count, flow_destinations, heights, current_position, next_position, recursive_cell_stack)
            # Down
            next_position = self.calculate_next_position_from_sequence(sequence, sequence_position, current_position)
            sequence_position = 0
            updated_destinations, recursive_cell_stack = self.inspect_cell(row_count, column_count, flow_destinations, heights, current_position, next_position, recursive_cell_stack)
        else:
            updated_destinations = self.assemble_safe_flow_destination_updates(updated_destinations, flow_destinations[current_position[0]][current_position[1]])
        return updated_destinations
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Configuration Variables
        row_count = len(heights)
        column_count = len(heights[0])
        flow_destinations = self.build_flow_destinations_matrix(row_count, column_count)
        sorted_coordinates = self.stable_sort_matrix(row_count, column_count, heights)
        
        # Calculate all the flow destinations
        for cell in sorted_coordinates:
            # So i want to recurse to here. How does that work?
            updated_destinations = self.find_flow_destinations_for_cell(row_count, column_count, flow_destinations, heights, cell.coordinates, [])
            # This is in the wrong space, it needs to be moved once the rest of the functions are defined.
            flow_destinations[cell.coordinates[0]][cell.coordinates[1]] = self.assemble_safe_flow_destination_updates(flow_destinations[cell.coordinates[0]][cell.coordinates[1]], updated_destinations)

        # Package it up for evaluation
        current_row = 0
        current_column = 0
        results = []
        # Expand the matrix and populate it with known flow destinations
        while current_row < row_count:
            while current_column < column_count:
                if flow_destinations[current_row][current_column] == {"Pacific": True, "Atlantic": True}:
                    results.append([current_row,current_column])
                current_column+=1
            current_row +=1
            current_column = 0
        return results

input_array = [[2,2,2],[2,1,2],[2,2,2]]
results = Solution.pacificAtlantic(Solution, input_array)
if results == [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]:
    print("Correct")
else:
    print(f"Wrong: {results}")

input_array = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
results = Solution.pacificAtlantic(Solution, input_array)
if results == [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]:
    print("Correct")
else:
    print(f"Wrong: {results}")
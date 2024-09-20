class Solution:
    @classmethod
    def is_new_position_in_matrix(self, row_count, column_count, new_position):
        if new_position[0] < 0:
            return False
        if new_position[1] < 0:
            return False
        if new_position[0] > row_count-1:
            return False
        if new_position[1] > column_count-1:
            return False
        return True

    @classmethod
    def storage_array_position_from_matrix_position(self, column_count, position):
        return (position[0] * column_count) + position[1]

    @classmethod
    def calculate_adjacent_cells_positions(self,current_position):
        adjacent_cell_positions = []
        adjacent_cell_positions.append([current_position[0], current_position[1]-1])
        adjacent_cell_positions.append([current_position[0], current_position[1]+1])
        adjacent_cell_positions.append([current_position[0]-1, current_position[1]])
        adjacent_cell_positions.append([current_position[0]+1, current_position[1]])
        return adjacent_cell_positions

    @classmethod
    def add_flow_destination_for_current_position(self, flow_destinations, column_count, current_position, new_destinations):
        new_destinations["cell_position"] = current_position
        current_destinations = flow_destinations[self.storage_array_position_from_matrix_position(column_count, current_position)]
        # Merge the old value with the new value
        flow_destinations[self.storage_array_position_from_matrix_position(column_count, current_position)] = current_destinations | new_destinations

    @classmethod
    def find_flow_destinations_for_current_position(self, matrix, row_count, column_count, current_position, flow_destinations):
        #print(f"current_position: {current_position}")
        ###
        ## Run the algo by hand; something is broken in the way I'm storing flow destinations.
        ###
        adjacent_cell_positions = self.calculate_adjacent_cells_positions(current_position)
        current_position_value = matrix[current_position[0]][current_position[1]]
        for adjacent_cell_position in adjacent_cell_positions:
            # If the cell position of a calculated adjacent cell is not in the matrix then we have a border cell.
            if self.is_new_position_in_matrix(row_count, column_count, adjacent_cell_position) == False:
                if adjacent_cell_position[0] == -1:
                    # If the row value is -1, then we're at the top of the matrix and thus have a flow destination of the Pacific
                    self.add_flow_destination_for_current_position(flow_destinations, column_count, current_position, {"Pacific": True})
                if adjacent_cell_position[1] == -1:
                    # If the column value is -1, then we're at the left of the matrix and thus have a flow destination of the Pacific
                    self.add_flow_destination_for_current_position(flow_destinations, column_count, current_position, {"Pacific": True})
                if adjacent_cell_position[0] > (row_count -1):
                    # If the row value is greater than the number of rows, adjusted for binary counting, then we're at the bottom of the matrix and thus have a flow destination of the Atlantic
                    self.add_flow_destination_for_current_position(flow_destinations, column_count, current_position, {"Atlantic": True})
                if adjacent_cell_position[1] > (column_count -1):
                    # If the column value is greater than the number of columns, adjusted for binary counting, then we're at the right of the matrix and thus have a flow destination of the Atlantic
                    self.add_flow_destination_for_current_position(flow_destinations, column_count, current_position, {"Atlantic": True})
            else:
                # If the adjacent_cell_position's value is lower than the current_positions' value then
                if matrix[adjacent_cell_position[0]][adjacent_cell_position[1]] < matrix[current_position[0]][current_position[1]]:
                    # Extract out the adjacent_cell's flow destinations
                    downstream_cell_destinations = flow_destinations[self.storage_array_position_from_matrix_position(column_count, adjacent_cell_position)]
                    self.add_flow_destination_for_current_position(flow_destinations, column_count, current_position, downstream_cell_destinations)

    @classmethod
    def calculate_next_position(self, row_count, column_count, current_position, current_direction):
        # Calculate next position
        next_position = [current_position[0], current_position[1]]
        if current_direction == "right":
            next_position[1] +=1
        if current_direction == "down":
            next_position[0] +=1
        if current_direction == "left":
            next_position[1] -=1
        if current_direction == "up":
            next_position[0] +=1
        return next_position
    
    @classmethod
    def is_next_position_valid(self, row_count, column_count, visited_cells, next_position):
        # Return False if the next position would take us off the matrix or to a previously visited cell
        if self.is_new_position_in_matrix(row_count, column_count, next_position) == False:
            return False
        if visited_cells[self.storage_array_position_from_matrix_position(column_count, next_position)] == True:
            return False
        return True

    @classmethod
    def increment_matrix_accessors(self, current_direction, current_row, current_column):
        if current_direction == "right":
            current_column +=1
        if current_direction == "down":
            current_row +=1
        if current_direction == "left":
            current_column -=1
        if current_direction == "up":
            current_row -=1
        return current_row, current_column
    
    @classmethod
    def clockwise_traverse_matrix(self, row_count, column_count, matrix, next_direction_sequence, visited_cells, flow_destinations):
        i = 0
        current_row = 0
        current_column = 0
        current_direction = "right"
        # Clockwise Algorithm - Assume the matrix is always square
        # 1. Move to the right until you encounter a previously visited cell or the edge of the matrix.
        # 2. Move down until you encounter a previously visited cell or the edge of the matrix.
        # 3. Move left until you encounter a previously visited cell or the edge of the matrix.
        # 4. Move up until you encounter a previously visited cell or the edge of the matrix.
        while i < ((row_count * column_count)):
            current_position = [current_row, current_column]
            visited_cells[self.storage_array_position_from_matrix_position(column_count, current_position)] = True
            # Assign flow_destinations for the current position based on what is around it.
            self.find_flow_destinations_for_current_position(matrix, row_count, column_count, [current_row, current_column], flow_destinations)

            # Check the next cell
            next_position = self.calculate_next_position(row_count, column_count, current_position, current_direction)
            if self.is_next_position_valid(row_count, column_count, visited_cells, next_position) == True:
                current_row, current_column = self.increment_matrix_accessors(current_direction, current_row, current_column)
            else:
                current_direction = next_direction_sequence[current_direction]
                current_row, current_column = self.increment_matrix_accessors(current_direction, current_row, current_column)
            i+=1

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_count = len(heights)
        column_count = len(heights[0])
        flow_destinations = [{"Atlantic": False, "Pacific": False} for x in range(row_count*column_count)]
        visited_cells = [False for x in range(row_count*column_count)]
        next_direction_sequence = {"right": "down", "down": "left", "left": "up", "up": "right"}
        self.clockwise_traverse_matrix(row_count, column_count, heights, next_direction_sequence, visited_cells, flow_destinations)
        #print(f"Flow Destinations: {flow_destinations}")
        
        cells_that_drain_into_both = []
        for flow_destination in flow_destinations:
            if flow_destination["Atlantic"] == True and flow_destination["Pacific"] == True:
                cells_that_drain_into_both.append(flow_destination["cell_position"])
        return cells_that_drain_into_both

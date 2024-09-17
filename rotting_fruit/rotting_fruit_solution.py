class Solution:
    @classmethod
    def is_new_position_the_previous_position(self, new_position, previous_position):
        if (new_position[0] == previous_position[0]) and (new_position[1] == previous_position[1]):
            return True
        else:
            return False

    @classmethod
    def is_new_position_in_grid(self, row_count, column_count, new_position):
        if new_position[0] < 0:
            return True
        if new_position[1] < 0:
            return True
        if new_position[0] > row_count-1:
            return True
        if new_position[1] > column_count-1:
            return True
        return False

    @classmethod
    def rot_propagation_by_position_index_from_position(self, column_count, position):
        return (position[0] * column_count) + position[1]

    @classmethod
    # Computational complexity is, at worst, (R x C)x T where R is Row count, C is column count and T is the number of zeros identified in the matrix.
    def evaluate_position_against_rules(self, grid, row_count, column_count, new_position, previous_position, distance_traversed, rot_propagation_by_position):
        # If new position is not off the edge
        if self.is_new_position_in_grid(row_count, column_count, new_position) == False:
            # If new position is not the previous position
            if self.is_new_position_the_previous_position(new_position, previous_position) == False:
                if grid[new_position[0]][new_position[1]] == 1:
                    # Check the value currently assigned to it:
                    new_position_current_propagation_distance = rot_propagation_by_position[self.rot_propagation_by_position_index_from_position(column_count, new_position)]
                    if new_position_current_propagation_distance == 0:
                        #ab. and its current rot_propagation_by_position value is zero -> update the rot_propagation_by_position with the value, and recurse
                        return True
                    if new_position_current_propagation_distance >= distance_traversed +1:
                        #ac. or its current rot_propagation_by_position value is the same or higher than the current distance traversed +1 -> update the rot_propagation_by_position with the value, and recurse
                        return True
        return False
    
    @classmethod
    # Computational complexity is R x C where R is row count and C is column count.
    def find_rotten_fruits_and_count_fresh_fruits(self, row_count, column_count, grid):
        current_row = 0
        current_column = 0
        fresh_fruit_count = 0
        rotten_fruits = []
        rot_propagation_by_position = [] # This is a flattened array to allow for easy completion tracking.
        while current_row < row_count:
            while current_column < column_count:
                if grid[current_row][current_column] == 2:
                    rotten_fruits.append([current_row, current_column])
                if grid[current_row][current_column] == 1:
                    fresh_fruit_count+=1
                rot_propagation_by_position.append(0)
                current_column+=1
            current_row+=1
            current_column = 0
        return rotten_fruits, rot_propagation_by_position, fresh_fruit_count

    @classmethod
    def propagate_rot(self, row_count, column_count, grid, current_position, previous_position, distance_traversed, rot_propagation_by_position):
        current_value = grid[current_position[0]][current_position[1]]
        # Check adjacent squares in sequence
        # Check Left
        new_position = [current_position[0], current_position[1]-1]
        if self.evaluate_position_against_rules(grid, row_count, column_count, new_position, previous_position, distance_traversed, rot_propagation_by_position) == True: 
            # Set the value of the rot_propagation_by_position for this index to distance_traversed + 1
            rot_propagation_by_position[self.rot_propagation_by_position_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, rot_propagation_by_position)
        
        # Check Up
        new_position = [current_position[0]-1, current_position[1]]
        # If new position is not off the edge
        if self.evaluate_position_against_rules(grid, row_count, column_count, new_position, previous_position, distance_traversed, rot_propagation_by_position) == True: 
            # Set the value of the rot_propagation_by_position for this index to distance_traversed + 1
            rot_propagation_by_position[self.rot_propagation_by_position_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, rot_propagation_by_position)

        # Check Right
        new_position = [current_position[0], current_position[1]+1]
        if self.evaluate_position_against_rules(grid, row_count, column_count, new_position, previous_position, distance_traversed, rot_propagation_by_position) == True: 
            # Set the value of the rot_propagation_by_position for this index to distance_traversed + 1
            rot_propagation_by_position[self.rot_propagation_by_position_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, rot_propagation_by_position)
        
        # Check Down
        new_position = [current_position[0]+1, current_position[1]]
        if self.evaluate_position_against_rules(grid, row_count, column_count, new_position, previous_position, distance_traversed, rot_propagation_by_position) == True: 
            # Set the value of the rot_propagation_by_position for this index to distance_traversed + 1
            rot_propagation_by_position[self.rot_propagation_by_position_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, rot_propagation_by_position)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])
        rotten_fruits, rot_propagation_by_position, fresh_fruit_count = self.find_rotten_fruits_and_count_fresh_fruits(row_count, column_count, grid)
        for index in rotten_fruits:
            self.propagate_rot(row_count, column_count, grid, index, index, 0, rot_propagation_by_position)
        
        max_rot_propagation_time = 0
        rotted_fruit_count = 0
        for value in rot_propagation_by_position:
            if value > 0:
                rotted_fruit_count+=1
            if value > max_rot_propagation_time:
                max_rot_propagation_time = value
        if rotted_fruit_count == fresh_fruit_count:
            return max_rot_propagation_time
        else:
            return -1
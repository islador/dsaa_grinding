class fruit:
    def __init__(self, position):
        self.position = position
        self.rotten = False
        self.fresh = True
        self.distance_to_rotten = 0

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
    def storage_array_index_from_position(self, column_count, position):
        return (position[0] * column_count) + position[1]

    @classmethod
    # Computational complexity is, at worst, (R x C)x T where R is Row count, C is column count and T is the number of zeros identified in the matrix.
    def evaluate_position(self, grid, row_count, column_count, new_position, previous_position, distance_traversed, storage_array):
        # If new position is not off the edge
        if self.is_new_position_in_grid(row_count, column_count, new_position) == False:
            # If new position is not the previous position
            if self.is_new_position_the_previous_position(new_position, previous_position) == False:
                if grid[new_position[0]][new_position[1]] == 1:
                    # Check the value currently assigned to it:
                    new_position_current_propagation_distance = storage_array[self.storage_array_index_from_position(column_count, new_position)]
                    if new_position_current_propagation_distance == 0:
                        #ab. and its current storage_array value is zero -> update the storage_array with the value, and recurse
                        return True
                    if new_position_current_propagation_distance >= distance_traversed +1:
                        #ac. or its current storage_array value is the same or higher than the current distance traversed +1 -> update the storage_array with the value, and recurse
                        return True
        return False
    
    @classmethod
    # Computational complexity is R x C where R is row count and C is column count.
    def find_rotten_fruits_and_count_fresh_fruits(self, row_count, column_count, grid):
        current_row = 0
        current_column = 0
        fresh_fruit_count = 0
        rotten_fruits = []
        storage_array = []
        while current_row < row_count:
            while current_column < column_count:
                if grid[current_row][current_column] == 2:
                    rotten_fruits.append([current_row, current_column])
                if grid[current_row][current_column] == 1:
                    fresh_fruit_count+=1
                storage_array.append(0)
                current_column+=1
            current_row+=1
            current_column = 0
        return rotten_fruits, storage_array, fresh_fruit_count

    @classmethod
    def propagate_rot(self, row_count, column_count, grid, current_position, previous_position, distance_traversed, storage_array):
        current_value = grid[current_position[0]][current_position[1]]
        # Check adjacent squares
        # Check Left
        new_position = [current_position[0], current_position[1]-1]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed, storage_array) == True: 
            # Set the value of the storage_array for this index to distance_traversed + 1
            storage_array[self.storage_array_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, storage_array)
        
        # Check Up
        new_position = [current_position[0]-1, current_position[1]]
        # If new position is not off the edge
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed, storage_array) == True: 
            # Set the value of the storage_array for this index to distance_traversed + 1
            storage_array[self.storage_array_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, storage_array)

        # Check Right
        new_position = [current_position[0], current_position[1]+1]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed, storage_array) == True: 
            # Set the value of the storage_array for this index to distance_traversed + 1
            storage_array[self.storage_array_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, storage_array)
        
        # Check Down
        new_position = [current_position[0]+1, current_position[1]]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed, storage_array) == True: 
            # Set the value of the storage_array for this index to distance_traversed + 1
            storage_array[self.storage_array_index_from_position(column_count, new_position)] = distance_traversed + 1
            # Recurse
            self.propagate_rot(row_count, column_count, grid, new_position, current_position, distance_traversed+1, storage_array)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])
        rotten_fruits, storage_array, fresh_fruit_count = self.find_rotten_fruits_and_count_fresh_fruits(row_count, column_count, grid)
        for index in rotten_fruits:
            self.propagate_rot(row_count, column_count, grid, index, index, 0, storage_array)
        max_rot_propagation = 0
        rotted_fruit_count = 0
        for value in storage_array:
            if value > 0:
                rotted_fruit_count+=1
            if value > max_rot_propagation:
                max_rot_propagation = value
        if rotted_fruit_count == fresh_fruit_count:
            return max_rot_propagation
        else:
            return -1
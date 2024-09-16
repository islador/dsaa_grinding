class Solution:
    @classmethod
    # Computational complexity is R x C where R is row count and C is column count.
    def find_treasures(self, row_count, column_count, grid, treasures):
        current_row = 0
        current_column = 0
        while current_row < row_count:
            while current_column < column_count:
                if grid[current_row][current_column] == 0:
                    treasures.append([current_row, current_column])
                current_column+=1
            current_row+=1
            current_column = 0

    @classmethod
    # Computational complexity is, at worst, (R x C)x T where R is Row count, C is column count and T is the number of zeros identified in the matrix.
    def evaluate_position(self, grid, row_count, column_count, new_position, previous_position, distance_traversed):
        # If new position is not off the edge
        if self.is_new_position_in_grid(row_count, column_count, new_position) == False:
            # If new position is not the previous position
            if self.is_new_position_is_the_previous_position(new_position, previous_position) == False:
                # If new position's value is the same or higher than the distance traversed from the origin zero
                if grid[new_position[0]][new_position[1]] >= distance_traversed + 1:
                    # If the current value of the new_position is less than the distance of that position from the origin zero
                    return True
        return False

    @classmethod
    def update_grid_square_distance_to_treasure(self, row_count, column_count, grid, current_position, previous_position, distance_traversed):
        current_value = grid[current_position[0]][current_position[1]]
        # Check adjacent squares
        # Check Left
        new_position = [current_position[0], current_position[1]-1]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed) == True: 
            # Set the value to the distance it is from the origin zero
            grid[new_position[0]][new_position[1]] = distance_traversed + 1
            # Recurse
            self.update_grid_square_distance_to_treasure(row_count, column_count, grid, new_position, current_position, distance_traversed+1)
        
        # Check Up
        new_position = [current_position[0]-1, current_position[1]]
        # If new position is not off the edge
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed) == True: 
            # Set the value to the distance it is from the origin zero
            grid[new_position[0]][new_position[1]] = distance_traversed + 1
            # Recurse
            self.update_grid_square_distance_to_treasure(row_count, column_count, grid, new_position, current_position, distance_traversed+1)

        # Check Right
        new_position = [current_position[0], current_position[1]+1]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed) == True: 
            # Set the value to the distance it is from the origin zero
            grid[new_position[0]][new_position[1]] = distance_traversed + 1
            # Recurse
            self.update_grid_square_distance_to_treasure(row_count, column_count, grid, new_position, current_position, distance_traversed+1)
        
        # Check Down
        new_position = [current_position[0]+1, current_position[1]]
        if self.evaluate_position(grid, row_count, column_count, new_position, previous_position, distance_traversed) == True: 
            # Set the value to the distance it is from the origin zero
            grid[new_position[0]][new_position[1]] = distance_traversed + 1
            # Recurse
            self.update_grid_square_distance_to_treasure(row_count, column_count, grid, new_position, current_position, distance_traversed+1)

            

    @classmethod
    def is_new_position_is_the_previous_position(self, new_position, previous_position):
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

    # Total complexity should be R x C x T + 1x(R x C)
    # There may be optimizations for 
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row_count = len(grid)
        column_count = len(grid[0])
        treasures = []
        self.find_treasures(row_count, column_count, grid, treasures)
        for index in treasures:
            print(f"Index: {index}")
            self.update_grid_square_distance_to_treasure(row_count, column_count, grid, index, index, 0)
import copy
#Game of life
#'*' to represent dead
#'O' to represent alive.

#Rules for the Game of Life
#1.) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#2.) Any live cell with two or three live neighbours lives on to the next generation.
#3.) Any live cell with more than three live neighbours dies, as if by overpopulation.
#4.) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

num_columns = 10
num_rows = 10
num_timesteps = 10

initial_grid = []
for row in range(num_rows):
    current_row = []
    for col in range(num_columns):
        current_row.append('*')
    initial_grid.append(current_row)

initial_grid[1][3]='O'
initial_grid[1][4]='O'
initial_grid[1][5]='O'


# for row in initial_grid:
#     print(row)

current_grid = copy.deepcopy(initial_grid)
initial_grid[0][0]='O'

for row in current_grid:
    print(row)

for timestep in range(num_timesteps):
    #We need to update the current grid into a new grid
    #using the 4 rules for the Game of Life.
    #Then we need to set the current grid to be the new grid.
    #The repeat.

    new_grid = copy.deepcopy(current_grid)

    for row in range(num_rows):
        for col in range(num_columns):
            neighbors = []
            for index_i in [-1,0,1]:
                for index_j in [-1,0,1]:
                    if row+index_i>=0 and row+index_i<num_rows and col+index_j<num_columns and col+index_j>=0 and current_grid[row+index_i][col+index_j] == 'O' and not index_i == index_j ==0:
                        neighbors.append([index_i,index_j])
            number_of_live_neighbors = len(neighbors)
            if number_of_live_neighbors<2:
                new_grid[row][col] = "*"
            elif number_of_live_neighbors ==2:
                new_grid[row][col] = current_grid[row][col]
            elif number_of_live_neighbors > 3:
                new_grid[row][col] = '*'
            else:
                new_grid[row][col] = 'O'
    for row in current_grid:
        print(row)

for row in current_grid:
    print(row)

for timestep in range(num_timesteps):
    #We need to update the current grid into a new grid
    #using the 4 rules for the Game of Life.
    #Then we need to set the current grid to be the new grid.
    #The repeat.

    new_grid = copy.deepcopy(current_grid)

    for row in range(num_rows):
        for col in range(num_columns):
            neighbors = []
            for index_i in [-1,0,1]:
                for index_j in [-1,0,1]: #quadruply nested loops are considered bad.
                    if row+index_i>=0 and row+index_i<num_rows and col+index_j<num_columns and col+index_j>=0 and current_grid[row+index_i][col+index_j] == 'O' and not index_i == index_j ==0: #This line is way too complicated.
                        neighbors.append([index_i,index_j])
            number_of_live_neighbors = len(neighbors)
            if number_of_live_neighbors<2:
                new_grid[row][col] = "*"
            elif number_of_live_neighbors ==2:
                new_grid[row][col] = current_grid[row][col]
            elif number_of_live_neighbors > 3:
                new_grid[row][col] = '*'
            else:
                new_grid[row][col] = 'O'
    for row in current_grid:
        print(row)
    print("---Next Generation---")
    current_grid = copy.deepcopy(new_grid)

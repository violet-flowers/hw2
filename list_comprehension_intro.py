import random #allows us to draw random numbers between 0 and 1 using random.random()

def initialize_game(size, probability):
    '''
    inputs: size: a non-negative integer that defines the length and width of the grid.
            probability: a number between 0 and 1 that is the probability of each cell starting alive.
    outputs: a list of lists of strings "*" (for dead) "O" (for alive) 
            where each value is chosen randomly with the probability in the input.
    side-effects: None
    '''
    starting_point_for_life = [['*' if random.random()>probability  else 'O' for col in range(size)] for row in range(size)]
    return starting_point_for_life

def update_cell(grid,cell):
    #inputs: grid is a doubly nested list of '*' and 'O'.
    #        cell is a list [i,j], where cell=grid[i][j].
    #outputs: "*" if the cell should be dead after applying the game rules.
    #         "O" if the cell should be alive after applying the game rules.
    #side-effets: None

def update_game(current_grid):
    #input: The grid (doubly nested list of '*' and 'O') before applying the game step.
    #output: The grid after applying a game step.
    #side_effect: None

    #Go through each cell of the grid and update each cell.


initial_game= initialize_game(10,0.2)
for row in initial_game:
    print(row)


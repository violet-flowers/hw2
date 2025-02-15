#Game of life
#'*' to represent dead
#'O' to represent alive.

#Rules for the Game of Life
#1.) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#2.) Any live cell with two or three live neighbours lives on to the next generation.
#3.) Any live cell with more than three live neighbours dies, as if by overpopulation.
#4.) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#Question: If you pick a probability, then you can start the game of life 
#by choosing each cell to be alive with probabilty p and dead otherwise,
#We can get a number: the average amount of time before the game start repeating.
#Which probability gives the greatest average amount of time before repeating?

#Concepts that we will see:

#List comprehensions
#Functions
#Dictionaries {key: value}. {prob: average time until the game repeats}

import random #allows us to draw random numbers between 0 and 1 using random.random()
import copy

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

def count_neighbors(cell,grid):
    #inputs: cell is a tuple (i,j) where i,j are nonnegative integers,
    #        grid is a list of lists of '*' and 'O'.
    #outputs: a integer, the number of live neighbors ('O') of cell in Grid.
    #side-effects: None
    def is_valid_index(i,j):
        #inputs: i,j are indices (integers)
        #ouputs: True/False depending on whether i,j is a valid index on the grid.
        if 0<=i<len(grid) and 0<=j<len(grid):
            return True
        else: 
            return False
    neighbors = [(cell[0]+index_i,cell[1]+index_j) for index_i in [-1,0,1] for index_j in [-1,0,1] if is_valid_index(index_i,index_j) and not index_i==index_j==0]
    print(neighbors)
    return len(neighbors)
count_neighbors((1,1),[['*','*'],['*','*']])
def update_cell(cell,grid):
    #inputs: grid is a doubly nested list of '*' and 'O'.
    #        cell is a list [i,j], where cell=grid[i][j].
    #outputs: "*" if the cell should be dead after applying the game rules.
    #         "O" if the cell should be alive after applying the game rules.
    #side-effects: None
    
    #To update a cell, we call count_neighbors to get the number of neighbors,
    #Then we apply the rules of the game of life.
    
    num_live_neighbors = count_neighbors(cell, grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if num_live_neighbors<2: #rule 1
                return('*')
            elif num_live_neighbors ==2:
                return(grid[row][col])
            elif num_live_neighbors > 3: #rule 4
                return('*')
            else: #number_of_live_neighbors == 3
                return('O')


def update_game(current_grid):
    #input: The grid (doubly nested list of '*' and 'O') before applying the game step.
    #output: The grid after applying a game step.
    #side_effect: None

    #Go through each cell of the grid and update each cell.
    
    new_grid = current_grid #We should use copy, but let's do it incorrectly for now.
    for row in range(len(new_grid)):
        for col in range(len(new_grid[0])):
            new_grid[row][col] = update_cell((row, col),current_grid)
    return new_grid

def game_loop(initial_grid):
    #input is a initial grid, doubly nested list of '*' and 'O'.
    #ouput is the number of steps until the game repeats itself.
    #side-effects: None

# initial_game= initialize_game(10,0.2)
# for row in initial_game:
#     print(row)


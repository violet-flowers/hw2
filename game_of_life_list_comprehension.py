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


starting_point_for_life = [['*' if row >=k or col >=k else 'O' for col in range(n)] for row in range(n)]
for row in starting_point_for_life:
    print(row)
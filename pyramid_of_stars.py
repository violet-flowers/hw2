'''We want to print out a pyramid of stars like this:
    *
   * *
  * * *
 * * * *
'''
#First let's do something simpler: a square of stars.
#We use one print statement for each row.
#We use a loop to go through all n rows.
n=7
for row in range(n): #row goes through the numbers 0, 1, 2, ... n-1.
    row_of_stars_list=[]
    for col in range(n): # col goes through 0,1, .., n-1
        row_of_stars_list += ["*"]
    #convert the list of strings into a string.
    row_of_stars_list="".join(row_of_stars_list)
    #print(row_of_stars_list)

#There is a better way to create the square of stars.
for row in range(n):
    print("*"*n) # string * n repeats the string n times.

#The pyramid of stars:

for row in range(n):
    print(" "*(n-1-row) +"* "*row + "*")

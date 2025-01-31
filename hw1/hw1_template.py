#This homework focuses on lists and loops. I believe these are the most important concepts in Python.

#You may work together, but you must type your own code.
#You should only use LLMs if you get stuck. If you choose to consult an LLM, then ask the machine follow-up questions about its solution.

#1.) The diamond of stars. 

def diamond_of_stars(n):
    #Input: n is a nonnegative integer.
    #Outputs: None
    #SideEffect: prints a diamond of stars whose longest row contains n stars.
    #For example, when n=3, we see this output:
    '''
  *
 * *
* * *
 * *
  *
    '''
    pass

#2.) The weird sequence of numbers.

def weird_sequence(n):
    #input: n is a natural number.
    #Outputs: A list of numbers continuing the pattern: 1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300, ... and so forth.
    #The list should NOT include 10^n, but end just before, at 9*10^(n-1)
    #Specifically, I mean OEIS-A037124, available here: https://oeis.org/A037124
    #For example, when n=2, the output is [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90]
    '''
    Hint: One solution is to use a doubly nested loop, appending the numbers one-by-one. 
    The exponent operator in python is expressed using **. For example, 100==10**2
    '''
    pass
    #Your last line should be return my_list
#3.) Count repeated occurences of letters.

def count_double_letters(input_string):
    #Input: input_string is a string. We assume basic characters: lowercase letters, spaces and numbers.
    #Output: The number of times a character is followed by itself.
    #For example, when run on "raccoons appear, skiing weekly." it should output 5.
    #When run on "hmmm...?", it should return 4.
    #When run on "double  spaced  words", it should return 2.
    pass
    #your last line should be return my_answer

#Make sure you name your file homework1.py
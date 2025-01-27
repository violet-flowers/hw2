#This file explains how loops work
my_string = "this is my string" #We've seen strings
my_list= list("this is my list") #We've seen loops
print(my_string)
print(my_list)
#The "for" loops allow us to step through the string, letter by letter.
#They also allow us to step through the list, element by element.

# for letter in my_string:
#     print(letter) #This prints out the letters of my_string one by one.

# for l in my_list:
#     print(l)

#More generally, you can use "for" loops to go through any "iterable" element by element.
Z = range(10) #range is an example of something that is iterable (so you can loop over it) but is not a list or string.
# print(type(Z))
# for item in range(10):
#     print(item)

#range(10) should be though of as [0,1,2,...9], but technically it's not a list, it is its own type.

'''Example: Fizz buzz
Interview question: print out the prime numbers between 0 and 100.
'''
a = 10
b = 9

#Want some way to test if a is even or odd.
print((a/2) == int(a/2)) #the == symbol checks if the two sides are equal
print((b/2) == int(b/2))
print(int(b/2))
#There is a better way to check if a number is odd or even:
print(12%5) #Useing the modulo operator which takes the remainder after division.


# for number in range(101):
#     if number %2 == 0: #Checks if the number is even.
#         print(number)

#Next, we need to check if a number is prime or not.
a = 50
#We check every number between 2 and 49 to see if a is divisible by that number.
for factor in range(2,a):
    if a % factor == 0:
        print("a is not prime. It has a factor of ", factor)
        break #The break statement says "stop doing the for loop."

for number in range(2,101): #outer loop loops over all numbers between 0 and 100.
    is_prime = True
    for factor in range(2,number): #inner loop loops over all numbers 2 to number -1
        if number % factor == 0:
            is_prime = False
    if is_prime:
        print(number)

#enumerate allows you to loop through a list and keep an index of where you are in the list.
my_list = ["a","b",7]
for index, value in enumerate(my_list):
    print(index, value)
for index, value in enumerate(range(10)):
    print(index, value)
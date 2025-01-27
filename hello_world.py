'''
Comments:

Longer comments can be enclosed by 3 quotes like this.
'''
#Shorter cmments in python are indicated by a '#' like this

#The first program anyone writes in any language is the "hello world" program.
print("hello world") #print is a function that takes in a string and prints the string to the terminal.

#Python allows us to use variables to represent objects.
x="hello" #set the variable x to be the string "hello".
print(x)

y= 5 #variables can also be integers.
z=10
print(y+z)

#Types: Everything in Python has a type, like "string" or "int".

print(type(print(type(x))))

print(print(type(x)))
 
none_variable = None

print(type(none_variable))

#types: strings: eg "hello", int: eg 5, Nonetype, eg None.

#Each type has its own operations available.

x="john said, \"hello\" to me" #re-assigns x to be "a"
y="\\" #re-assigns y to be "b"

print(x+y) #we can add strings, also called concatenation.


#----Strings----#
x="this is a string"
print(x)
y="this is another string"
x+y #This is called concatenation.
print(x+y)

z = str(reversed(x))
print(type(z))
print(z)

#Apparently you're not supposed to use reversed to reverse a string, but only a list.

#If you actually want to reverse a string, you should use slicing.

print(x[0]) #Should print 't', which is the 0th letter of x.
print(len(x)) #You can use the length function to check the length of the string.
print(x[15], x[14], x[13] ) #This starts to reverse the string x, but it's too hard-coded.
#--#
x = "thisisastring"
print(x[3:10]) #This does include x[3] up to x[9], and does not include x[10]. The length of this slice is 10-3=7.
print(x[3:10:2])
#---Negative numbers in the slice ---# 
print(x[-1]) #Negative numbers start counting from the end. So x[-1] is the last letter.
print(x[4:-1])
print(x[-4:-1])
print(x[10:3]) #Prints the empty string, ""
print(x[5:5]) #Prints the empty string, ""
print(x[::-1])
print(x) #List slicing does not mutate the arguments.


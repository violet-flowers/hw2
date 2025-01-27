'''
Lists are "container objects" that you can put other objects into.
'''
example_list = [4,2,"a"] #Lists are enclosed in square brackets.
list_of_strings = ["a","b","c","d","e"]
#Indexing lists works exactly like indexing strings.
print(list_of_strings[1])
print(list_of_strings[1:])
print(list_of_strings[::-1])
#Join allows you take a list of strings and join them into a single string.
print("-".join(list_of_strings))

#Operations on lists: append and extend
#Append puts another item at the end of a list.
list_of_strings.append("f")
print(list_of_strings) #prints ['a', 'b', 'c', 'd', 'e', 'f']
print(list_of_strings.append("f")) #prints None. This is because append modifies list_of_strings, it doesn't return anything.

sum_list = list_of_strings + example_list #Addition of lists concatenates them. It puts one after the other.
print(sum_list)

print(list_of_strings + example_list) #prints ['a', 'b', 'c', 'd', 'e', 'f', 'f', 4, 2, 'a']
#The + operator concatenates the two strings and returns a new string. The input strings are unchanged.
print(list_of_strings)
new_list = list_of_strings.extend(example_list)
#Extend modifies the string that it's called on to have the argument appended.
print(list_of_strings) #prints ['a', 'b', 'c', 'd', 'e', 'f', 'f', 4, 2, 'a']

#What is the difference between append and extend?
x = ['a','b','c']
x.extend([54]) #Extend throws an error unless it is given a single list.
y = ['a','b','c']
y.append(54) #Append expects a single object as an argument.
print("Print on line 34", x,y)
#A key difference between lists and strings in Python is that strings are immutable. They cannot be changed.
#On the other hand, lists are mutable and can be changed.

#Strings are immutable:
ex_string= "This is a string"
#ex_string[0]="t" #This gives an error because you can't modify strings.
ex_string_list = list(ex_string)
print(ex_string_list)
ex_string_list[0] = "t"
print(ex_string_list) #This works because lists are mutable and can be changed.

#Lists of lists. We can put lists into lists.
nested_list = [[1,5],["six", "hi", None],None]
print(nested_list[1][1])
#How to access the word "hi" in nested_list using indexing?

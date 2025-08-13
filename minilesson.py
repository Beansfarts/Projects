
#1. Create a function that creates a new list based off user input. 
# The function should have a parameter variable that receives how long the list is
# It should have a for loop to add each item to list
# It will return the list for the user to use outside the function
# Print your list with a for loop

#Version 4

# 2. Create a function that removes copies of the same string within a list.
# The function will have a parameter that receives the list
# The function will return the new list
#Print your new list






''' 
input() - prints and receives and returns user input
len() - receives parameter and returns length of object
 .append() - receives parameter and adds the data to list 
 == - something equals something
 != - oposite of ==

for i in range(x):

This for loop will run x amount of times
i tells you which iteration you are on (eg.. 0,1,2,3)

list = ["String", 0, True]


'''

































def makeList(x):
    list = []
    for i in range(x):
        list.append(input(""))
    return list    


newList = makeList(3)

for i in newList:
    print(1)
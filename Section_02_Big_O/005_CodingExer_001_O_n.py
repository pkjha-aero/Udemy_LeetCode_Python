# Code for O (n)

## WRITE THE PRINT_ITEMS FUNCTION HERE ##
#                                       #
#                                       #
#                                       #
#                                       #
#########################################

def print_items(n):
    # print_items accepts one argument 'n'. It will print
    # a sequence of numbers from 0 up to, but not including, 'n'.
    
    for i in range(n):
        # A for loop is initiated with 'i' iterating over
        # the sequence of numbers produced by range(n).
        # For each iteration, 'i' takes the current number in
        # the sequence from 0 up to but not including 'n'.
        
        print(i)
        # Inside the loop, print(i) is called. This prints
        # the current value of 'i' to the console. This
        # action is performed 'n' times due to the for loop,
        # resulting in printing of numbers from 0 to 'n - 1'.           
              
print_items(10)                  
 

#########################################                 
#Other possible solutions:

#There are a few different ways the for loop in your print_items function could be rewritten. Here are a few examples:

'''
Using a while loop instead of a for loop:

def print_items(n):
    i = 0
    while i < n:
        print(i)
        i += 1
'''
'''
Using a for loop with an explicitly defined list:

def print_items(n):
    for i in list(range(n)):
        print(i)
'''
'''
Using a for loop with iterator:

def print_items(n):
    for i in iter(range(n)):
        print(i)
'''
'''
Using list comprehension (though this isn't recommended if the goal is just to print the items, as it unnecessarily creates a list of None values):

def print_items(n):
    _ = [print(i) for i in range(n)]
'''
'''
Using the map function. This method is also not recommended for printing purposes, as it's less readable and efficient than a simple loop, and it also unnecessarily creates a list of None values:

def print_items(n):
    _ = list(map(print, range(n)))
'''
#Each of these alternative solutions achieves the same result as the original function, but the simplest and most straightforward solution is the original for loop.

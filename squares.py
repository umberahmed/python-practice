# Create a function that will sq a list of numbers and return the numbers as a list

def sq(n):
    """Function will square any number that is passed as an argument"""
    return n**2;

list = map(sq, [1, 2, 3, 4]) # used map function, passed in sq function and list of integers to return list of squared integars


print(*list)
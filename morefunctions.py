def display_message():
    """Function prints a welcome greeting"""
    print "In this chapter I am learning about functions."

def favorite_book(book):
    """Function prints favorite book"""
    print("My favorite book is " + book.title() + ".")

def distance_from_zero(number):
    """Function to determine the distance from zero"""
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "Nope!"

display_message()                           # call function from above, nothing to add for arguments
favorite_book("Chicken Soup For The Soul")  # call funtion and pass in book name for 1 argument
print(distance_from_zero(-10))              # print function and pass in negative number to test abs

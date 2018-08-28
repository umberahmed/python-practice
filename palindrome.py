# Create a function to determine if a string is a palindrome.

def check_palindrome(inputString):
    """Function checks to see if input string is palindrome."""
    return inputString[::-1] == inputString

print check_palindrome("aaa")
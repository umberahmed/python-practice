def add_odd_numbers(numbers):
    sum = 0;
    # loop through the list of numbers
    for num in numbers:
        # Identify odd numbers
        # 3 % 2 = 1
        # 4 % 2 = 0
        if num % 2 == 1:   # ==, > >=, <, <=, !=  ;  * + - / %
            # add them
            sum += num
    # return the sum
    return sum

print add_odd_numbers([1, 2, 3, 4, 5, 6, 7, 7])
#IF ELSE python practice

people = 30
cars = 40
trucks = 15

if cars > people:                       # True, statement will print
    print "We should take the cars."
elif cars < people:                     # False, statement will not print
    print "We should not take the cars."
else:
    print "We can't decide."            # because 1st statement is True, statement will not be evaluated

if trucks > cars:                       # False, statement will not print
    print "That's too many cars."
elif trucks < cars:                     # True, statement will print
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."      # because 2nd statement is True, else will not evaluate

if people > trucks:
    print "Alright, let's just take the trucks."    # True, statement will print
else:
    print "Fine, let's stay home then." # conditional is True, statement will print

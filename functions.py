def shut_down(s):
    """Function prompt to shutdown using nested if elif conditionals"""
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

shut_down("yes")
print shut_down("no")
print shut_down(345)

def make_shirt(size, message):
    """Function returns shirt sizes and message to display on shirt"""
    print("You have requested a shirt size of " + size + " and the message will read " + message)

make_shirt("small", '"Chickens are fun!"')
make_shirt(size= "large", message= '"Twinkle, Twinkle, Little Star"')

def make_shirt_lg(message, size= 'large'):
    """Function with set value to 'large' for shirts with personal message"""
    print("Your shirt will be a size " + size + " and will read " + message)

make_shirt_lg(message= '"I love python!"')
make_shirt_lg(message= '"Hello, World!"', size= "x-small") # reset the default value of size by passing in a new size for argument

def describe_city(city, country= "united states of america"):
    """Describes cities in the country of United States of America"""
    print("\n" + city.title() + " is a city in the country of the " + country.title() + ".")

describe_city("san francisco")
describe_city("portland")
describe_city("madrid", country= "spain")
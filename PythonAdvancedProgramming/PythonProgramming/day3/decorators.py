#cherry on the cake
#function decorates another function
#wrapper function around the functions are called as decorators

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner

@make_pretty
def vanillacake():
    print("I am the vanilla cake")

@make_pretty
def strawberrycake():
    print("i am the strawberry cake")

vanillacake()
strawberrycake()
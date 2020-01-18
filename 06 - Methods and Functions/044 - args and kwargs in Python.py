def myfunc(a, b):
    #returns 5% of the sum of a and b
    return sum((a, b)) * 0.05

print(myfunc(40, 60))

def myfunc2(a, b, c = 0, d = 0):
    #returns 5% of the sum of a and b
    return sum((a, b, c, d)) * 0.05

print(myfunc2(40, 60, 100))

#*args tuple-ként viselkedik (nem csak "args" lehet a neve, de ez a konvenció)
def myfunc3(*args):
    return sum(args) * 0.05

print(myfunc3(10, 20, 30, 40, 50, 60))

#Key-word arguments, dictionary-t vár
def myfunc4(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("I did not find any fruit here")

myfunc4(fruit='apple', veggie = 'lettuce')

def myfunc5(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunc5(10, 20, 30, fruit = "orange", food="eggs", animal = "dog")
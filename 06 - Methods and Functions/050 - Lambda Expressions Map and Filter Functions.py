def square(num):
    result = num ** 2
    return result

my_nums = [1, 2, 3, 4, 5]

# Map: végrehajt egy paraméterként kapott függvényt a paraméter tömb elemein
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names=["Andy", "Eve", "Sally"]

print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]
# Boolean-t visszaadó fügvénnyel kiszedi a hamisakat a kapott tömbből
print(list(filter(check_even, my_nums)))


square = lambda num: num ** 2
print(square(3))

print(list(map(lambda num:num**2, mynums)))

print(list(filter(lambda num:num % 2 == 0, mynums)))

print(list(map(lambda x : x[0], names)))

print(list(map(lambda x : x[::-1], names)))
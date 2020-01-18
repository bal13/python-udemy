myString = "hello"
myList = []
for letter in myString:
    myList.append(letter)

print(myList)

# Ez is ugyanaz (futásidőt sem spórol csak rövidebb)
myList = [letter for letter in myString]
print(myList)

myList = [x for x in "Hahaha"]
print(myList)

myList = [num for num in range(0, 11)]
print(myList)

myList = [num**2 for num in range(0, 11)]
print(myList)

#Csak a párosakat emeli négyzetre
myList = [x**2 for x in range(0, 11) if x % 2 == 0]
print(myList)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

myList = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        myList.append(x * y)

print(myList)

#ez is ugyanaz, de már kevésbé olvasható ki...
myList = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
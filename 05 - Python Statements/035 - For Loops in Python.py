myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in myList:
    print(num)

for num in myList:
    print('hello')

for num in myList:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Number: {num}")

list_sum = 0
for num in myList:
    list_sum = list_sum + num

print(list_sum)

for letter in "Hello world":
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

myList = [(1,2), (3,4), (5,6), (7,8)]
print(len(myList))
for item in myList:
    print(item)

#Tuple unpacking
for (a, b) in myList:
    print(a)
    print(b)
#Ugyanaz...
for a, b in myList:
    print(a)
    print(b)

for a, b in myList:
    print(b)

myList = [(1,2,3), (4,5,6), (7,8,9)]
for a, b, c in myList:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key, value in d.items():
    print(value)
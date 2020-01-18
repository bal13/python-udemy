myList = [1, 2, 3]

for num in range(10):
    print(num)

for num in range(3, 10):
    print(num)

for num in range(0, 11, 2):
    print(num)

#range egy generátor
print(list(range(0, 11, 2)))

index_count = 0
for letter in "abcde":
    print(f"At index {index_count}, the letter is {letter}")
    index_count += 1

index_count = 0
word = "abcde"
for letter in word:
    print(word[index_count])
    index_count += 1

#Tuple-t ad vissza...
word = "abcde"
for item in enumerate(word):
    print(item)

#Amit szét is lehet szedni
word = "abcde"
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

#zip is generátor, össze tud rántani tuple listába pl. listákat
myList1 = [1, 2, 3]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300, 400] # Nem dob hibát, de legrövidebb listáig megy
for item in zip(myList1, myList2, myList3):
    print(item)

print(list(zip(myList1, myList2, myList3)))

# in operátor boolean-nal tér vissza
print('x' in ['z', 'y', 'x'])
d = {"mykey": 345}
print(345 in d.values())

print("e" in "hello")

myList = [10, 20, 30, 40, 50, 100]
print(min(myList))
print(max(myList))

# function importálása libraryból
from random import shuffle
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(myList) #Nincs visszatérési értéke, az eredeti listát machinálja
print(myList)

from random import randint
print(randint(0,100))
myNum = randint(0, 100)
print(myNum)

result = input("Enter a number here: ")
print(result) #Ez mindig string lesz, tehát castolni kell!
print(type(result))

result = int(input("Enter a number here: "))
print(type(result))
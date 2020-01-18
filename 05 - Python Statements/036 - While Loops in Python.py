x = 0
while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else: # Akkor is lefut, ha a feltétel már a kezdetkor sem volt igaz!
    print("X is not less than 5")

x = [1, 2, 3]
for item in x:
    #comment
    pass #nem csinál semmit, de legalább nem száll el
print("End of my script")

myString = "Sammy"

for letter in myString:
    if letter == 'a':
        continue
    print(letter)

for letter in myString:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x) 
    x += 1
name = "Sam"
# name[0] = 'P' -> String immutability miatt nem működik
last_letters =  name[1:]
print(last_letters)
print('P' + last_letters)

x = "Hello world"
x = x + " it is beautiful outside"
print(x)
letter = 'z'
print(letter * 10)
print(2 + 5)
print('2' + '3')


x = "Hello world"
print(x.upper())
print(x.split())

x = "Hi this is a string"
print(x.split("i"))
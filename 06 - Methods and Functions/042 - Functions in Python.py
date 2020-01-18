def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input...
    OUTPUT: Hello...
    '''
    print("Hello")

def say_hello(name='NAME'):
    return "Hello " + name

result = say_hello("Zack")
print(result)

def add(n1, n2):
    return n1 + n2

result = add(20, 30)
print(result)

#Find out if a word dog is in a string
def dog_check(myString):
    return 'dog' in myString.lower()

print(dog_check("Dog ran away"))

def pig_latin(word):
    first_letter = word[0]

    #check is vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin("apple"))
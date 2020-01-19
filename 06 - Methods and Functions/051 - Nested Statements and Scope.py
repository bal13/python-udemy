x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

# LEGB rule:
# Local
# Enclosing function local
# Global (module)
# Built-in (python)

# GLOBAL
name = "THIS IS A GLOBAL STRING"

def greet():
    # ENCLOSING
    name = "Sammy"

    def hello():
        # LOCAL
        name = "I\'M A LOCAL"
        print('Hello ' + name)

    hello()

greet()
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Something is wrong")


try:
    x = 5
    y = 0

    z = x / y
except ZeroDivisionError:
    print("Zero division")
except:
    print("Something went wrong")
finally:
    print("All done")

def ask():
    while True:
        try:
            print((int(input("Please enter a number: ")))**2)
        except:
            print("That's not a number!")
            continue
        else:
            print("OK...")
            break

ask()
# one.py


def func():
    print("Func() in one.py")


print("Top level in one.py")

if __name__ == '__main__':
    #Ez szokott a futtatott fájl végén lenni, és ez után jönnek a futtatandó kódok, előtte csak definíciók
    print('One.py is being run directly')
else:
    print('One.py has been imported')
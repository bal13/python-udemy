#Olyanok mint a list, de immutable tulajdonságúak
t = (1,2,3)
myList = [1,2,3]

print(type(t))
print(len(t))

t = ('one', 2)
print(t[0])
print(t[-1])

t=('a', 'a', 'b')
print(t.count('a'))
print(t.index('a')) # Az első találat indexét adja vissza

myList[0] = 'NEW' # Működik
# t[0] = 'NEW' -- Nem működik

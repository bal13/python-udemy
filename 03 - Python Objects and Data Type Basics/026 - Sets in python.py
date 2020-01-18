mySet = set()
print(mySet)

mySet.add(1)
print(mySet)

mySet.add(2)
print(mySet)

mySet.add(2)
print(mySet) #Rendezetlen, egyedi értékek vannak benne, ezért nem megye bele mégegyszer

myList = [1,1,1,1,1,1,2,2,2,3,3,3]
set(myList)
print(myList)
print(mySet) #Rendezetlen!
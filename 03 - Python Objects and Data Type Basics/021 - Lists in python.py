#[]

my_list = [1,2,3]
print(my_list)
my_list = ["STRING", 100, 32.2]
print(my_list)
print(len(my_list))
my_list = ["one", "two", "three"]
print(my_list)
print(my_list[0])
print(my_list[1:])
another_list = ["four", "five"]
print(another_list)
print(my_list + another_list)
new_list = my_list + another_list

new_list[0] = "ONE ALL CAPS"
print(new_list) # Listák nem immutable tulajdonságúak!

new_list.append("six") # in place effect - nem kell új változó
print(new_list)

new_list.append("sevem") # in place effect - nem kell új változó
print(new_list)

new_list.pop() 
print(new_list)
print("Popped item: " + new_list.pop()) #vissza is tér a "seven értékkel"
print(new_list)

new_list.pop(0) # alapból a -1. elemet poppolja, de lehet indexelni
print(new_list)

print("\n")

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
print(new_list)
print(num_list)

new_list.sort() # in place, nem tér vissza semmivel!!! nem úgy mint a pop
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)


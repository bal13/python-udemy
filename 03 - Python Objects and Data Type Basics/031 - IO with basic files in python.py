myFile = open('text.txt')
print(myFile.read())
print(myFile.read()) # Üres String meg a kurzon a fájl végén van
myFile.seek(0) # Visszaáll a kurzor a fájl elejére
print(myFile.read())
myFile.seek(0)
content = myFile.read()
print(content)

myFile.seek(0)
print(myFile.readlines()) # Soronkénti tömb
myFile.close()

#Windows alatt "\\"" a mappaelválasztó, mac és linux alatt "/"
myFile = open("d:\\Learn\Python\\python-udemy\\03 - Python Objects and Data Type Basics\\text.txt")
myFile.close()

#Ha így nyitjuk meg a fájlt, nem kell bajlódnunk a close-zal
with open('text.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

#Megnyitás olvasásra
with open('text.txt', mode='r') as myFile:
    contents = myFile.read()

#Megnyitás (felül)írásra (ilyenkor az olvasásra hibát dob)
# with open('text.txt', mode='w') as myFile:
#     contents = myFile.read()

# #Megnyitás hozzáfűzésre (ilyenkor az olvasásra hibát dob)
# with open('text.txt', mode='a') as myFile:
#     contents = myFile.read()

#mode = 'r' is read only
#mode = 'w' is write only (will overwrite files or create new!)
#mode = 'a' is append only (will add on to files)
#mode = 'r+' is reading and writing
#mode = 'w+' is reading and writing (will overwrite files or create new!)

with open('my_new_file.txt', mode = 'r') as f:
    print(f.read())

with open('my_new_file.txt', mode = 'a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file.txt', mode = 'r') as f:
    print(f.read())

with open('sdasd.txt', mode = 'w') as f:
    f.write('I CREATED THIS FILE')

with open('sdasd.txt', mode = 'r') as f:
    print(f.read())

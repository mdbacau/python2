myfile = open('files/test.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
contents = myfile.read()
print(contents)

# We can get output as a list which we can loop into
myfile.seek(0)
print(myfile.readlines())
# PEP8 Best practices. File still runs in background, we need to close
myfile.close()

# New method for opening files, doesn't require myfile.close() anymore
with open('files/test.txt') as my_new_file:
    contents2 = my_new_file.read()

print(contents2)

# Different options, such as mode='r' or 'w'; usually assigning permissions to scripts
# mode = 'r' = read only
# mode = 'w' = write only
# mode = 'a' = append only
# mode = 'r+' = read and write
# mode = 'w+' = read and write + overwrite / create new file
with open('files/doubletest.txt',mode='r') as functie_read:
    print(functie_read.read())

with open('files/thirdtest.txt',mode='a') as functie_append:
    functie_append.write('FOR O FOR\n')
with open('files/thirdtest.txt',mode='r') as functie_append:
    print(functie_append.read())

with open('files/created.txt',mode='w') as functie_write:
    functie_write.write('I CREATED THIS')
with open('files/created.txt',mode='r') as functie_write:
    print(functie_write.read())

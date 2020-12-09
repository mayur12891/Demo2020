
# File read write
# w - write
# r - read
# r+ - read and write
# a - append
# Below code will create/write a new file and read a file
# By default it will save the file in same directory location

my_file = open("firstfile.txt", "w")
my_file.write("this is first line" + "\n")
my_file.write("this is second line")
my_file.close()

file = open("firstfile.txt", "r")
print(file.read())          #this will read full file
#print(file.readline())     #this will read code line by line
#print(file.readlines())    #this will store the content in a list
file.close()

a = "mayur"
b = 'mayur'
c = 'c'
print(a)
print(b)

# Check if a is equal to b and return boolean
print(a == b)
print(a is c)

# Variables can also be assigned in below manner
x = y = z = 10
print(x, y, z)
p, q, r = 1, 2, 3
print(p, q, r)
d = 10
e = 20.5
print(d + e)
print(d / e)

# bool is an inbuilt function using which we can get boolean value for something.
a = 0
b = 1
c = ""
print(bool(a))
print(bool(b))
print(bool(c))

# Accessing characters in a string
string = "mayur"
first = string[1]
print(first)

# Simple string methods
string1 = "My name is Mayur"
print(string1.upper())
print(string1.lower())
print(len(string1))
# str is keyword used to add int + string
print("Length of the string is: " + str(16))

# Concatinate two strings
string2 = 'Hello'
string3 = 'World'
print(string2 + " " + string3)

# Level 2 string methods
# In-built replace method
string4 = '1 a 2 a 3 a'
print(string4.replace('a','A'))
print(string4.replace('a','B',2))

# Sub-strings
# remember: starting index is inclusive and ending index is exclusive in python for sub-strings
string5 = 'AQuickBrownFoxJumpsOverTheLazyDog'
print(string5[6])
print(string5[0:5])
print(string5[3:6])
print(string5[0:10:2])
print(string5[1:])
print(string5[-1])
# below can be used to reverse a string
print(string5[::-1])

# Understanding Lists
# List is defined inside []. Dictionary is defined inside {}.
cars = ['bmw', 'Rolls', 'Audi']
print(cars)
print(cars[2])
mixlist = ['mayur', 12, 'August', 1991]
print(mixlist)
# List values can be updated
mixlist[0] = 'chhowala'
print(mixlist)

# In-built methods for lists
cars.append('Jeep')
print(cars)
cars.insert(2,'bentley')
print(cars)
cars.reverse()
print(cars)
cars.remove('Jeep')
print(cars)
print(cars.index('Rolls'))
print(len(cars))
print(cars[0:2])

# Tip to remember: Normal dictionary has word and meaning. Similarly python dictionary has key and value.
# Dictionary: It is similar to Hashmap in Java. Dictionary is similar to Lists, but data is stored in key-value pair.
# Dictionary is defined inside {}. List is defined inside [].
# key and value is seperated by :    Each key-value pair is separated by ,
# Example: {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# values can be of any datatype. Also, there is no sequence and no indexing.

# empty dictionary can also be defined to add values inside later
empty = {}
print(empty)
empty['fname'] = 'deep'
empty['lname'] = 'chh'
print(empty)

# Normal dictionary shown below
details = {'name': 'mayur', 'age': 28, 'Addr': 'Pune', 1991: 'birthyear'}
print(details)

# values of Dictionary cannot be printed using index. Use below
print(details['Addr'])
print(details['age'])
print(details[1991])
empname = details['name']
print(empname)

# Dictionary methods
print(details.keys())
print(details.values())
print(details.items())
details_copy = details.copy()
print(details_copy)
print(details.pop('name'))
print(details)
details.clear()
print(details)


"""
# Comparators
# in response we will get a boolean value
=  --> assignment operator
== --> this does comparison
!= --> not equal to
<  --> less than
>  --> greater than
<= --> less than or equal to
>= --> greater than or equal to
"""

# Tuple is exactly similar to List; difference is they are immutable
# means value cannot be changed. And it is defined using ().
my_tuple = (1, 2, 3, 3, 3, 1)
print(my_tuple)
print(my_tuple.index(3))
print(my_tuple.count(3))

# if condition
if 10 == 9:
    print('something')
else:
    print("nothing")

if 10 == 8:
    print('something')
elif 10 == 7:
    print('something')
else:
    print('Nomething')


# while loop
x = 1
while x < 10:
    print(x)
    x = x + 1
else:
    print('this is always printed')

# for loop
my_list = [1, 2, 3]
for i in my_list:
    print(i)

# In-built function range:
# range will generate sequence of numbers but will not save them in memory
# range accepts three arguments - start, stop and step
# value mentioned in stop is exclusive
# user to cast range inside a list in order to print the same
r = range(0, 11, 2)
print(list(r))

# range function is usually used in combination with for loop
# ex: if ask is to run a loop 3 times then do below
for i in range(3):
    print('this loop will print three times')

# Using return in a method
def add(n1, n2):
    sum = n1 + n2
    return sum

addition = add(2,4)
print(addition)

# Optional/Positional parameters:
# If user passes the value then those values are used, else default values are used.
def mul(n1=3, n2=6):
    print(n1*n2)

mul()

# When a method is defined with * in arguments, it means that the function can accept any number of arguments.
# instead of args, we can also give a.
def my_method(*args):
    print(args)

my_method(1, 2, 3, 'mayur', 4)

# Exception handling
# Like try n catch in Java, we have try n except in Python.
# We can have more than one expect blocks with one try block.
# In case of any exceptions, the program control will go to expect block and no error will be raised.
# Also, program execution will not stop because of exception.

# Finally in Python. Just like finally block in Java, python has else and finally block.
# When there is no exception, then else block is executed.
# What ever may the condition, finally block is always executed.

def division():
    try:
        n1 = 10
        n2 = 5
        print(n1/n2)
    except:
       print("Inside except block")
    else:
        print("Else is printed only when there is no exception")
    finally:
        print("Finally is always printed")

division()
print("print from next line of code after division method")


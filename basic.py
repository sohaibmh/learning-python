def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    elif type(value) == list:
        the_mean = sum(value) / len(value)
    else:
        return "inocrrect type"
    return the_mean


mean_list =  [2, 4, 6]
mean_dict = {"a": 2, "b": 4, "c": 6}

print(mean(mean_list))
print(mean(mean_dict))
print(mean(2))

# for loop

list_eg = ["H", "O", "S", "B"]
string_eg = "Hello"
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
dict_eg = {"London": 1, "Madrid": 2, "Lisbon": 3}

for letter in list_eg:
    print(letter)

for letter in string_eg:
    print(letter)

for color in colors:
    if isinstance(color, int):
        print(color)

for city in dict_eg.items():
    print(city)

for city in dict_eg.keys():
    print(city) 

for city in dict_eg.values():
    print(city) 


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

for value in phone_numbers.values():
    print(value.replace("+", "00"))


# while loop 

# while True:
#     username = input("Enter username: ")
#     if username == "Sohaib":
#         break
#     else:
#         continue


# List Comprehensions 

def foo(list_):
    return [i for i in list_ if i > 0 ]
    
def foo(lst):
    return [i for i in lst if  isinstance(i, int)]

def foo(lst):
    return [i*2 if i>0 else 0 for i in lst]


# Indifinite number of arguments

def foo(*args):
    return args

# File processing 

# an object gets created when you open a file
myfile = open("README.md")

# when you open a file the cursor is initially at the start of the file,
# but when you read it, the cursor goes to the end of the file,
# so if I print the below twice, for the second one it will only be an empty string
print(myfile.read())

# this removes it from memory
myfile.close()

# another way of writing the above, as a block:
with open("README.md") as myfile:
    content = myfile.read()
    print(content)

    # this would only print the first five characters
    print(content[:5])

    print(content.count("h"))

# creating a new file
# the second argument means to "write", by default it's "r" i.e. "read"
with open("fruits.txt", "w") as myfile:
    myfile.write("Mango\nBanana\nApple")   

# "a" opens the file for writing, however it won't over-write the existing content
# "+" allows the file to be read 
with open("fruits.txt", "a+") as myfile:
    myfile.write("\nGrapes")
    # this takes the cursor back to the top
    myfile.seek(0)
    content = myfile.read()
    print(content)


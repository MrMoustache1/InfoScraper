import datetime as dt

# Basic Data Types:
my_str = 'string here'
my_int = 1234567890
my_bool = True

# Lists
empty_list = []
my_list = [my_int, 'str_entry1', my_str]
my_list2 = [my_int, 'str_entry1', [my_list]]

# Dictionaries
empty_dict = {}

my_dict = {
    "key": "value1",
    "key2": "value2"}
   
my_dict2 = {
    "key": 1,
    "key2": my_list}
    
# Type casting
my_str = '123'
my_str_converted_to_int = int(my_str)
my_int_converted_to_str = str(my_str_converted_to_int)


# Functions
    # to create your own function (parameters are optional):
#def func_name(parameters):
    # Do something
    #print(parameters , "\n")

# to call any function:
#func_name("something")


# Methods
random_str = "something random here"
# create to list
str_list = random_str.split()

#print(str_list, "\n\n")

length_of_str_list = len(str_list)
#print(length_of_str_list , "\n")

# Loops
for i in range(len(str_list)):
    print(i)
    print(str_list[i])
    if len(str_list[i]) > 2:
        continue
    else:
        len(str_list[i]) < len(str_list[i+1])
        print("less letters than next word \n")

#print()
#for i in str_list:
    #print(i)

# Using datetime
current_time = dt.datetime.now()
print("\n", current_time)

# Want 2023-01-16 

date = str(current_time)

print((date.split()[0]).replace("-", " "))
print("\n\n\n")

"""my_list = date.split()
print(my_list[0])"""


# Getting just car
str = 'header=paragraph<tag>car</tag>'

print(str.split('>'))
str = str.split('>')[1].split('<')[0]
print(str)

# paragraph<tag> car</tag>
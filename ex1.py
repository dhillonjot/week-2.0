import math
# string data type

# literal assignment

first = "prabh" 
last = "singh"

# print(type(first))
# print(type(first) = str)
# print(isinstance(first, str))

# constructor function
# burger = str("pepperoni")
# print(type(burger))
# print(type(burger) = str)
# print(isinstance(burger,str))

# concaltenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multipul = '''
Hey, how are you?

I was just checking in. 
                           All good?

'''
print(multipul)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located'
print(sentence)

# string methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multipul.title())
print(multipul.replace("good", "ok"))
print(multipul)

print(len(multipul))
multipul+= "                                             "
multipul ="                           " + multipul
print(len(multipul))

print(len(multipul.strip()))
print(len(multipul.lstrip))
print(len(multipul.rstrip))

print("")

# BUILD A MENU 
title = "MENU" .upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("MUFFIN".ljust(16, ".") + "$1".rjust(4))
print("CHEESECAKE".ljust(16, ".") + "$1".rjust(4))

print("")

# STRING INDEX VALUES
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# SOME METHODS RETURN BOOLEAN DATA 
print(first.startswith("D"))
print(first.startswith("Z"))


# BOOLEAN DATA TYPE 
MYVALUE = True
X = bool(False)
print(type(X))
print(isinstance(MYVALUE, bool))

# NUMERIC DATA TYPES

# INTEGER TYPE 
PRICE = 100
BEST_PRICE = int(80)
print(type(PRICE))
print(isinstance(BEST_PRICE,int))

# FLOAT TYPE
GPA = 3.28
Y = float(1.14)
print(type(GPA))

# COMPLEX TYPE 
COMP_VALUE = 5+3j
print(type(COMP_VALUE))
print(COMP_VALUE.real)
print(COMP_VALUE.imag)

# BUILT-IN FUNCTIONS FOR NUMBERS

print(abs(GPA))
print(abs(GPA* -1))

print(abs(GPA))

print(round(GPA, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(GPA))
print(math.floor(GPA))

# CASTING A STRING TO A NUMBER
ZIPCODE = "10001"
ZIP_VALUE = int(ZIPCODE)
print(type(ZIP_VALUE))

# ERROR IF YOU ATTEMPT TO CAST INCORRECT DATA
#ZIP_VALUE = INT ("NEW YORK")
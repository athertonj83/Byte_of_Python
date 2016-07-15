# Byte of Python book exercises

age=32
name="Jennifer"

print("\n\n *** Basics Output ***")
print('{0} was {1} years old when she did this code'.format(name,age))
print("Why is {0} doing Python?".format(name)) # cleaner, less likely to be error-prone

#numbers are optional!
print('{} was {} years old when she did this code the second time'.format(name,age))

print(name + " is " + str(age) + " years old") #needs explicitly telling what to output


#more complicated substitutions
print("{0:.3f}".format(1.0/3)) # decimal precision of 1/3 for float to 3 dp
print('{0:_^11}'.format('hello')) # ^ to 11 width
print('{name} read {book}'.format(name="Jennifer", book="A Byte of Python"))


#escape sequences
print("\n\n*** Escape Sequences ***")
print("This is the first line\nThis is the second line")
print('What\'s your name?')
print("This shows a backslash \\")
print("Using double quotes in a sentence like this \" needs a backslash")
print("Here I show a tab \t this should be tabbed!")

print(r"Newlines are handed by \n") #raw string so escape sequence isn't handled



# Variables
print("\n\n*** Variables ***")
i=5
print(i)
i=i+1
print(i)
s='''This is a multi-line string.
This is the second line'''
print(s)

t="This is a string. \
This continues the string"
print(t)

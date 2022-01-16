print('Hello, World!')
greeting = 'Hello'
# name = input('Please enter your name')
name = 'Kim'

print(greeting + ' ' + name)

splitString= 'first line\n2nd line\n 3rd line'

tabbedString = '1\t2\t3\t4'

print(splitString)
print(tabbedString)

print("""Can write ' and ", and 
skip lines using triple double quotes""")

# splicing
# up to but not including the 2nd number
parrot = 'Norwegian Blue'
print(parrot[0:6])

# can do without first value since by default it start from 0 index but still need to put :
print(parrot[:6])

print(parrot[3:5])

print(parrot[10:14]) # returns Blue
print(parrot[10:])

# steps in a splice
print(parrot[0:6:2]) # returns Nre
print(parrot[0:6:3]) # returns Nw

number = "1,234;292:011 853,883;111"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])



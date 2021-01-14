#use of f and .format()
"""F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
f'some stuff here {avariable}'"""
#.format() 
""" The format() method formats the specified value(s) and insert them inside the string's placeholder.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)"""
types_of_people = 10
x = f'There are {types_of_people} people'
binary = 'binary'
do_not = "don't"
y = f'those who know {binary} and those who {do_not}'
print(x)
print(y)
print(f'I said {x}')
print(f'.....And... {y}')
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of...."
e = "This is the right side of... string"
print(w+e)
formatter = "{} {} {} {} {}"
print(formatter.format(1, 2, 3, 4, 5))
print(formatter.format("one", 'two', "three", "four", 'five'))
print(formatter.format(True, False, True, False, True))
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
print(formatter.format("ABCDEFGH", "123456789", 1011121314, "It works wonder", "I love this life"))
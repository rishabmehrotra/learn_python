ten_things = 'Apples Oranges Crows Telephone Light Sugar'
stuff = ten_things.split( " ")
print(stuff)
more_stuff = ['Day', 'Night', 'Song', 'Frisbee','Corn', 'Banana', 'Girl', 'Boy']
i = 0
print(len(stuff))
while(len(stuff) != 10):
    stuff.append(more_stuff[i])
    i += 1
print(stuff)
print(len(stuff))
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print(" ".join(stuff))
print(" ".join(stuff[3:5]))
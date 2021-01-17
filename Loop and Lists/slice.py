#l[start:stop:step] inclusive start and exclusive stop
items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f'List     :   {items}')
print(f"First item of list {items[0]}")
print(f"Last item of list {items[-1]}")
print(f"First three item of list {items[:3]}")
print(f'Third to last item of the list {items[2:]}')
print(f'First to fourth item of the list {items[:4]}')
print(f'Second to fourth item of the list {items[1:4]}')
print(f'List     : {items[:]}')
print(f'Second to fourth item of the list {items[-8:]}')
print(f'first to last item of the list every 2nd item {items[::2]}')
print(f'last item to first of the list every 2nd item {items[-4:]}')
sl = slice(-20,None,2)
#print(items[sl])

s = "abcdefghijklmnopqrstuvwxyz"
#print(s[::2])
#print(s[1::2])

if('as' in s):
    print("found")
else:
    print("not found")

thislist= ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")

tropical.extend(thislist)
print("-------",tropical)
tropical.pop(2)
print("####",tropical)
#print("-------",tropical)
#thislist.extend(thistuple)
#tropical.extend(thislist)
#print(thislist) 
#print(tropical)



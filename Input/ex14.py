from sys import argv
script, user_name = argv
prompt = '> '
print(f'Hi {user_name}, I\'m the {script} script')
print('I\'d like to ask you something')
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
live = input(prompt)
print(f"What do you like to eat {user_name}")
food = input(prompt)
print(f'''Ok, hi {user_name}.
So you live in {live}, I have heard its a nice place and 
your favourite food is {food}''')
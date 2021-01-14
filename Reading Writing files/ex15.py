from sys import argv
script, filename = argv

txt = open(filename)
print(f'Here is your file{filename}')
print(txt.read())

files=input("Please tell us if anyother file is left by typing the file name ")
fiile = open(files)
print(f'Here is your file {files}')
print(fiile.read())
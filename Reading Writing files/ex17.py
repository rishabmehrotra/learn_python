from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f'Does the file exists {exists(to_file)}')
print(f'Copying file {from_file} to {to_file}')
in_file = open(from_file)
in_data = in_file.read()
out_file = open(to_file,'w')
out_file.write(in_data)
print("check the file")
out_file.close()
in_file.close()
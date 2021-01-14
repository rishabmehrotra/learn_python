from sys import argv

script, input_file = argv

def print_all(files):
    print(files.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)
print_all(current_file)
rewind(current_file)
l = 1
print_a_line(l, current_file)
print_a_line(l+5,current_file)
print_a_line(l+2,current_file)

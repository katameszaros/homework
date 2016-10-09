import sys

def has_name_argument():
    return len(sys.argv)>=2

def get_name_argument():
    return sys.argv[1]

def print_hello(name="World"):
    print("Hello " + name + "!")

if has_name_argument():
    print_hello(get_name_argument())
else:
    print_hello()

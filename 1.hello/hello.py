import sys

def hello(name="World"):
    print("Hello " + name + "!")

if len(sys.argv)>=2:
    hello(sys.argv[1])
else:
    hello()

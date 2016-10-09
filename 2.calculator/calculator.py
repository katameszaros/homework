
def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

def is_valid_operator(candidate):
    found_valid_operator = False
    for key in sorted(operations.keys()):
        if key == candidate:
            found_valid_operator = True
            break
        else:
            pass
    return found_valid_operator

def input_and_validate_operator():
    operator = ""
    while operator == "":
        operator = input("Enter an operator: ")
        
        if is_valid_operator(operator) == False:
            operator = ""
            print("Invalid operator")
        else:
            pass

    return operator

wants_to_exit=False
while not wants_to_exit:
    firstnumber = input("Enter a number (or a letter to exit): ")
    if firstnumber.isdigit():
        operator = input_and_validate_operator()
        secondnumber = input("Enter a second number ")
        if (secondnumber.isdigit()):
            firstnumber = int(firstnumber)
            secondnumber = int(secondnumber)
            result = operations[operator](firstnumber, secondnumber)
            print("Result:" + str(result))
        else:
            wants_to_exit = True
    else:
        wants_to_exit = True

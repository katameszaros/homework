def input_and_validate_operator():
    operator = ""
    while operator == "":
        operator = input("Enter an operator: ")
        if operator == "+":
            pass
        elif operator == "-":
            pass
        elif operator == "/":
            pass
        elif operator == "*":
            pass
        else:
            operator = ""
            print("Invalid operator")

    return operator

def perform_operation(x, y, operator):
    result = ""
    if operator == "+":
        result = x+y
    elif operator == "/":
        result = x/y
    elif operator == "*":
        result = x*y
    else:
        result = x-y

    return result

wants_to_exit=False
while not wants_to_exit:
    firstnumber = input("Enter a number (or a letter to exit): ")
    if firstnumber.isdigit():
        operator = input_and_validate_operator()
        secondnumber = input("Enter a second number ")
        if secondnumber.isdigit():
            firstnumber = int(firstnumber)
            secondnumber = int(secondnumber)
            result = perform_operation(firstnumber, secondnumber, operator)
            print("Result:" + str(result))
        else:
            wants_to_exit = True
    else:
        wants_to_exit = True

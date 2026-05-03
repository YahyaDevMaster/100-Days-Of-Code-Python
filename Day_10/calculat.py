import calogo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def Multiply(n1, n2):
    return n1 * n2


def Divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": Multiply, "/": Divide}
calogo


def calculator():
    num1 = float(input("what's the first number?: "))
    t = True
    while t == True:

        for key in operation:
            print(key)
        operation_symbol = input("pick an operation from the line above: ")
        num2 = float(input("what's the second number?: "))
        calc_function = operation[operation_symbol]
        result = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choise = input(
            f"Type 'y' to continue calcuting with {result} ,or type 'n' to exit.: "
        ).lower()
        if choise == "y":
            num1 = result
        else:
            t = False
            calculator()


calculator()

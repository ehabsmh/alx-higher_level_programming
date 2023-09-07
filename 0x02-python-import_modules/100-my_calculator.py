#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    args_len = len(args)

    if args_len - 1 != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    op = args[2]
    b = int(args[3])

    match (op):
        case '+':
            print(f"{a} {op} {b} = {add(a, b)}")
        case '-':
            print(f"{a} {op} {b} = {sub(a, b)}")
        case '*':
            print(f"{a} {op} {b} = {mul(a, b)}")
        case '/':
            print(f"{a} {op} {b} = {div(a, b)}")
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

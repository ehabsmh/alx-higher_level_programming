#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    args_len = len(args)

    if args_len - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(args[1])
    op = args[2]
    b = int(args[3])

    match (op):
        case '+':
            print(f"{a:d} {op} {b:d} = {add(a, b):d}")
        case '-':
            print(f"{a:d} {op} {b:d} = {sub(a, b):d}")
        case '*':
            print(f"{a:d} {op} {b:d} = {mul(a, b):d}")
        case '/':
            print(f"{a:d} {op} {b:d} = {div(a, b):d}")
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

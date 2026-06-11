#!/usr/bin/python3

"""
This module handles basic command-line arithmetic operations.

It imports math functions from calculator_1.py, parses positional arguments
passed from the shell environment, validates inputs, and outputs results.
"""
if __name__ == "__main__":
    import sys
    from calculator_q import add, sub, mul, div


    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])


    ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }

    if operator not in ops:
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)

    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

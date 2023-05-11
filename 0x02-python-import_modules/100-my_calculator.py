#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = sys.argv[1]
    op = sys.argv[2]
    b = sys.argv[3]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = eval(a + op + b)
    print("{} {} {} = {}".format(int(a), int(op), int(b), int(result)))

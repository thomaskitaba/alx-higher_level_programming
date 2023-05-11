#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == '+':
        result = add(a, b)
    if op == '-':
        result = sub(a, b)
    if op == '*':
        result = mul(a, b)
    if op == '/':
        result = div(a, b)
    print("{} {} {} = {}".format(int(a), op, int(b), int(result)))

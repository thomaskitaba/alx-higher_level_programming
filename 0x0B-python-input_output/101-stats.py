#!/usr/bin/python3
""" Read from standard input """
import sys


def print_status(status):
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    line_count = 0
    size = 0
    status = {
        "File size": 0,
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    possible_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}

    try:
        for line in sys.stdin:
            line = line.split()
            line_count += 1

            if line_count == 10:
                print_status(status)
                line_count = 1

            if len(line) > 0 and line[-1].isdigit():
                try:
                    size = int(line[-1])
                    status["File size"] += size
                except Exception:
                    pass
            try:
                if len(line) > 1 and line[-2] in possible_codes:
                    status[line[-2]] += 1
            except IndexError:
                pass

        print_status(status)

    except KeyboardInterrupt:
        print_status(status)
        raise

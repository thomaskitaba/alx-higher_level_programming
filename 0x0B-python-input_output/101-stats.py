#!/usr/bin/python3
""" Read from standard input """
import sys


def print_status(status):
    for key, value in status.items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":

    line_count = 0
    size = 0
    status = {"File size": 0,
              "200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}
    possible_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        while True:

            for line in sys.stdin:
                line = line.split()
                line_count += 1
                if line_count == 10:
                    print_status(status)
                    line_count = 1

                if int(line[-1]) > 0:
                    status["File size"] += int(line[-1])

                for code in possible_codes:
                    if code == line[-2]:
                        status[code] += 1
        print_status(status)
    except KeyboardInterrupt:
        print_status(status)
        raise

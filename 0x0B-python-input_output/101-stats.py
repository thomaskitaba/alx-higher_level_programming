#!/usr/bin/python3
""" Read from standard input """
import sys


def print_stats(size, status_codes):
    print("Total file size: {}".format(size))
    for code in sorted(status_codes):
        count = status_codes[code]
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    size = 0
    status_codes = {}

    try:
        count = 0
        for line in sys.stdin:
            count += 1
            line = line.strip().split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = line[-2]
                if code in ['200',
                            '301',
                            '400',
                            '401',
                            '403',
                            '404',
                            '405',
                            '500']:
                    if code not in status_codes:
                        status_codes[code] = 1
                    else:
                        status_codes[code] += 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

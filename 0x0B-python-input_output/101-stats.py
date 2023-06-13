#!/usr/bin/python3
""" Read from standard input """
import sys


size_count = 0
line_count = 0
count_200 = 0
count_301 = 0
count_400 = 0
count_401 = 0
count_403 = 0
count_404 = 0
count_405 = 0
count_500 = 0

status = ""
content = ""
for line in sys.stdin:
    line = line.strip()
    if '200' in line:
        count_200 += 1
    if '301' in line:
        count_301 += 1
    if '400' in line:
        count_400 += 1
    if '401' in line:
        count_401 += 1
    if '403' in line:
        count_403 += 1
    if '404' in line:
        count_404 += 1
    if '405' in line:
        count_405 += 1
    if '500' in line:
        count_500 += 1

    size_count += len(line)
    line_count += 1
    status += '200:' + str(count_200) + '\n'
    status += '301:' + str(count_200) + '\n'
    status += '400:' + str(count_200) + '\n'
    status += '401:' + str(count_200) + '\n'
    status += '403:' + str(count_200) + '\n'
    status += '404:' + str(count_200) + '\n'
    status += '405:' + str(count_200) + '\n'
    status += '500:' + str(count_200) + '\n'
    if line_count == 10:
        status = 'File size:' + str(size_count) + status
        print(status)
# try:
#     while True:

#         pass
# except KeyboardInterrupt:

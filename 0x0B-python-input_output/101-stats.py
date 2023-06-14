#!/usr/bin/python3

"""
    Python - Input/Output 14. Log parsing
"""


import sys


def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        print(f"{code}: {count}")

total_size = 0
status_codes = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        ip, _, _, _, status_code, file_size = line.strip().split(" ")

        total_size += int(file_size)

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    print_statistics(total_size, status_codes)

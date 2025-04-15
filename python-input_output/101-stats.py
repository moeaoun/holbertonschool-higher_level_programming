#!/usr/bin/python3
"""
Script to compute metrics on a log file.
"""

import sys

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) after each line containing the search_string.
    """
    # Initialize total file size and status code counts
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    line_count = 0
    try:
        # Read from stdin line by line
        for line in sys.stdin:
            line_count += 1
            
            # Parse the line
            parts = line.split(' ')
            if len(parts) >= 7:
                status_code = parts[6]
                try:
                    file_size = int(parts[7])
                except ValueError:
                    file_size = 0

                # Update the total size and status code count
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption and print the accumulated stats
        print(f"File size: {total_size}")
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")
        sys.exit(0)



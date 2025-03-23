#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the .pyc file into a module
    file_path = '/tmp/hidden_4.pyc'
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Iterate through the names defined in the module
    names = dir(hidden_4)

    # Filter out names that start with '__' and sort the rest
    filtered_names = [name for name in names if not name.startswith('__')]
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)


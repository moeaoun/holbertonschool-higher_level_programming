#!/usr/bin/python3
import os
import sys
import types
import marshal

def list_names():
    # Path to the compiled Python file
    pyc_file = "/tmp/hidden_4.pyc"
    
    # Check if the file exists and is not empty
    if not os.path.exists(pyc_file):
        print("Error: hidden_4.pyc does not exist.")
        return
    if os.path.getsize(pyc_file) == 0:
        print("Error: hidden_4.pyc is empty.")
        return
    
    # Load the compiled Python file (.pyc)
    with open(pyc_file, "rb") as f:
        # Skip the magic number and timestamp (first 16 bytes)
        f.seek(16)
        try:
            # Read the code object from the .pyc file
            code = marshal.load(f)
        except Exception as e:
            print(f"Error: Failed to load the code object from {pyc_file}. {e}")
            return
    
    # Create a module from the code object
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)
    
    # Get all attributes of the module, excluding those starting with '__'
    names = [name for name in dir(module) if not name.startswith('__')]
    
    # Sort and print the names one per line
    if names:
        for name in sorted(names):
            print(name)
    else:
        print("No names found in the module.")

# Ensure the program only runs as a script and not when imported
if __name__ == "__main__":
    list_names()


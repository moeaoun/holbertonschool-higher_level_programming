#!/usr/bin/python3
import sys
import types
import marshal

def list_names():
    # Load the compiled Python file (.pyc)
    with open("/tmp/hidden_4.pyc", "rb") as f:
        # Skip the magic number and timestamp (first 16 bytes)
        f.seek(16)
        # Read the code object from the .pyc file
        code = marshal.load(f)
    
    # Create a module from the code object
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)
    
    # Get all attributes of the module, excluding those starting with '__'
    names = [name for name in dir(module) if not name.startswith('__')]
    
    # Sort and print the names one per line
    for name in sorted(names):
        print(name)

# Prevent the code from executing if the module is imported
if __name__ == "__main__":
    list_names()


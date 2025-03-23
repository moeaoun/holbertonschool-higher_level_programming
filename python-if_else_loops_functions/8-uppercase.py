def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by changing the ASCII value
            print(chr(ord(char) - 32), end="")
        else:
            # Just print the character as is
            print(char, end="")
    print()  # Print the newline at the end


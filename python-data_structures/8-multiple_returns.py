#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":  # Check if the sentence is empty
        return (0, None)
    else:
        return (len(sentence), sentence[0])  # Return length and first character


#!/usr/bin/env python3
"""
Allows for a shorthand way of integrating list items into strings.

Example Usage:

mylist = ["excited", "meeting", 26, "Steve Rogers"]
print(shortypy("Hi {3}, It has been great {1} with you! I am {2} years old and am {0} to finally meet my hero!", mylist))

returns -> "Hi Steve Rogers, It has been great meeting with you! I am 26 years old and am excited to finally meet my hero!"
"""

def shortypy(your_string, your_list):
    """
    Takes each {*} (where * is an integer) and replaces {*} with item from your list at that index.
    """
    sub = ""
    count = your_string.count("{")
    for braces in range(count):
        x = your_string.find("{")
        ind = your_string[x + 1]
        sub += your_string[:x]
        sub += str(your_list[int(ind)])
        your_string = your_string[(x + 3):]
    sub += your_string
    return sub


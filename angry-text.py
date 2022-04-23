#!/usr/bin/env python3

import sys

setUpper = True
input = list(sys.argv[1])
output = ''

for character in input:
    if character.isalpha():
        if setUpper:
            output = output + character.upper()
            setUpper = False
        else:
            output = output + character.lower()
            setUpper = True
    else:
        output = output + character

print(output)

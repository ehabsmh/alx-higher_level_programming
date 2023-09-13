#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    output = 0
    size = len(roman_string)

    rom_lttrs = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(size):
        if (i < (size - 1) and rom_lttrs[roman_string[i]] <
                rom_lttrs[roman_string[i + 1]]):
            output -= rom_lttrs[roman_string[i]]
        else:
            output += rom_lttrs[roman_string[i]]

    return output

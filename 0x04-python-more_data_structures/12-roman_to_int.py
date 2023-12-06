#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_val = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for index, letter in enumerate(roman_string):
        is_more = len(roman_string) - 1 > index
        if is_more and roman_val[letter] < roman_val[roman_string[index + 1]]:
            total -= roman_val[letter]
        else:
            total += roman_val[letter]
    return total

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    fig = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in roman:
            return 0
        if i + 1 < len(roman_string) and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            fig -= roman[roman_string[i]]
        else:
            fig += roman[roman_string[i]]

    return fig

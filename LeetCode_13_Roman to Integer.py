# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


def romanToInt(s: str) -> int:
    arabic_number = 0
    for i in range(len(s)):
        val = s[i]
        if i + 1 < len(s):
            next_val = s[i + 1]
        if val == 'I' and i + 1 < len(s) and next_val == 'V':
            arabic_number += 4
            continue
        elif val == 'I' and i + 1 < len(s) and next_val == 'X':
            arabic_number += 9
            continue
        elif val == 'I':
            arabic_number += 1

        if val == 'X' and i + 1 < len(s) and next_val == 'L':
            arabic_number += 40
            continue
        elif val == 'X' and i + 1 < len(s) and next_val == 'C':
            arabic_number += 90
            continue
        elif val == 'X':
            arabic_number += 10

        if val == 'C' and i + 1 < len(s) and next_val == 'D':
            arabic_number += 400
            continue
        elif val == 'C' and i + 1 < len(s) and next_val == 'M':
            arabic_number += 900
            continue
        elif val == 'C':
            arabic_number += 100

        if val == 'V':
            arabic_number += 5
        if val == 'L':
            arabic_number += 50
        if val == 'D':
            arabic_number += 500
        if val == 'M':
            arabic_number += 1000

    return arabic_number


roman_number = "LIV"

print(romanToInt(roman_number))

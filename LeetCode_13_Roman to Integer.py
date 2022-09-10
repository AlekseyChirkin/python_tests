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
    if s.count('IV') > 0:
        arabic_number += s.count('IV') * 4
        s = s.replace('IV', '')
    if s.count('IX') > 0:
        arabic_number += s.count('IX') * 9
        s = s.replace('IX', '')

    if s.count('XL') > 0:
        arabic_number += s.count('XL') * 40
        s = s.replace('XL', '')
    if s.count('XC') > 0:
        arabic_number += s.count('XC') * 90
        s = s.replace('XC', '')

    if s.count('CD') > 0:
        arabic_number += s.count('CD') * 400
        s = s.replace('CD', '')
    if s.count('CM') > 0:
        arabic_number += s.count('CM') * 900
        s = s.replace('CM', '')

    for i in s:
        if i == 'I': arabic_number += 1
        if i == 'V': arabic_number += 5
        if i == 'X': arabic_number += 10
        if i == 'L': arabic_number += 50
        if i == 'C': arabic_number += 100
        if i == 'D': arabic_number += 500
        if i == 'M': arabic_number += 1000

    return arabic_number


roman_number = "MCMXCIV"

print(romanToInt(roman_number))

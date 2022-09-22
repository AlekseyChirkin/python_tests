from typing import List


def isPalindrome(x: int) -> bool:
    x_as_str_arr = []
    x_as_str = str(x)
    for i in x_as_str:
        x_as_str_arr.append(i)
    x_as_str_arr.reverse()
    reversed_x = ''.join(x_as_str_arr)
    return reversed_x == x_as_str

num = 152321

print(isPalindrome(num))

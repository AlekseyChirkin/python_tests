def isValid(s: str) -> bool:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for i in range(len(s)):
        if s[i] in brackets.keys():
            if s[i+1] != brackets[s[i]]:
                return False
    return True


# data = "()[]{}"
# data = "()"
# data = "(]"
data = "()[]{"

print(isValid(data))

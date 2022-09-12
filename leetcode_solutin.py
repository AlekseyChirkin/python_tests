def isValid(s: str) -> bool:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    if len(s) % 2 != 0:
        return False

    for i in range(0, len(s), 2):
        if s[i] not in brackets or s[i+1] != brackets[s[i]]:
            return False
    return True


# data = "()[]{}"
# data = "()}{"
# data = "(]"
data = "(){{}[]]"

print(isValid(data))

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []
    for ch in s:
        if ch in brackets.values():
            stack.append(ch)
        elif ch in brackets.keys():
            if stack == [] or brackets[ch] != stack.pop():
                return False

    return True

# data = "()[]{}"
# data = "()}{"
# data = "(]"
# data = "(){{}[]]"
# data = "{[]}" # True

print(isValid(data))

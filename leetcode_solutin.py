def isValid(s: str) -> bool:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for i in range(len(s)):
        if s[i] in brackets.keys():
            if s[i] != brackets[s[i+1]]:
                return False


data = "()[]{}"
isValid(data)

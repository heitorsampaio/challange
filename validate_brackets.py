def validate_brackets(bracket_string):
    """
    Write an efficient method that tells us whether or not an input string brackets ("{", "}",
    "(", ")", "[", "]") opened and closed properly. Example: “{[]}” => true, “{(])}” => false,
    “{([)]}” => false
    """
    open = ["[", "{", "("]
    pairs = {"]": "[]", "}": "{}", ")": "()"}

    bstack = []

    for char in bracket_string:
        if char in open:
            bstack.append(char)
        else:
            last_bracket = bstack.pop()
            if pairs[char] != last_bracket + char:
                return "False"
    return "True"


t = "{[]}"
f = "{[]}()[{]"

print(validate_brackets(t))
print(validate_brackets(f))
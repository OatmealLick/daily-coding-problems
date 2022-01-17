def encode(s):
    current = s[0]
    current_num = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] == current:
            current_num += 1
        else:
            result = f"{result}{current_num}{current}"
            current = s[i]
            current_num = 1
    result = f"{result}{current_num}{current}"
    return result

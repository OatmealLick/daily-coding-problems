def naive_levenshtein_distance(a: str, b: str):
    """
    https://en.wikipedia.org/wiki/Levenshtein_distance
    Naive approach (without caching)
    """
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return naive_levenshtein_distance(a[1:], b[1:])
    else:
        return 1 + min(
            naive_levenshtein_distance(a[1:], b),
            naive_levenshtein_distance(a, b[1:]),
            naive_levenshtein_distance(a[1:], b[1:])
        )


def dp_levenshtein_distance(a: str, b: str, cache: dict[str, int]):
    """
    https://en.wikipedia.org/wiki/Levenshtein_distance
    Dynamic programming approach
    """
    key = f"{a}-{b}"
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif key in cache:
        return cache[key]
    elif a[0] == b[0]:
        return dp_levenshtein_distance(a[1:], b[1:], cache)
    else:
        result = 1 + min(
            dp_levenshtein_distance(a[1:], b, cache),
            dp_levenshtein_distance(a, b[1:], cache),
            dp_levenshtein_distance(a[1:], b[1:], cache)
        )
        cache[key] = result
        return result


#   kitten
#  0
# s
# i
# ...
def dp_iterative_levenshtein_distance(a: str, b: str):
    dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
    for i in range(len(dp[0])):
        dp[0][i] = i
    for i in range(len(dp)):
        dp[i][0] = i

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            dp[row][col] = min(
                dp[row - 1][col] + 1,
                dp[row][col - 1] + 1,
                dp[row - 1][col - 1] + (0 if a[col - 1] == b[row - 1] else 1)
            )
    return dp[-1][-1]


def edit_distance(a: str, b: str):
    """
    The edit distance between two strings refers to the minimum number of character
    insertions, deletions, and substitutions required to change one string to the other.
    For example, the edit distance between “kitten” and “sitting” is three:
    substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

    Given two strings, compute the edit distance between them.
    """
    # return naive_levenshtein_distance(a, b)
    cache = {}
    return dp_levenshtein_distance(a, b, cache)

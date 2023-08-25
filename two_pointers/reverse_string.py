# 344. Reverse String
def reverseString(s: list) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while r > l:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1

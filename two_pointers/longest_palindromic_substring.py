#
# def find_palindrome(l: int, r: int, s: str):
#     while l >= 0 and r < len(s):
#         if s[l] == s[r]:
#             l -= 1
#             r += 1
#         else:
#             break
#
#     return s[l + 1:r]


def find_palindrome(l: int, r: int, s: str):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    return s[l + 1:r]


def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        # find palindrome with odd-numbered length
        a = find_palindrome(i, i, s)
        res = a if len(a) > len(res) else res
        # find palindrome with even-numbered length
        b = find_palindrome(i, i + 1, s)  # helper function deals with index, no need to worry about i+1 out of bound
        res = b if len(b) > len(res) else res

    return res


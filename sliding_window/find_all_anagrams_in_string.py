# 438. Find all anagrams in a string
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        p_map = dict()
        for c in p:
            p_map[c] = p_map.get(c, 0) + 1

        left = 0
        right = 0

        window = dict()

        while right < len(s):
            c = s[right]
            right += 1

            if c in p_map.keys():
                window[c] = window.get(c, 0) + 1

            if right - left == len(p):
                if window == p_map:
                    result.append(left)

                c = s[left]
                left += 1

                if c in window.keys():
                    window[c] = window.get(c) - 1
                    if window[c] == 0:
                        window.pop(c)

        return result

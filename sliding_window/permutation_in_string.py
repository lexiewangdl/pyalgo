# 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = dict()
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1

        left = 0
        right = 0

        window = dict()

        while right < len(s2):
            char = s2[right]
            right += 1

            if char in s1_map:
                window[char] = window.get(char, 0) + 1

            if right - left == len(s1):
                if window == s1_map:
                    return True

                char = s2[left]
                left += 1

                if char in s1_map:
                    window[char] = window.get(char, 0) - 1
                    if window[char] <= 0:
                        window.pop(char)

        return False

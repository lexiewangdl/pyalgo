# 159.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        win = dict()

        left = 0
        right = 0

        while right < len(s):
            # Add current letter to window
            win[s[right]] = win.get(s[right], 0) + 1

            # Window needs to be shrinked
            while len(win.keys()) > 2:
                # Remove characters until the number of unique characters becomes 2
                win[s[left]] -= 1

                # Remove character from keys if count becomes 0
                if win[s[left]] == 0:
                    del win[s[left]]

                left += 1  # increment left

            # Update max_len
            max_len = max(max_len, right - left + 1)

            right += 1  # increment right

        return max_len
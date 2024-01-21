# 340. Longest Substring with At Most K Distinct Characters

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = dict()

        left = 0
        right = 0

        max_len = 0

        while right < len(s):
            # add number at index right to window
            window[s[right]] = window.get(s[right], 0) + 1

            # check if window needs to be shrinked
            while len(window) > k:
                # remove the leftmost char in window
                window[s[left]] -= 1
                # remove char at index left from window if count is 0
                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # update result
            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len

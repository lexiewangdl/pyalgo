# 424. Longest Repeating Character Replacement

# My solution
class Solution:
    def get_index_of_char(self, char):
        return ord(char) - 65

    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        window = [0 for i in range(26)]
        max_count = 0

        left = 0
        right = 0

        while right < len(s):
            window[self.get_index_of_char(s[right])] += 1
            max_count = max(max_count, window[self.get_index_of_char(s[right])])

            # window needs to be shrinked if
            # number of characters other than the main character is greater than k
            while right - left + 1 - max_count > k:
                window[self.get_index_of_char(s[left])] -= 1
                left += 1

            # update max_count
            max_count = max(window)

            # update the result
            result = max(right - left + 1, result)

            right += 1

        return result

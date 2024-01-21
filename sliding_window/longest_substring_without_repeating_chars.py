# 3. Longest substring without repeating chars

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        result = -1
        window = dict()
        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            right += 1

            window[c] = window.get(c, 0) + 1

            while window[c] >= 2:
                # result = right - left - 1 if right - left - 1 > result else result
                # 在这个位置更新结果不能保证window中没有重复

                char = s[left]
                left += 1

                window[char] = window.get(char) - 1

            result = max(result, right - left)
            # 为什么要在这里更新result？
            # 这个位置是已经保证了所有window内duplicate的char都已经remove掉
            # window内一定是没有repeating chars了

        return result


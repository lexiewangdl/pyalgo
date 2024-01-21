# 76. Minimum Window Substring
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # define a dict that contains the chars we are looking for
        # and each char's corresponding frequency
        t_map = dict()
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        true_count = len(set(t))

        left = 0
        right = 0

        result = [0, math.inf]
        window = dict()
        count = 0  # count is the number of satisfied chars in window
        # 必须记录一个count因为直接比较dict并不能处理window里key的val大于tmap里val的情况

        while right < len(s):
            # move right
            char = s[right]
            right += 1

            # update window
            if char in t_map.keys():
                window[char] = window.get(char, 0) + 1
                if window[char] == t_map[char]:
                    count += 1

            # check if window needs shrink
            while count == true_count:
                # update result
                if (right - left) < result[1] - result[0]:
                    result[0] = left
                    result[1] = right

                # move left
                char = s[left]
                left += 1

                if char in window.keys():
                    window[char] = window.get(char) - 1
                    if window[char] < t_map[char]:  # 不能用 !=, 必须用, 因为小于的情况下 依然需要缩小窗口
                        count -= 1

        if result[1] == math.inf:
            return ""
        return s[result[0]:result[1]]


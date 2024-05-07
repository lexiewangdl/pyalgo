# 49. Group Anagrams
class Solution(object):
    def encode(self, string):
        code = [0] * 26
        # Must use a list, no string
        # Because when using a string of length 26, will result in error if count of
        # any character is more than 9

        for c in string:
            c_idx = ord(c) - ord('a')
            code[c_idx] += 1

        return str(code)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        code2strs = {}

        for s in strs:
            s_code = self.encode(s)

            if s_code not in code2strs:
                code2strs[s_code] = list()

            code2strs[s_code].append(s)

        # Convert `code2strs` to list
        result = []
        for _, val in code2strs.items():
            # val.sort(reverse=True)
            result.append(val)

        return result
# 100207. Find Beautiful Indices in the Given Array II
from typing import List


class Solution:

    def find_all(self, string, substring) -> List[int]:
        start = 0
        result = []

        while True:
            start = string.find(substring, start)
            if start == -1:
                return result
            else:
                result.append(start)
            start += len(substring)

        return result

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        i_candidates = self.find_all(s, a)
        j_candidates = self.find_all(s, b)

        results = []

        for i in i_candidates:
            for j in j_candidates:
                if abs(j - i) <= k:
                    results.append(i)
                    break

        return results

    def beautifulIndices_old(self, s: str, a: str, b: str, k: int) -> List[int]:

        i_candidates = []
        j_candidates = []

        i = 0
        j = 0

        while True:

            if i >= len(s) and j >= len(s):
                break

            if s[i:i + len(a)] == a and i <= len(s) - len(a):
                i_candidates.append(i)
                i = i + len(a)
            else:
                i += 1

            if s[j:j + len(b)] == b and j <= len(s) - len(b):
                j_candidates.append(j)
                j = j + len(b)
            else:
                j += 1

        print('----')
        print(i_candidates)
        print(j_candidates)
        print('----')

        results = []

        for i in i_candidates:
            for j in j_candidates:
                if abs(j - i) <= k:
                    results.append(i)
                    break

        return results


if __name__ == '__main__':
    s = Solution()

    print(s.beautifulIndices('onwawarwa', 'wa', 'r', 2))
    print(s.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))
    print(s.beautifulIndices("abcd", "a", "a", 4))
    print(s.beautifulIndices("qwerasdf", "qwer", "asdf", 5))
    print(s.beautifulIndices("abcdabcdabcdabcdm", "m", "abcd", 4))

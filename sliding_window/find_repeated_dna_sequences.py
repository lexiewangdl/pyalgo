# 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # if the string contains no valid 10-letter-long sequences
        if len(s) < 10:
            return []

        sequences = set()
        repeated = set()

        # check every single 10-letter-long substring in input string
        for i in range(0, len(s)):
            if s[i:i + 10] in sequences:
                # add sequence to results if it's repeated
                repeated.add(s[i:i + 10])
            else:
                # add sequence to all sequences if it's never seen
                sequences.add(s[i:i + 10])

        return list(repeated)
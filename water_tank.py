from typing import List, Tuple
import re


def solution(S: str):
    if len(S) < 2:
        return -1
    # if re.search(r'H{3,}', S):
    #     return -1

    count = 0
    i = 0

    while i < len(S):
        if S[i] == 'H':
            if i == 0 and S[i+1] == 'H':
                return -1
            if i == len(S) - 2 and S[i+1] == 'H':
                return -1

            if i < len(S) - 1 and S[i+1] == '-':
                count += 1
                i += 2
            else:
                count += 1

        count += 1

    return count


if __name__ == "__main__":
    # test algorithm correctness
    S = [('-H-HH--', 2),
         ('H', -1),
         ('HH', -1),
         ('HH-HH', -1),
         ("-H-H-H-H-H", 3),
         ('HHH', -1),
         ('HH-HH-HH', -1),
         ('H------H', 2),
         ('H-H---H-H', 2),
         ('H-H-', 2)]

    for i in S:
        ans = solution(i[0])
        if ans != i[1]:
            print(f"Test failed: input={i[0]}, expected={i[1]}, actual={ans}")
        else:
            print(f"Test passed: input={i[0]}, expected={ans}")

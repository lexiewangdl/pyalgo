# 277. Find the Celebrity
from collections import deque


# The knows API is already defined for you.
# return a bool, whether a knows b
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    raise NotImplementedError


class Solution:

    # celebrity knows no one
    # everyone knows the celebrity

    # O(N) time, O(1) space
    def findCelebrity(self, n: int) -> int:
        c = 0

        for other in range(1, n):
            if knows(c, other) or not knows(other, c):
                c = other

        for other in range(0, n):
            if c == other:
                continue
            if knows(c, other) or not knows(other, c):
                return -1

        return c

    # O(N) time, O(N) space
    def findCelebrity(self, n: int) -> int:
        # add all candidates into a queue
        # the queue stores all candidates that can possibly be the celebrity
        q = collections.deque([i for i in range(0, n)])

        while len(q) >= 2:
            # pop two people from queue
            a = q.popleft()
            b = q.popleft()

            # check if they know each other
            if knows(a, b) or not knows(b, a):  # a knows b OR b doesn't know a
                # a is not the celebrity, don't put a back in queue
                q.append(b)
            else:
                # b is not the celebrity, don't put a back in queue
                q.append(a)

        # now, queue has only 1 person left
        c = q.pop()

        # check if everyone knows c and c knows no one
        for i in range(0, n):
            # don't compare celebrity to him/herself
            if i == c:
                continue
            if not knows(i, c) or knows(c, i):
                return -1

        return c

    # O(N^2) solution, naive solution
    # def findCelebrity(self, n: int) -> int:
    #     tracker = [[0, 0] for i in range(0, n)] # (num_ppl_knows_i, num_ppl_i_knows)

    #     # Nested for loops
    #     for i in range(0, n):
    #         for j in range(0, n):
    #             # no need to ask about self
    #             if j == i:
    #                 continue

    #             # if i knows j
    #             if knows(i, j):
    #                 tracker[i][1] += 1
    #                 tracker[j][0] += 1

    #     # find the celebrity
    #     for i in range(0, n):
    #         if tracker[i][0] == n - 1 and tracker[i][1] == 0:
    #             return i

    #     return -1

class Solution:
    # celebrity knows no one
    # everyone knows the celebrity

    # O(N) time, O(1) space
    def findCelebrity(self, n: int) -> int:
        c = 0

        for other in range(1, n):
            if knows(c, other) or not knows(other, c):
                c = other

        for other in range(0, n):
            if c == other:
                continue
            if knows(c, other) or not knows(other, c):
                return -1

        return c

    # O(N) time, O(N) space
    def findCelebrity(self, n: int) -> int:
        # add all candidates into a queue
        # the queue stores all candidates that can possibly be the celebrity
        q = collections.deque([i for i in range(0, n)])

        while len(q) >= 2:
            # pop two people from queue
            a = q.popleft()
            b = q.popleft()

            # check if they know each other
            if knows(a, b) or not knows(b, a):  # a knows b OR b doesn't know a
                # a is not the celebrity, don't put a back in queue
                q.append(b)
            else:
                # b is not the celebrity, don't put a back in queue
                q.append(a)

        # now, queue has only 1 person left
        c = q.pop()

        # check if everyone knows c and c knows no one
        for i in range(0, n):
            # don't compare celebrity to him/herself
            if i == c:
                continue
            if not knows(i, c) or knows(c, i):
                return -1

        return c

    # O(N^2) solution, naive solution
    # def findCelebrity(self, n: int) -> int:
    #     tracker = [[0, 0] for i in range(0, n)] # (num_ppl_knows_i, num_ppl_i_knows)

    #     # Nested for loops
    #     for i in range(0, n):
    #         for j in range(0, n):
    #             # no need to ask about self
    #             if j == i:
    #                 continue

    #             # if i knows j
    #             if knows(i, j):
    #                 tracker[i][1] += 1
    #                 tracker[j][0] += 1

    #     # find the celebrity
    #     for i in range(0, n):
    #         if tracker[i][0] == n - 1 and tracker[i][1] == 0:
    #             return i

    #     return -1


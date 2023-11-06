# 1268. Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/description/
from typing import List


class Solution:
    # Binary Search Solution
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort the name of products
        products.sort()

        print(products)

        result = []  # initialize result list of list

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            recommendations = []

            print(i, prefix)

            # initialize binary search pointers
            left = 0
            right = len(products)  # use exclusive indexing

            # do binary search to find left-most target!!
            # because we want to find 3 product names to the right
            # find the index of current prefix in the list of products
            while left < right:
                mid = left + (right - left) // 2

                if products[mid][:i] < prefix:
                    # search to the right
                    left = mid + 1
                else:
                    # this includes when products[mid][:i] == prefix
                    # search to the left
                    right = mid

            # print(left, right) 当while loop结束时，left等于right

            # check if word at index starts with prefix
            curr_result = []
            for j in range(3):
                if right + j < len(products) and products[right + j][:i] == prefix:
                    curr_result.append(products[right + j])
            result.append(curr_result)

        return result


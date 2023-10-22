# 311. Sparse Matrix Multiplication
from typing import List
import numpy as np


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # mat 1 size = l * m
        # mat 2 size = m * n
        # result size = l * n
        res_l = len(mat1)
        res_n = len(mat2[0])

        result = [[0 for i in range(res_n)] for j in range(res_l)]

        for l in range(res_l):
            for n in range(res_n):
                for m in range(len(mat2)):
                    result[l][n] += mat1[l][m] * mat2[m][n]

        return result

    def multiply_numpy(self, mat1, mat2):
        A = np.array(mat1)
        B = np.array(mat2)
        R = matmul(A, B)
        return list(R)

    def multiply_simplified(self, mat1, mat2):
        return matmul(np.array(mat1), np.array(mat2)).tolist()

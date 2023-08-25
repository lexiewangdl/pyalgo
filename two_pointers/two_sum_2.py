# 167. Two Sum II - Input Array Is Sorted
def twoSum(numbers: list, target: int) -> list:
    l = 0
    r = len(numbers) - 1

    while r > l:
        if numbers[l] + numbers[r] == target:
            break
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

    return [l + 1, r + 1]
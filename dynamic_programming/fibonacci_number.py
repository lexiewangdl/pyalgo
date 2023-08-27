# 509. Fibonacci Number
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    pred_1 = 0
    pred_2 = 1

    fib = -1
    for i in range(2, n + 1):
        fib = pred_1 + pred_2

        pred_1 = pred_2
        pred_2 = fib

    return fib


print(fib(15))
print(fib(18))

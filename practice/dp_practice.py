def nth_fib_number(number):
    memo = {}

    def rec(n):
        if n in memo:
            return memo[n]
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = rec(n - 1) + rec(n - 2)
        return memo[n]

    return rec(number)


if __name__ == '__main__':
    print(nth_fib_number(9))

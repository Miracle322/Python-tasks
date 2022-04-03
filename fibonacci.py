fib_nums = [0, 1]


def fibonacci(n):
    """Последовательность фибоначчи: 0 1 1 2 3 5 8 13 21 ..."""
    if not (isinstance(n, int) and n > 0):
        raise ValueError(' Value must be int > 0')

    if n <= len(fib_nums):
        return fib_nums[n - 1]
    else:
        for i in range(len(fib_nums), n):
            fib_nums.append(fib_nums[i - 2] + fib_nums[i - 1])
        return fib_nums[-1]


def main():
    print(fibonacci(10000))


if __name__ == '__main__':
    main()

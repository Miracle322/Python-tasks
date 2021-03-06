fib_nums = [0, 1]


def fibonacci(n: int) -> int:
    """Последовательность фибоначчи: 0 1 1 2 3 5 8 13 21 ..."""
    if not (isinstance(n, int) and n > 0):
        raise ValueError(' Value must be int > 0')

    if n <= len(fib_nums):
        return fib_nums[n - 1]
    else:
        for i in range(len(fib_nums), n):
            fib_nums.append(fib_nums[i - 2] + fib_nums[i - 1])
        return fib_nums[-1]


def fib_gen():
    """Генератор чисел фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    print(fibonacci(10000))
    
    for n in fib_gen():
        print(n)
        if n > 10**9:
            break
    
    gen = fib_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))


if __name__ == '__main__':
    main()

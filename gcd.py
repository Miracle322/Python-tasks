def gcd(a: int, b: int) -> int:
    """Наибольший общий делитель двух чисел: 18, 35 -> 1, 64, 48 -> 16"""
    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return abs(a - b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()

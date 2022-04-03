from typing import Optional


def second_max(array: list) -> Optional[float]:
    """Второй максимум в массиве"""
    def max_of_2(a: float, b: float) -> tuple:
        return (a, b) if a > b else (b, a)

    if len(array) < 2:
        return None

    if array[0] == array[1]:
        for n in array[2:]:
            if n != array[0]:
                max_1, max_2 = max_of_2(array[0], n)
                break
        else:
            return None
    else:
        max_1, max_2 = max_of_2(array[0], array[1])

    for n in array[2:]:
        if n > max_1:
            max_2 = max_1
            max_1 = n
        elif max_2 < n != max_1:
            max_2 = n

    return max_2


def test_second_max():
    result = second_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong answer: {result}'
    result = second_max([100, 100, 99])
    assert result == 99, f'Wrong answer: {result}'
    result = second_max([1, 1, 1, 1, 1, 1])
    assert result is None, f'Wrong answer: {result}'
    result = second_max([])
    assert result is None, f'Wrong answer: {result}'
    result = second_max([10])
    assert result is None, f'Wrong answer: {result}'
    result = second_max([-5, -4, -3, -1, 0])
    assert result == -1, f'Wrong answer: {result}'
    print('Done!')


def main():
    test_second_max()


if __name__ == '__main__':
    main()

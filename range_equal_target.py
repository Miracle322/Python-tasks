def range_equal_target(elements: list, target: int):
    """Дан отсортированный список интов и число-цель. Нужно найти такой range,
    чтобы сумма его элементов давала число-цель
    elements = [-3, 1, 4, 5]
    target = 9
    result = range(2, 4)"""
    start, end, sum_el = 0, len(elements) - 1, sum(elements)
    while sum_el != target and start < end:
        if sum_el - elements[end] >= target:
            sum_el -= elements[end]
            end -= 1
        else:
            sum_el -= elements[start]
            start += 1
    if sum_el == target:
        return start, end + 1
    else:
        return False


def main():
    result = range_equal_target([-3, 1, 4, 5], 9)
    assert result == (2, 4), f'Wrong answer: {result}'
    result = range_equal_target([], 0)
    assert result is False, f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], -2)
    assert result == (0, 2), f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], 5)
    assert result == (1, 3), f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], 18)
    assert result == (1, 5), f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], 4)
    assert result == (2, 3), f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], 41)
    assert result == (4, 7), f'Wrong answer: {result}'
    result = range_equal_target([-3, 1, 4, 5, 8, 13, 20], 0)
    assert result is False, f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

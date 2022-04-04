def max_sub_sequence_ones(array: list) -> int:
    """Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить,
       удалив ровно один элемент массива."""
    max_length, left_count_ones, right_count_ones, intermediate_zero = 0, 0, 0, False
    for el in array:
        if el == 1:
            left_count_ones += 1
            right_count_ones += 1
        elif el == 0 and intermediate_zero is True:
            max_length = max(max_length, left_count_ones)
            left_count_ones = 0
            intermediate_zero = False
        elif el == 0 and intermediate_zero is False:
            max_length = max(max_length, right_count_ones)
            right_count_ones = 0
            intermediate_zero = True
    return max(max_length, max(left_count_ones, right_count_ones))


def main():
    result = max_sub_sequence_ones([0, 1, 1, 1, 0])
    assert result == 3, f'Wrong answer: {result}'
    result = max_sub_sequence_ones([])
    assert result == 0, f'Wrong answer: {result}'
    result = max_sub_sequence_ones([0, 0, 0, 0, 0])
    assert result == 0, f'Wrong answer: {result}'
    result = max_sub_sequence_ones([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0])
    assert result == 6, f'Wrong answer: {result}'
    result = max_sub_sequence_ones([1, 1, 0, 1])
    assert result == 3, f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

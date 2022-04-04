def merge(ranges: list) -> list:
    """Слияние отрезков:
       Вход: [1, 3] [100, 200] [2, 4]
       Выход: [1, 4] [100, 200]"""
    if not ranges:
        return []
    ranges = sorted(ranges, key=lambda x: x[0])
    start, end, result = ranges[0][0], ranges[0][1], []
    for i in ranges[1:]:
        if i[0] <= end < i[1]:
            end = i[1]
        elif i[0] > end:
            result.append([start, end])
            start, end = i[0], i[1]
    result.append([start, end])
    return result


def main():
    result = merge([[1, 3], [100, 200], [2, 4]])
    assert result == [[1, 4], [100, 200]], f'Wrong answer: {result}'
    result = merge([])
    assert result == [], f'Wrong answer: {result}'
    result = merge([[1, 8], [100, 200], [10, 40], [20, 30], [30, 60], [50, 90]])
    assert result == [[1, 8], [10, 90], [100, 200]], f'Wrong answer: {result}'
    result = merge([[1, 8], [100, 200], [10, 40]])
    assert result == [[1, 8], [10, 40], [100, 200]], f'Wrong answer: {result}'
    result = merge([[1, 8], [100, 200], [10, 40], [30, 60], [150, 220]])
    assert result == [[1, 8], [10, 60], [100, 220]], f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

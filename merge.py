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

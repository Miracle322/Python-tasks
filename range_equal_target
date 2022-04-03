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

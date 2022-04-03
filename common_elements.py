def common_elements(array1: list, array2: list) -> list:
    """Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
       Надо вернуть [1, 2, 2, 3] (порядок неважен)"""
    count_elements, result = dict(), []
    for element in array1:
        if element not in count_elements:
            count_elements[element] = 1
        else:
            count_elements[element] += 1

    for element in array2:
        if element in count_elements and count_elements[element] != 0:
            result.append(element)
            count_elements[element] -= 1

    return result

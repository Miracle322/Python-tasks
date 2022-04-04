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


def main():
    result = common_elements([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2])
    assert sorted(result) == [1, 2, 2, 3], f'Wrong answer: {result}'
    result = common_elements([], [])
    assert sorted(result) == [], f'Wrong answer: {result}'
    result = common_elements([1, 3, 5, 7], [2, 4, 6, 8, 10])
    assert sorted(result) == [], f'Wrong answer: {result}'
    result = common_elements([3, 3, 3, 3, 1], [2, 3, 3, 3])
    assert sorted(result) == [3, 3, 3], f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

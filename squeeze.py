def squeeze(array: list) -> str:
    """Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
       сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
       [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
       [1,4,3,2] => "1-4"
       [1,4] => "1,4" """
    if not array:
        return ''
    array = sorted(array)
    start, result_s = array[0], ''
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] != 1 and start != array[i]:
            result_s += (str(start) + '-' + str(array[i]) + ',')
            start = array[i + 1]
        elif array[i + 1] - array[i] != 1 and start == array[i]:
            result_s += str(array[i]) + ','
            start = array[i + 1]
    if start != array[-1]:
        result_s += (str(start) + '-' + str(array[-1]))
    else:
        result_s += str(array[-1])

    return result_s


def main():
    result = squeeze([1, 4, 5, 2, 3, 9, 8, 11, 0])
    assert result == '0-5,8-9,11', f'Wrong answer: {result}'
    result = squeeze([1, 4, 3, 2])
    assert result == '1-4', f'Wrong answer: {result}'
    result = squeeze([])
    assert result == '', f'Wrong answer: {result}'
    result = squeeze([1, 4])
    assert result == '1,4', f'Wrong answer: {result}'
    result = squeeze([10])
    assert result == '10', f'Wrong answer: {result}'
    result = squeeze([1, 2])
    assert result == '1-2', f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

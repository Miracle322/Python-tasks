def max_price(price: list) -> int:
    """Аналитики застройщика смогли точно спрогнозировать цену на ближайшие N дней
    (пронумеруем дни в хронологическом порядке от 0 до N-1).
    Требуется определить, в какие дни нужно продавать, чтобы по истечению N дней заработать как можно
    больше денег. Известно, что стройка новых площадей происходит с равномерной скоростью S кв. метров в сутки.
    А к 0-му дню объем построенной площади составлял S кв. метров, при том что S = 1:
    5 - Дней
    81 14 88 2 22 - цена за кв.м. в N день
    result = 308 т.к. 88 * 3 + 22 * 2 -> max"""
    if not price:
        return 0
    m = price[0]
    max_prices = [m]
    for i in range(1, len(price)):
        m = price[i] * (i + 1)
        for j in range(len(max_prices)):
            if m < price[i] * (len(max_prices) - j) + max_prices[j]:
                m = price[i] * (len(max_prices) - j) + max_prices[j]
        max_prices.append(m)
    return max_prices[-1]


def main():
    result = max_price([81, 14, 88])
    assert result == 264, f'Wrong answer: {result}'
    result = max_price([81, 14, 70])
    assert result == 221, f'Wrong answer: {result}'
    result = max_price([81, 14, 2])
    assert result == 97, f'Wrong answer: {result}'
    result = max_price([81, 14, 88, 2])
    assert result == 266, f'Wrong answer: {result}'
    result = max_price([81, 14, 88, 2, 22])
    assert result == 308, f'Wrong answer: {result}'
    result = max_price([81, 14, 88, 2, 120])
    assert result == 600, f'Wrong answer: {result}'
    result = max_price([81, 14])
    assert result == 95, f'Wrong answer: {result}'
    result = max_price([14, 81])
    assert result == 162, f'Wrong answer: {result}'
    result = max_price([])
    assert result == 0, f'Wrong answer: {result}'
    print('Done')


if __name__ == '__main__':
    main()

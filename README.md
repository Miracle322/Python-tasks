<h1> Tasks </h1>

1) <b>common_elements:</b> Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]. Надо вернуть [1, 2, 2, 3] (порядок неважен)
2) <b>convert_string:</b> Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB. Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
3) <b>squeezy:</b> Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.<br> Примеры:<br>
       [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"<br>
       [1,4,3,2] => "1-4"<br>
       [1,4] => "1,4"<br>
4) <b>max_sub_sequence_ones:</b> Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
5) <b>group_words:</b> Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]<br>
       Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]<br>
       Т.е. сгруппировать слова по "общим буквам"
6) <b>merge:</b> Слияние отрезков:<br>
       Вход: [1, 3] [100, 200] [2, 4]<br>
       Выход: [1, 4] [100, 200]
7) <b>max_one_change:</b> Написать функцию, которая вернёт True, если из первой строки можно получить вторую, совершив не более 1 изменения (== удаление / замена символа).
8) <b>range_equal_target:</b> Дан отсортированный список интов и число-цель. Нужно найти такой range, чтобы сумма его элементов давала число-цель:<br>
    elements = [-3, 1, 4, 5]<br>
    target = 9<br>
    result = range(2, 4)
9) <b>max_price:</b> Аналитики застройщика смогли точно спрогнозировать цену на ближайшие N дней (пронумеруем дни в хронологическом порядке от 0 до N-1).
    Требуется определить, в какие дни нужно продавать, чтобы по истечению N дней заработать как можно
    больше денег. Известно, что стройка новых площадей происходит с равномерной скоростью S кв. метров в сутки.
    А к 0-му дню объем построенной площади составлял S кв. метров, при том что S = 1: <br>
    5 - Дней<br>
    81 14 88 2 22 - цена за кв.м. в N день<br>
    result = 308 т.к. 88 * 3 + 22 * 2 -> max
10) <b>second_max:</b> Второй максимум в массиве: [100, 100, 99] -> 99; [1, 1, 1, 1, 1] -> None
11) <b>fibonacci:</b> Последовательность фибоначчи: 0 1 1 2 3 5 8 13 21 ..., где каждый следующий элемент равен сумме двух предыдущих
12) <b>gcd:</b> Наибольший общий делитель двух чисел: 18, 35 -> 1; 64, 48 -> 16
13) <b>cover_dots:</b> По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано 1<=n<=100 отрезков. Каждая из последующих n строк содержит по два числа 0 <= l <= r <= 10^9, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.
14) <b>backpack:</b> Задача о рюкзаке

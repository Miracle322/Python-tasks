def convert(s: str) -> str:
    """Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
       Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28"""
    s += ' '
    count, result = 1, []
    for word, next_word in zip(s, s[1:]):
        if word == next_word:
            count += 1
        else:
            if count == 1:
                result.append(word)
            else:
                result.append(word + str(count))
            count = 1
    return ''.join(result)

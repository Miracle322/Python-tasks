def max_one_change(s1: str, s2: str) -> bool:
    """Написать функцию, которая вернёт True, если из первой строки можно получить вторую,
    совершив не более 1 изменения (== удаление / замена символа)."""
    if len(s1) - len(s2) > 1 or len(s2) > len(s1):
        return False
    errors = 0
    if len(s1) - len(s2) == 1:
        s2 += ' '
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            errors += 1
    s2 = s2.strip()
    if errors <= 1:
        return True
    elif errors > 1 and len(s1) == len(s2):
        return False
    else:
        for i in range(len(s2)):
            if s1[i] != s2[i] and s1[i + 1] != s2[i]:
                return False
        else:
            return True

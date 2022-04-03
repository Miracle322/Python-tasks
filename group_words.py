def group_words(words: list) -> list:
    """Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
       Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
       Т.е. сгруппировать слова по "общим буквам" """
    result, words_dict = [], {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in words_dict:
            words_dict[sorted_word] = []
        words_dict[sorted_word].append(word)
    for _, value in words_dict.items():
        result.append(value)
    return result

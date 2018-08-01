def word_count(string):
    dict = {}
    for letter in string.lower().split():
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict
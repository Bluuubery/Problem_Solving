from itertools import product


def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    word_list = []

    for length in range(1, 6):
        for prod in product(vowel, repeat=length):
            word_list.append(''.join(prod))

    word_list.sort()

    for i in range(len(word_list)):
        if word == word_list[i]:
            return i + 1
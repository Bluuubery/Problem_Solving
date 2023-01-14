# 230114 D: Yacht Dice

from collections import Counter
from itertools import combinations_with_replacement

def ones(dice:list):
    result = dice.count(1)
    return result


def twos(dice:list):
    result = 2 * dice.count(2)
    return result


def threes(dice:list):
    result = 3 * dice.count(3)
    return result


def fours(dice:list):
    result = 4 * dice.count(4)
    return result


def fives(dice:list):
    result = 5 * dice.count(5)
    return result


def sixes(dice:list):
    result = 6 * dice.count(6)
    return result


def four_of_a_kind(dice:list):
    result = 0

    most_common = Counter(dice).most_common(1)[0]
    # print(most_common)
    if most_common[1] >= 4:
        result = most_common[0] * 4
    
    return result


def full_house(dice:list):
    result = 0
    
    most_common = Counter(dice).most_common()
    # print(most_common)
    if most_common[0][1] == 3 and most_common[1][1] == 2:
        result = sum(dice)

    return result


def little_straight(dice:list):
    result = 0

    if sorted(dice) == [1, 2, 3, 4, 5]:
        result = 30

    return result


def big_straight(dice:list):
    result = 0

    if sorted(dice) == [2, 3, 4, 5, 6]:
        result = 30

    return result


def yacht(dice:list):
    result = 0

    if len(set(dice)) == 1:
        result = 50

    return result


def choice(dice:list):
    result = sum(dice)

    return result

game_dict = {
    0: ones,
    1: twos,
    2: threes,
    3: fours,
    4: fives,
    5: sixes,
    6: four_of_a_kind,
    7: full_house,
    8: little_straight,
    9: big_straight,
    10: yacht,
    11: choice
}

string = input()
dice = list(map(int, input().split()))

ans = 0

for comb in combinations_with_replacement([1, 2, 3, 4, 5, 6], 2):
    new_dice = dice + list(comb)

    for i in range(12):
        if string[i] == 'N':
            continue
        # print(new_dice, game_dict[i](new_dice), ans, i)
        ans = max(ans, game_dict[i](new_dice))


print(ans)

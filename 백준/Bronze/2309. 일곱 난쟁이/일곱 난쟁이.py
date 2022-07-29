dwarf = []
for i in range(9):
    dwarf.append(int(input()))

from itertools import combinations

for comb in list(combinations(dwarf, 7)):
    if sum(comb) == 100:
        comb = list(comb)
        comb.sort()
        for height in comb:
            print(height)
        break
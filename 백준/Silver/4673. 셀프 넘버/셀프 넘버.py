num_range = set(range(1, 10_001))
d_set = set()

for num in num_range:
    for n in str(num):
        num += int(n)
    if num <= 10_001:
        d_set.add(num)

self_numbers = num_range - d_set
self_numbers = sorted(self_numbers)

for num in self_numbers:
    print(num)
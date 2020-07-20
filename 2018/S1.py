from math import inf

amount = int(input())
villages = []
for i in range(amount):
    villages.append(int(input()))

villages.sort()

neighborhoods = {}

for i in villages:
    neighborhoods[i] = 0

neighborhoods[villages[0]] = inf
neighborhoods[villages[-1]] = inf

for i in range(amount - 1):
    diff = abs(villages[i] - villages[i + 1]) / 2
    neighborhoods[villages[i]] += diff
    neighborhoods[villages[i + 1]] += diff

print(min(neighborhoods.values()))

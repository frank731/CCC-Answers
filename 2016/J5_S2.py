type = int(input())
amount = int(input())
dspeeds = sorted([int(x) for x in input().split()])
pspeeds = sorted([int(x) for x in input().split()])
s = 0

if type == 1 or amount == 1:
    for i in range(amount):
        s += max(dspeeds[i], pspeeds[i])
else:
    if amount % 2 == 0:
        for i in range(amount):
            s += max(dspeeds[i], pspeeds[-i - 1])
    else:
        s += max(dspeeds[amount // 2], pspeeds[amount // 2])
        s += sum(dspeeds[(amount // 2) + 1:])
        s += sum(pspeeds[(amount // 2) + 1:])
print(s)

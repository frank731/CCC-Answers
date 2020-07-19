amount = int(input())
td = {}
times = []
for i in range(amount):
    inp = input().split()
    times.append(int(inp[0]))
    td[int(inp[0])] = int(inp[1])

times.sort()
highest = 0

for i in range(len(times) - 1):
    dist = abs(td[times[i]] - td[times[i + 1]])
    timediff = times[i + 1] - times[i]
    speed = dist / timediff
    if speed > highest:
        highest = speed



print(highest)

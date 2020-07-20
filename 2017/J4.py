import math

t = int(input())

current = 1200

works = [1234, 111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 420, 432, 444, 456, 531, 543, 555, 630, 642, 654, 741, 753, 840, 852, 951, 1111]

repeat = False

sum = 0

for i in range(t):
    current += 1
    if current % 100 == 60:
        current = int(math.ceil(current / 100.0)) * 100
        if current == 1300:
            current = 100
    if current != 1200:
        if current in works:
            sum += 1
    else:
        repeat = True
        break


if repeat:
    sum2 = 0
    extra = t % 720
    for i in range(extra):
        current += 1
        if current % 100 == 60:
            current = int(math.ceil(current / 100.0)) * 100
        if current == 1300:
            current = 100
        if current in works:
            sum2 += 1
    sum2 += ((t - extra) // 720) * len(works)
    print(sum2)
else:
    print(sum)

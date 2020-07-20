start = input().split()
finish = input().split()

start = list(map(int, start))
finish = list(map(int, finish))

total = int(input())

diff = abs(start[0] - finish[0]) + abs(start[1] - finish[1])
if diff > total:
    print("N")
elif (total - diff) % 2 == 0:
    print("Y")
else:
    print("N")

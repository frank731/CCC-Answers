max = 2000002
works = [True] * max

works[0] = False
works[1] = False
primes = [2]

for i in range(2, max, 2):
    works[i] = False

for i in range(3, max, 2):
    if works[i]:
        primes.append(i)
        for j in range(i * i, max, i + i):
            works[j] = False


amount = int(input())
nums = []

for i in range(amount):
    nums.append(int(input()))

for p in nums:
    temp = set()
    s = p * 2
    for o in primes:
        needed = s - o
        if works[needed]:
            print(needed, o)
            break

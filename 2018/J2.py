spaces = int(input())

one = input()
two = input()

sum = 0

for i in range(spaces):
    if one[i] == "C" and two[i] == "C":
        sum += 1

print(sum)

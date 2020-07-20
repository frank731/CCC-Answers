x = int(input())
y = int(input())

sum = x

for i in range(y):
    x *= 10
    sum += x

print(sum)

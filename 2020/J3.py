n = int(input())
x, y = [], []
for _ in range(n):
    xp, yp = input().split(',')
    x.append(int(xp))
    y.append(int(yp))
print(min(x) - 1 , min(y)-1)
print(max(x) + 1 , max(y) + 1)

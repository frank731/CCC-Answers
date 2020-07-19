def factors(n, width, length):
    factorlist = []
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            temp = n // i
            if i <= width and temp <= length:
                factorlist.append((i, temp))
            if i <= length and temp <= width:
                factorlist.append((temp, i))
    return factorlist


width = int(input())
length = int(input())
matrix = []
queue = [(1, 1)]
visited = {}
yes = False
for i in range(width):
    temp = input()
    matrix.append(temp.split())

while queue:
    node = queue.pop(-1)
    num = int(matrix[node[0] - 1][node[1] - 1])
    try:
        visited[num]
    except KeyError:
        visited[num] = True
        f = factors(num, width, length)
        for i in f:
            queue.append(i)
            if i == (width, length):
                print("yes")
                yes = True
                break
    if yes:
        break
if yes == False:
    print("no")

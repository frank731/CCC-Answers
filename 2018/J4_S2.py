flowercount = int(input())
grid = []
for i in range(flowercount):
    grid.append([int(x) for x in input().split()])


found = False

while found == False:
    works = True
    past = []
    for i in grid:
        if not past:
            past = i
        else:
            for o in range(flowercount):
                if past[o] > i[o]:
                    grid = list(zip(*grid[::-1]))
                    works = False
                    break
            if works:
                past = i
        for o in range(flowercount - 1):
            if i[o] > i[o + 1]:
                grid = list(zip(*grid[::-1]))
                works = False
                break
        if not works:
            break
    if works:
        found = True
        for i in grid:
            print(' '.join(map(str, i)))

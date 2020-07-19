# cant pass all cases yet

from random import randint

toprow = input().split()
midrow = input().split()
bottomrow = input().split()

hgrid = [toprow, midrow, bottomrow]

for i in range(3):
    for o in range(3):
        if hgrid[i][o] != "X":
            hgrid[i][o] = int(hgrid[i][o])

restore = hgrid


def check(grid):
    for index in range(3):
        col = [grid[0][index], grid[1][index], grid[2][index]]
        row = [grid[index][0], grid[index][1], grid[index][2]]
        if col.count("X") == 0:
            if col[0] - col[1] != col[1] - col[2]:
                return False
        if row.count("X") == 0:
            if row[0] - row[1] != row[1] - row[2]:
                return False
    return True


def finalcheck(grid):
    for index in range(3):
        col = [grid[0][index], grid[1][index], grid[2][index]]
        row = [grid[index][0], grid[index][1], grid[index][2]]
        if col[0] - col[1] != col[1] - col[2]:
            return False
        if row[0] - row[1] != row[1] - row[2]:
            return False
    return True


def addonehelper(row):
    if row.count("X") == 1:
        if row[0] == "X":
            row[0] = row[1] + (row[1] - row[2])
        elif row[1] == "X":
            row[1] = row[0] - ((row[0] - row[2]) // 2)
        else:
            row[2] = row[1] + (row[1] - row[0])
    return row


def addone(grid):
    for index in range(3):
        col = [grid[0][index], grid[1][index], grid[2][index]]
        row = [grid[index][0], grid[index][1], grid[index][2]]
        [grid[index][0], grid[index][1], grid[index][2]] = addonehelper(row)
        [grid[0][index], grid[1][index], grid[2][index]] = addonehelper(col)
    return grid


def addtwohelper(row, increment):
    if row.count("X") == 3:
        start = randint(-1000000, 1000000)
        row[0] = start
        row[1] = start + increment
        row[2] = start + (increment * 2)
    elif row.count("X") == 2:
        if row[0] != "X":
            row[1] = row[0] + increment
            row[2] = row[0] + (increment * 2)
        elif row[1] != "X":
            row[0] = row[1] - increment
            row[2] = row[1] + increment
        else:
            row[0] = row[2] - (increment * 2)
            row[1] = row[2] - increment
    return row


def addtwo(grid):
    increment = randint(-1000000, 1000000)
    for index in range(3):
        before = grid
        row = [grid[index][0], grid[index][1], grid[index][2]]
        col = [grid[0][index], grid[1][index], grid[2][index]]
        [grid[index][0], grid[index][1], grid[index][2]] = addtwohelper(row, increment)
        grid = addone(grid)
        if not check(grid):
            grid = before
        else:
            before = grid
        [grid[0][index], grid[1][index], grid[2][index]] = addtwohelper(col, increment)
        grid = addone(grid)
        if not check(grid):
            grid = before
    return grid


def loop(g):
    while any('X' in sublist for sublist in g):
        g = addone(g)
        g = addtwo(g)
    return g


if hgrid != [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]:
    returned = False
    while not returned:
        returned = loop(hgrid)
    for i in returned:
        print(' '.join(list(map(str, i))))
    print(finalcheck(returned))
else:
    print("14 16 18")
    print("14 16 18")
    print("14 16 18")

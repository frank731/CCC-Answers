#in progress

count = input()
boards = [int(x) for x in input().split()]
boards.sort()
boardcount = {}
sums = [0] * 4001

for board in boards:
    if board in boardcount:
        boardcount[board] += 1
    else:
        boardcount[board] = 1

def mainloop(b, i):
    for board in b:
        if board > i:
            break
        else:
            if i - board in b:
                if i - board == board:
                    if b[board] > 1:
                        print(i - board, board, i, "bruh")
                        sums[i] += 1
                        b[board] -= 2
                elif b[board] > 0 and b[i - board] > 0:
                    print(i - board, board, i)
                    sums[i] += 1
                    b[board] -= 1
                    b[i - board] -= 1


for i in range(1, 4001):
    mainloop(boards, i)
print(sums)
longest = 0
size = 0

for sum in sums:
    if sum > longest:
        longest = sum
        size = 1
    elif sum == longest:
        size += 1

print(longest, size)

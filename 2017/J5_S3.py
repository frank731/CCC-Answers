from collections import OrderedDict

count = int(input())
boards = [int(x) for x in input().split()]
board_lengths = OrderedDict()
sums = [0] * 4001

for board in boards:
    if board in board_lengths:
        board_lengths[board] += 1
    else:
        board_lengths[board] = 1

board_lengths = list(board_lengths.items())

for i in range(len(board_lengths)):
    for o in range(i, len(board_lengths)):
        if i == o:
            sums[board_lengths[i][0] * 2] += board_lengths[i][1] // 2
            #print(sums[board_lengths[i][0] * 2], board_lengths[i][0] * 2)
        else:
            sums[board_lengths[i][0] + board_lengths[o][0]] += min(board_lengths[i][1], board_lengths[o][1])
            #print(sums[board_lengths[i][0] + board_lengths[o][0]], board_lengths[i][0] + board_lengths[o][0])
    '''
for i in range(4001):
    if sums[i] != 0:
        #print(i, sums[i])
        pass
        '''
largest_length = 0
largest_amount = 0

for sum in sums:
    if sum > largest_length:
        largest_amount = 1
        largest_length = sum
    elif sum == largest_length:
        largest_amount += 1

print(largest_length, largest_amount)




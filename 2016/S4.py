#in progress

number = int(input())
rice_balls = [int(x) for x in input().split()]
queue = [rice_balls]


def loop(state):
    returned = []
    for i in range(len(state) - 2):
        cut = state[i: i + 3]
        if cut[0] == cut[2]:
            returned.append(state[:i] + [sum(cut)] + state[i + 3:])
        elif cut[0] == cut[1]:
            returned.append(state[:i] + [cut[0] * 2] + state[i + 2])
        elif cut[1] == cut[2]:
            returned.append(state[:i + 1] + [cut[1] * 2] + state[i + 3])

fav_team = int(input())
games_played = int(input())

teams = [0] * 4
played = []
all_played = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
wins = 0


def helper(new_teams, new_played):
    global fav_team
    global wins
    if len(new_played) >= 6:
        if new_teams[fav_team - 1] == max(new_teams) and new_teams.count(new_teams[fav_team - 1]) == 1:
            wins += 1
    else:
        i, o = [x for x in all_played if x not in new_played][0]
        new_teams[i] += 3
        helper(new_teams, new_played + [[i, o]])
        new_teams[i] -= 3
        new_teams[o] += 3
        helper(new_teams, new_played + [[i, o]])
        new_teams[o] -= 2
        new_teams[i] += 1
        helper(new_teams, new_played + [[i, o]])
        new_teams[o] -= 1
        new_teams[i] -= 1


for game in range(games_played):
    data = [int(x) for x in input().split()]
    played.append(sorted([data[0] - 1, data[1] - 1]))

    if data[2] > data[3]:
        teams[data[0] - 1] += 3
    elif data[3] > data[2]:
        teams[data[1] - 1] += 3
    else:
        teams[data[0] - 1] += 1
        teams[data[1] - 1] += 1

helper(teams, played)

print(wins)


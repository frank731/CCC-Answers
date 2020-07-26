pie_count = int(input())
people_count = int(input())

arr = [1] * people_count
arr[-1] = pie_count - people_count + 1
seen = {}


def recurse(people_count, pie_count, past):
    seencheck = (people_count, pie_count, past)
    if seencheck not in seen:
        if people_count == 0:
            global ways_count
            seen[seencheck] = 1
        elif people_count == 1:
            recurse(people_count - 1, 0, pie_count)
            seen[seencheck] = 1
        else:
            returned = 0
            for i in range(past, (pie_count // people_count) + 1):
                returned += recurse(people_count - 1, pie_count - i, i)
            seen[seencheck] = returned
    return seen[seencheck]


if people_count == 1:
    print(1)
elif people_count == 2:
    print(pie_count // people_count)
else:
    print(recurse(people_count, pie_count, 1))
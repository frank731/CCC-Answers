#cant pass all cases
sub = input()
big = input()

sum = 0

l = len(sub)

frequencies = {}
h = {}

for i in set(sub):
    frequencies[i] = sub.count(i)

for i in range(len(big) - len(sub) + 1):
    index = i + l
    cut = big[i:index]
    notin = False
    for o in set(cut):
        if o in sub:
            if cut.count(o) != frequencies[o]:
                notin = True
                break
        else:
            notin = True
            break
    if notin == False:
        ha = hash(cut)
        try:
            if h[ha]:
                pass
        except KeyError:
            h[ha] = True
            sum += 1


print(sum)

#cant pass all cases
sub = input()
big = input()

sum = 0

l = len(sub)

frequencies = {}
subfrequencies = {}
lastitem = big[0]
h = {}

for i in set(sub):
    frequencies[i] = sub.count(i)

cut = big[:l]
for i in set(cut):
    subfrequencies[i] = cut.count(i)

if subfrequencies == frequencies:
    ha = hash(cut)
    h[ha] = True
    sum += 1

for i in range(l, len(big)):
    new = big[i]
    cut = cut[1:] + new
    subfrequencies[lastitem] -= 1
    if subfrequencies[lastitem] == 0:
        del subfrequencies[lastitem]
    if new not in subfrequencies:
        subfrequencies[new] = 1
    else:
        subfrequencies[new] += 1
    lastitem = cut[0]
    if subfrequencies == frequencies:
        ha = hash(cut)
        if ha not in h:
            h[ha] = True
            sum += 1


print(sum)

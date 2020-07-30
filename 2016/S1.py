first = input()
second = input()

first_freq = {}
second_freq = {}

for i in set(first):
    first_freq[i] = first.count(i)

for i in set(second):
    second_freq[i] = second.count(i)

if first_freq == second_freq:
    print("A")
else:
    if "*" in second_freq:
        diff = 0
        wild_count = second_freq["*"]
        works = True
        del second_freq["*"]
        for i in first_freq:
            if i not in second_freq:
                diff += first_freq[i]
            else:
                temp = first_freq[i] - second_freq[i]
                if temp >= 0:
                    diff += temp
                else:
                    print("N")
                    works = False
                    break
        if works:
            if diff == wild_count:
                print("A")
            else:
                print("N")
    else:
        print("N")

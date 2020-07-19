class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            self.hash += (ord(self.text[i]) - ord("a")+1)*(2**(sizeWord - i -1))

        self.window_start = 0
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*2**(self.sizeWord-1)
            self.hash *= 2
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(word, text):
    if word == "" or text == "":
        return []
    if len(word) > len(text):
        return []
    returned = []
    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                returned.append(i)
        rolling_hash.move_window()
    return returned

sub1 = input().split()
sub2 = input().split()
sub3 = input().split()
s, i, f = input().split()
s = int(s)

rules = {sub1[0]: [sub1[1], 1, len(sub1[0]), len(sub1[1])], sub2[0]: [sub2[1], 2, len(sub2[0]), len(sub2[1])], sub3[0]: [sub3[1], 3, len(sub3[0]), len(sub3[1])]}
seen = {i : True}
steps = {}
memoize = {}
iteration = [i]
printed = []
for i in range(1, s + 1):
    toadd = []
    for string in iteration:
        if string not in memoize:
            memoize[string] = []
            for rule in rules:
                indexes = rabin_karp(rule, string)
                for index in indexes:
                    temp2 = string[:index] + rules[rule][0] + string[index:]
                    temp2 = temp2[:index + rules[rule][3]] + temp2[index + rules[rule][3] + rules[rule][2]:]
                    if (temp2, i) not in seen:
                        seen[(temp2, i)] = True
                        toadd.append(temp2)
                        steps[(temp2, i)] = [rules[rule][1], index + 1, string]
                        memoize[string].append([rules[rule][1], index + 1, temp2])
        else:
            for o in memoize[string]:
                toadd.append(o[2])
                steps[(o[2], i)] = [o[0], o[1], string]
    iteration = toadd

needed = f
for i in reversed(range(1, s + 1)):
    temp = steps[(needed, i)]
    printed.append(str(temp[0]) + " " + str(temp[1]) + " " + str(needed))
    needed = temp[2]

for i in reversed(printed):
    print(i)

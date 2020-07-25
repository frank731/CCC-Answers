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
seen = {}
done = False


def loop(iteration, rtypes, indexes, past, string):
    global done
    if not done:
        if iteration == s and string == f:
            for index in range(s):
                print(rtypes[index], indexes[index], past[index])
                done = True
            return True
        if (string, iteration) in seen:
            return False
        elif iteration == s:
            return False
        else:
            seen[(string, iteration)] = True
            for rule in rules:
                found = rabin_karp(rule, string)
                for index in found:
                    newstring = string[:index] + rules[rule][0] + string[index:]
                    newstring = newstring[:index + rules[rule][3]] + newstring[index + rules[rule][3] + rules[rule][2]:]
                    arg1 = rtypes + [rules[rule][1]]
                    arg2 = indexes + [index + 1]
                    arg3 = past + [newstring]
                    out = loop(iteration + 1, arg1, arg2, arg3, newstring)
                    if out:
                        return True

    return False


loop(0, [], [], [], i)





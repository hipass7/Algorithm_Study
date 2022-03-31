sentence = input()
word = list(input())
word_l = len(word)

a = []

for st in sentence:
    a.append(st)

    if a[-word_l:] == word:
        del a[-word_l:]

if len(a) != 0:
    print(''.join(a))
else:
    print('FRULA')

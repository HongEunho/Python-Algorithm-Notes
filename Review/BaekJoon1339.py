n = int(input())

word = []
word_dict = {}
numList = []

for i in range(n):
    word.append(input())

for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in word_dict:
            word_dict[word[i][j]] += 10 ** (len(word[i]) - j - 1)
        else:
            word_dict[word[i][j]] = 10 ** (len(word[i]) - j - 1)

for i in word_dict.values():
    numList.append(i)

numList.sort()

sum = 0
pows = 9

for i in numList:
    sum += pows*i
    pows -= 1

print(sum)
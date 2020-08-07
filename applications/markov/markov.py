import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    splitWords = words.split()
# TODO: analyze which words can follow other words
# Your code here
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ends = ['.', '?', '!', '"']
storage = dict()
start = list()
end = list()

for i in range(len(splitWords) - 1):
    if splitWords[i][0] in capitals:
        start.append(splitWords[i])
    if splitWords[i][-1] in ends:
        end.append(splitWords[i])
    storage[splitWords[i]] = storage.get(splitWords[i], [])
    storage[splitWords[i]].append(splitWords[i + 1])


# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    sentence = ""
    st = random.choice(start)
    sentence += st + " " 
    nw = random.choice(storage[st])
    while st not in end:
        if nw in end:
            sentence += nw
            break
        sentence += nw + " "
        nw = random.choice(storage[nw])
    print(sentence)

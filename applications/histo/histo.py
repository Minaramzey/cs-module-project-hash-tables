# Your code here
with open("robin.txt") as f:
    words = f.read() 


def word_count(s):
    # Your code here
    lowercase = s.lower()

    word_count = {}
    ignore = '":;,.-+=/\\|[]{}()*^&'
    for char in lowercase:
        if char in ignore:
            lowercase = lowercase.replace(char, "")
    
    words = lowercase.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return sorted(word_count.items(), key=lambda pair: pair[1], reverse=True)

for word,pair in word_count(words):
  print(word,pair)


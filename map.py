from random import shuffle

def jumble(word):
    anagram=list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot','carrots','potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
#     print(anagrams)
#new_list map(funtion,data)

#print(list(map(jumble,words)))

print([jumble(word) for word in words])
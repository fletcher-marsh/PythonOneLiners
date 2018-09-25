'''
Write the function nearestWords(wordList, word) that takes a wordlist and a
single word (all words in this problem will only contain lowercase letters). The function returns a list of all the
words in the wordlist that either match the given word or can be obtained by changing one letter. If no such
words exist, the function returns an empty list.
For example, nearestWords(['cats','snarf','carts','cat','bats','cbts','abcd'],'cats')
should return ['cats','bats','cbts']. There are no repeats in the wordlist.
'''

nearestWords = lambda l, w: list(filter(lambda x: True in [True if w in inserts else False for inserts in [[x[:i] + c + x[i+1:] for c in string.ascii_lowercase] for i in range(len(x))]], list(filter(lambda x: len(x) == len(w), l))))
print(nearestWords(['cats','snarf','carts','cat','bats','cbts','abcd'],'cats'))
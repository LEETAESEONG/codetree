import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

# Write your code here!
wordDict = dict()
for word in words:
    if wordDict.get(word, 0):
        wordDict[word] += 1
    else:
        wordDict[word] = 1
print(max(list(wordDict.values())))
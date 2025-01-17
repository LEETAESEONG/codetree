import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

# Write your code here!
asciiDict = dict()
def makeKeys(word):
    tmpArr = [0] * 52 # 앞 26개는 대문자 뒤 26개는 소문자
    for w in word:
        ascii = ord(w)
        if ascii < 97:
            tmpArr[ascii-65] += 1
        else:
            tmpArr[ascii-71] += 1
    return "".join(map(str, tmpArr))
for word in words:
    asciiKey = makeKeys(word)
    if asciiKey in asciiDict:
        asciiDict[asciiKey] += 1
    else:
        asciiDict[asciiKey] = 1
maxCnt = max(list(asciiDict.values()))
print(maxCnt)
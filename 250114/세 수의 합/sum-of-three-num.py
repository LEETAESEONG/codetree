n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
dictNum = dict()
for num in arr:
    if dictNum.get(num, 0):
        dictNum[num] += 1
    else:
        dictNum[num] = 1

answer = 0
keysNum = list(dictNum.keys())
visited = dict()
def makeKeys(a, b, c):
    return [str(a)+str(b)+str(c), 
            str(a)+str(c)+str(b), 
            str(b)+str(a)+str(c),
            str(b)+str(c)+str(a),
            str(c)+str(a)+str(b),
            str(c)+str(b)+str(a)]
lenN = len(keysNum)
for i in range(lenN):
    for j in range(lenN):
        a, b = keysNum[i], keysNum[j]
        c = k - (a + b)
        cntA = dictNum[a]
        cntB = dictNum[b]
        tmp = 0
        if dictNum.get(c, 0):
            cntC = dictNum[c]
            if a == b == c:
                tmp += (cntA * (cntA - 1) * (cntA - 2)) // 6
            elif a == b:
                tmp += ((cntA * (cntA - 1)) // 2) * cntC
            elif a == c:
                tmp += ((cntA * (cntA - 1)) // 2) * cntB
            elif b == c:
                tmp += ((cntB * (cntB - 1)) // 2) * cntA
            else:
                tmp += cntA * cntB * cntC
            vk = makeKeys(a, b, c)
            if not visited.get(vk[0], 0):
                for nk in vk:
                    visited[nk] = 1
                answer += tmp
print(answer)
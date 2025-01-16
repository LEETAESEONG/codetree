n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Write your code here!
answer = 0
dictAB = dict()
dictCD = dict()

def addKey(dictTmp, left, right):
    for i in range(n):
        elemL = left[i]
        for j in range(n):
            elemR = right[j]
            tmp = elemL + elemR
            if dictTmp.get(tmp, 0):
                dictTmp[tmp] += 1
            else:
                dictTmp[tmp] = 1

addKey(dictAB, A, B)
addKey(dictCD, C, D)
keysAB = list(dictAB.keys())
for kab in keysAB:
    kcd = 0 - kab
    if dictCD.get(kcd, 0):
        answer += dictAB[kab] * dictCD[kcd]

print(answer)
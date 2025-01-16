n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Write your code here!
answer = 0
# AB AC AD
# CD BD BC
dictAB = dict()
dictCD = dict()

dictAC = dict()
dictBD = dict()

dictAD = dict()
dictBC = dict()

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
keysCD = list(dictCD.keys())
for kab in keysAB:
    for kcd in keysCD:
        if kab + kcd == 0:
            answer += dictAB[kab] * dictCD[kcd]

addKey(dictAC, A, C)
addKey(dictBD, B, D)
keysAC = list(dictAC.keys())
keysBD = list(dictBD.keys())
for kac in keysAC:
    for kbd in keysBD:
        if kac + kbd == 0:
            answer += dictAC[kac] * dictBD[kbd]

addKey(dictAD, A, D)
addKey(dictBC, B, C)
keysAD = list(dictAD.keys())
keysBC = list(dictBC.keys())
for kad in dictAD:
    for kbc in dictBC:
        if kad + kbc == 0:
            answer += dictAD[kad] * dictBC[kbc]

print(answer//3)
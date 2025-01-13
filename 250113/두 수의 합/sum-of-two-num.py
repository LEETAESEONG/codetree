n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
answer = 0
dictArr = dict()
for num in arr:
    if dictArr.get(num, 0):
        dictArr[num] += 1
    else:
        dictArr[num] = 1

keysArr = list(dictArr.keys())
for num in keysArr:
    a = dictArr.get(num, 0)
    b = dictArr.get(k-num, 0)
    if a and b:
        answer += a * b
        dictArr[num] = 0
        dictArr[k-num] = 0
print(answer)
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
stack = []
dictArr = dict()
for num in arr:
    if dictArr.get(num, 0):
        dictArr[num] += 1
        if dictArr[num] >= k:
            stack.append(num)
    else:
        dictArr[num] = 1
setStack = sorted(list(set(stack)), reverse=True)
print(*setStack)
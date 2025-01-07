n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Write your code here!
cntDict = dict()
for a in arr:
    if cntDict.get(a, 0):
        cntDict[a] += 1
    else:
        cntDict[a] = 1

for num in nums:
    tmp = cntDict.get(num, 0)
    print(tmp, end=" ")
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
stack = []
dictArr = dict()
for num in arr:
    if dictArr.get(num, 0):
        dictArr[num] += 1
    else:
        dictArr[num] = 1
itemsArr = sorted(list(dictArr.items()), key=lambda x:(x[1], x[0]), reverse=True)
for i in range(k):
    iak, iav = itemsArr[i]
    print(iak, end=" ")
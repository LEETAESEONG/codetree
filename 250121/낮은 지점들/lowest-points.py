n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
dictP = dict()
for x, y in points:
    # y값이 0인 경우
    tmp = dictP.get(x, "no")
    if tmp == "no":
        dictP[x] = y
    else:
        if tmp > y:
            dictP[x] = y
answer = sum(list(dictP.values()))
print(answer)
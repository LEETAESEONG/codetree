string = input()

# Write your code here!
dictStr = dict()
lenS = len(string)
for i in range(lenS):
    s = string[i]
    if dictStr.get(s, 0):
        dictStr[s][0] += 1
    else:
        dictStr[s] = [1, i]
sortedStr = sorted(list(dictStr.items()), key=lambda x: (x[1][0], x[1][1]))
if sortedStr[0][1][0] == 1:
    print(sortedStr[0][0])
else:
    print("None")


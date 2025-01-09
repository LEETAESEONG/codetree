import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dictionary = dict()
indexDict = [""] * (n+1)
# Note: Using 1-based indexing for words as per C++ code
for i in range(1, n+1):
    string = input().strip()
    dictionary[string] = i
    indexDict[i] = string
# Write your code here!
for _ in range(m):
    string = input().strip()
    if string.isdigit():
        print(indexDict[int(string)])
    else:
        print(dictionary[string])
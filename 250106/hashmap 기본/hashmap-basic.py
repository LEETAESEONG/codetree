import sys
input = sys.stdin.readline

hashMap = dict()
n = int(input())
for _ in range(n):
    string = input().split()
    command = string[0]
    if command == "add":
        hashMap[string[1]] = string[2]
    elif command == "remove":
        del hashMap[string[1]]
    else:
        print(hashMap.get(string[1], 'None'))

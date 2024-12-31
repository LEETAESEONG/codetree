n, k = map(int, input().split())
nums = list(map(int, input().split()))
tot = nums[0]
answer = 100000
r = 0
for l in range(n):
    while r + 1 <= n and tot + nums[r] <= k:
        tot += nums[r]
        r += 1
    if tot >= k:
        answer = min(answer, r - l + 1)
    tot -= nums[l]
if answer == 100000:
    print(-1)
else:
    print(answer)
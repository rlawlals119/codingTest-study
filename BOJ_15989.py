t = int(input())
cnt = 0

nums = []
for _ in range(t):
    nums.append(int(input()))

maxN = max(nums)
dp1 = [0 for _ in range(maxN + 1)]
dp2 = [0 for _ in range(maxN + 1)]
dp3 = [0 for _ in range(maxN + 1)]

dp1[1] = 1
dp1[2] = 1
dp2[2] = 1
dp1[3] = 1
dp2[3] = 1
dp3[3] = 1

for i in range(4, maxN + 1):
    dp1[i] = dp1[i - 1]
    dp2[i] = dp1[i - 2] + dp2[i - 2]
    dp3[i] = dp1[i - 3] + dp2[i - 3] + dp3[i - 3]

for n in nums:
    print(dp1[n] + dp2[n] + dp3[n])
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = 1000
dp = [[0] * M for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(M):
        if dp[i][j] == 0:
            continue
        dp[i+1][j] = dp[i][j]
        if j+nums[i] < M:
            dp[i+1][j+nums[i]] = 1
print(sum(dp[-1]))

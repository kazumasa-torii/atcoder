import sys
input = sys.stdin.readline

N = int(input())
jump = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(1, N):
    if i == 1:
        dp[i] = dp[i-1] + abs(jump[i-1] - jump[i])
        continue
    dp[i] = min(dp[i-1] + abs(jump[i-1] - jump[i]), dp[i-2] + abs(jump[i-2] - jump[i]))
print(dp[-1])

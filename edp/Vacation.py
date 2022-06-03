import sys
input = sys.stdin.readline
day = int(input())
nums = [list(map(int, input().split())) for _ in range(day)]
nums.insert(0, [0, 0, 0])
dp = [[0] * 3 for _ in range(day+1)]
for i in range(1,day+1):
    dp[i][0] = max(dp[i-1][1] + nums[i][0], dp[i-1][2] + nums[i][0])
    dp[i][1] = max(dp[i-1][0] + nums[i][1], dp[i-1][2] + nums[i][1])
    dp[i][2] = max(dp[i-1][0] + nums[i][2], dp[i-1][1] + nums[i][2])
print(max(dp[day][0], dp[day][1], dp[day][2]))

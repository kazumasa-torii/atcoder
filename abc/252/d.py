N = int(input())
freq = [0] * (2 * 10**5 + 10)
for a in map(int, input().split()):
  freq[a] += 1
dp = [1, 0, 0, 0, 0]
for f in freq:
    if f == 0:
        continue
    nx = [0] * 5
    for i in range(4):
        nx[i + 1] += dp[i] * f
        nx[i] += dp[i]
    dp = nx
print(dp[3])

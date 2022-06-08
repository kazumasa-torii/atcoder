import sys
input = sys.stdin.readline

# 正規の解き方
def main():
    N = int(input())
    li = list(map(int, input().split()))
    minus = 0
    for i in range(N):
        if li[i] < 0:
            minus += 1
            li[i] *= -1
    total = sum(li)
    min_num = min(li)
    print(total if minus % 2 == 0 else total - min_num * 2)

# DPでの解き方
def dp():
    INF = -100000000000000000000000
    N = int(input())
    li = list(map(int, input().split()))
    dp = [[INF] * 2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = max(dp[i][0] + li[i], dp[i][1] - li[i])
        dp[i+1][1] = max(dp[i][0] - li[i], dp[i][1] + li[i])
    print(dp)

main()

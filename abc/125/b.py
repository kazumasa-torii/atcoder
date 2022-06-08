import sys
input = sys.stdin.readline

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    li = []
    for i in range(N):
        li.append(V[i] - C[i])
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i+1] = max(dp[i], dp[i]+li[i])
    print(dp[-1])


main()

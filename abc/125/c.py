import sys
import math
def main():
    input = sys.stdin.readline
    N = int(input())
    li = list(map(int,input().split()))

    #累積GCD
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        # 前からgcdしていき前から挿入していく
        left[i + 1] = (math.gcd(left[i], li[i]))
        # 後ろからgcdを求めていき後ろに挿入
        right[N - i - 1] = (math.gcd(right[N - i], li[N - 1 - i]))

    ans = 0
    for i in range(N):
        # 一つの値を抜いた状態でのGCDを求めていく
        ans = max(ans, math.gcd(left[i],right[i + 1]))
    print(ans)

main()

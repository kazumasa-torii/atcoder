"""
for 一つで考える
"""
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if i + 1 < N:
            if P[i-1] < P[i] < P[i+1] or P[i-1] > P[i] > P[i+1]:
                ans += 1
    print(ans)

    return

main()

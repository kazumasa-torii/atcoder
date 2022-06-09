import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        p: int = 1
        x: int = i
        while x < K:
            p *= 0.5
            x *= 2
        ans += p/N
    print(ans)


main()

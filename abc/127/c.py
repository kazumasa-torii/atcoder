import sys
input = sys.stdin.readline

def main():
    INF = 10 ** 8
    N, M = map(int, input().split())
    L = 0
    R = INF
    for _ in range(M):
        l, r = map(int, input().split())
        L = max(L, l)
        R = min(R, r)
    if L > R:
        print(0)
        sys.exit()
    print(R-L+1)
    return

main()

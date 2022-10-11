import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = int(1e19)
    sa = sum(a)
    ass = 0
    for i in range(n):
        ass += a[i]
        if i + 1 < n: ans = min(ans, abs(sa-(ass*2)))
    print(ans)
    return

if __name__ == '__main__':
    main()
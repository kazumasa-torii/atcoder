import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    p = [[i+1] for i in range(n)]
    for _ in range(m):
        a = list(map(int, input().split()))
        for i in a[1:]:
            p[i-1].extend(a[1:])
    for i in p:
        tmp = set()
        for j in i:
            tmp.add(j)
        if len(tmp) != n:exit(print('No'))
    print('Yes')
    return

if __name__ == '__main__':
    main()
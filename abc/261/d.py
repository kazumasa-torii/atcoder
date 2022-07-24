import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    coin = defaultdict(int)
    ms = int()
    mb = int()
    for _ in range(m):
        c, y = map(int, input().split())
        coin[c] = y
        if mb <= y:
            mb = y
            ms = c
    idx = 0
    zan = n
    total = 0
    mx = x.index(max(x))
    for i in range(n):
        if zan > ms and idx >= ms and mx != i:
                idx = 0
                continue
        idx += 1
        zan -= 1
        total += x[i]
        total += coin[idx]

    print(total)
    return

if __name__ == '__main__':
    main()

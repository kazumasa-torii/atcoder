import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    n, m, t = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    dic = defaultdict(int)
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        dic[x] = y
    for i in range(n):
        t -= a[i]
        if t <= 0: break
        t += dic[i]
    else:exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()
